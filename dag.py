import re
from pathlib import Path
from typing import Dict, List, Tuple


class DAGMermiad:
    def __init__(self):
        self.pattern = r"(?:!)?\[\[(?![^\]]*\.(?:png|jpg|jpeg|gif|svg|webp))[^\]]*\]\]"
        self.ignore_filepaths = ["content/index.md", "content/dependency_graph.md"]

    def find_subdirectories(self, base_dir: str) -> List[str]:
        """找到所有包含 .md 文件的子目录"""
        subdirs = []
        base_path = Path(base_dir)
        for item in base_path.iterdir():
            if item.is_dir():
                # 检查目录下是否有 .md 文件（递归检查）
                if any(item.rglob("*.md")):
                    subdirs.append(str(item))
        return subdirs

    def filter_files_by_directory(self, filepath_list: List[str], dir_path: str) -> List[str]:
        """过滤出属于指定目录及其子目录的文件"""
        dir_path_obj = Path(dir_path)
        result = []
        for filepath in filepath_list:
            filepath_obj = Path(filepath)
            try:
                # 检查文件是否在指定目录下
                filepath_obj.relative_to(dir_path_obj)
                result.append(filepath)
            except ValueError:
                # 文件不在指定目录下
                pass
        return result

    def find_all_filepaths(self, dir_path: str) -> List[str]:
        """递归查找目录下所有 .md 文件路径"""
        base_path = Path(dir_path)
        return [str(p) for p in base_path.rglob("*.md")]

    def filter_filepaths(self, filepath_list: List[str], pattern: str = None) -> List[str]:
        if pattern is None:
            pattern = self.pattern
        result_filepath_list = []
        for filepath in filepath_list:
            with open(filepath, "r") as f:
                text = f.read()
                reference_list = re.findall(pattern, text)
                if reference_list:
                    result_filepath_list.append(filepath)
        return result_filepath_list

    def find_dependencies(self, filepath_list: List[str], pattern: str = None) -> Dict[str, List[str]]:
        if pattern is None:
            pattern = self.pattern
        result_dict = {}
        for filepath in filepath_list:
            # 忽略所有 dependency_graph.md 文件
            if filepath.endswith("dependency_graph.md"):
                continue
            with open(filepath, "r") as f:
                text = f.read()
                reference_list = re.findall(pattern, text)
                result_dict[filepath] = reference_list

        for filepath in self.ignore_filepaths:
            if filepath in result_dict:
                result_dict.pop(filepath)
        return result_dict

    def unify_format(self, dependencies_dict: Dict[str, List[str]]) -> Dict[str, List[Tuple[str, str]]]:
        """统一格式，返回 Dict[filepath, List[(ref_path, link_type)]]，link_type 为 'ref'（普通引用）或 'include'（![[...]] 嵌入）。"""
        result = {}
        for filepath, reference_list in dependencies_dict.items():
            filepath = filepath.replace("content/", "").replace(".md", "")
            result[filepath] = []
            for raw in reference_list:
                is_include = raw.strip().startswith("!")
                ref = raw.replace("!", "").replace("[", "").replace("]", "")
                ref = re.sub(r"#.*", repl="", string=ref).strip()
                if ref == "dependency_graph" or ref.endswith("/dependency_graph"):
                    continue
                link_type = "include" if is_include else "ref"
                result[filepath].append((ref, link_type))
        return result

    def generate_mermaid_graph(self, dependencies_dict: Dict[str, List[Tuple[str, str]]]) -> str:
        """生成 Mermaid 图：普通引用 [[...]] 用实线 -->，嵌入 ![[...]] 用虚线 -.->。"""
        result_str = "```mermaid\n"
        result_str += "graph TD\n"
        name_to_id = {}
        count = 0
        for filepath, reference_list in dependencies_dict.items():
            name_id = name_to_id.get(filepath, None)
            if name_id is None:
                name_id = count
                count += 1
                name_to_id[filepath] = name_id
            for reference, _ in reference_list:
                reference_id = name_to_id.get(reference, None)
                if reference_id is None:
                    reference_id = count
                    count += 1
                    name_to_id[reference] = reference_id

        for filepath, reference_list in dependencies_dict.items():
            for reference, link_type in reference_list:
                edge = "-.->" if link_type == "include" else "-->"
                result_str += f'{name_to_id[reference]}["{reference}"] {edge} {name_to_id[filepath]}["{filepath}"]\n'
        result_str += "```"
        return result_str

    def transitive_reduction(
        self, dependencies_dict: Dict[str, List[Tuple[str, str]]]
    ) -> Tuple[Dict[str, List[Tuple[str, str]]], List[Tuple[str, str, str]]]:
        """移除冗余依赖：若A可经由其他路径到达C，则移除A对C的直接依赖。
        例如A依赖B和C，B依赖C，则A对C的直接依赖是冗余的，只保留A→B。
        返回 (精简后的依赖字典, 冗余列表[(filepath_unified, ref_unified, link_type)])。
        """

        def reachable_excluding(node: str, exclude_dep: str) -> dict:
            """从node的所有直接依赖（排除exclude_dep）出发DFS，返回 {可达节点: 到达路径}。"""
            visited: dict[str, list] = {}
            stack = [
                (dep, [node, dep])
                for dep, _ in dependencies_dict.get(node, [])
                if dep != exclude_dep
            ]
            while stack:
                curr, path = stack.pop()
                if curr in visited:
                    continue
                visited[curr] = path
                for next_dep, _ in dependencies_dict.get(curr, []):
                    if next_dep not in visited:
                        stack.append((next_dep, path + [next_dep]))
            return visited

        result = {}
        redundant: List[Tuple[str, str, str]] = []
        for filepath, dep_list in dependencies_dict.items():
            reduced_deps = []
            for ref, link_type in dep_list:
                reachable = reachable_excluding(filepath, ref)
                if ref not in reachable:
                    reduced_deps.append((ref, link_type))
                else:
                    path_str = " -> ".join(reachable[ref])
                    print(f"[冗余依赖] {filepath} -> {ref}\n           替代路径: {path_str}")
                    redundant.append((filepath, ref, link_type))
            result[filepath] = reduced_deps
        return result, redundant

    def remove_redundant_from_files(self, redundant_list: List[Tuple[str, str, str]]) -> None:
        """从原始 .md 文件中删除冗余的 wikilink 引用。"""
        from collections import defaultdict

        file_to_refs: dict = defaultdict(list)
        for filepath_unified, ref_unified, link_type in redundant_list:
            original_path = "content/" + filepath_unified + ".md"
            file_to_refs[original_path].append((ref_unified, link_type))

        for original_path, refs_to_remove in file_to_refs.items():
            with open(original_path, "r", encoding="utf-8") as f:
                content = f.read()

            for ref, link_type in refs_to_remove:
                escaped = re.escape(ref)
                if link_type == "include":
                    pat = r'!\[\[' + escaped + r'(?:#[^\]]*)?]]'
                else:
                    # 匹配 [[ref]] 或 [[ref#section]]，但不匹配 ![[ref]]
                    pat = r'(?<!!)\[\[' + escaped + r'(?:#[^\]]*)?]]'
                content = re.sub(pat, '', content)

            # 清理：合并行内多余空格，移除仅含空白的行（保留空行的段落结构）
            lines = content.splitlines()
            cleaned = [re.sub(r' {2,}', ' ', line).rstrip() for line in lines]
            content = '\n'.join(cleaned)
            if not content.endswith('\n'):
                content += '\n'

            with open(original_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[已修改] {original_path}")

    def generate_subdirectory_dependency_graph(
        self, all_unified_reduced: Dict[str, List[Tuple[str, str]]], subdir_path: str
    ) -> Dict[str, List[Tuple[str, str]]]:
        """从已经 unify_format 且 transitive_reduction 的全局依赖字典中，为子目录生成依赖图。
        对子目录节点做完整的传递依赖展开，使得朴素集合论等根节点能出现在图的顶层。
        """
        subdir_prefix = subdir_path.replace("content/", "") + "/"

        result: Dict[str, List[Tuple[str, str]]] = {}
        to_visit: List[str] = []

        # 先把子目录内的所有节点加入，带上完整 dep list
        for filepath, dep_list in all_unified_reduced.items():
            if filepath.startswith(subdir_prefix):
                result[filepath] = dep_list
                to_visit.append(filepath)

        # BFS 展开所有传递依赖，保留各节点在完整图中的真实 dep list
        while to_visit:
            node = to_visit.pop()
            for ref, _ in result.get(node, []):
                if ref not in result:
                    dep_list = all_unified_reduced.get(ref, [])
                    result[ref] = dep_list
                    to_visit.append(ref)

        return result


def main():
    dag_mermiad = DAGMermiad()
    filepath_list = dag_mermiad.find_all_filepaths(dir_path="content")
    filtered_filepath_list = dag_mermiad.filter_filepaths(filepath_list)
    dependencies_dict = dag_mermiad.find_dependencies(filtered_filepath_list)

    unified_dependencies_dict = dag_mermiad.unify_format(dependencies_dict)
    reduced_dependencies_dict, redundant_list = dag_mermiad.transitive_reduction(unified_dependencies_dict)
    dag_mermiad.remove_redundant_from_files(redundant_list)

    # 生成总的依赖图
    print("Generating main dependency graph...")
    mermaid_graph = dag_mermiad.generate_mermaid_graph(reduced_dependencies_dict)
    with open("content/dependency_graph.md", "w") as f:
        f.write(mermaid_graph)

    # 为每个子目录生成依赖图
    subdirs = dag_mermiad.find_subdirectories("content")
    for subdir in subdirs:
        subdir_name = Path(subdir).name
        print(f"Generating dependency graph for {subdir_name}...")

        subdir_dependencies = dag_mermiad.generate_subdirectory_dependency_graph(reduced_dependencies_dict, subdir)

        subdir_graph_path = Path(subdir) / "dependency_graph.md"
        if subdir_dependencies:
            subdir_mermaid_graph = dag_mermiad.generate_mermaid_graph(subdir_dependencies)
            with open(subdir_graph_path, "w") as f:
                f.write(subdir_mermaid_graph)
        else:
            with open(subdir_graph_path, "w") as f:
                f.write("```mermaid\ngraph TD\n```")


if __name__ == "__main__":
    main()
