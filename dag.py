import re
from pathlib import Path
from typing import Optional


class DAGMermiad:
    foundation = "朴素集合论/naive-set-theory-1"

    def __init__(self):
        self.pattern = r"(?m)^- (\[\[[^\]]+\]\])[ \t]*$"
        self.ignore_filepaths = ["content/index.md", "content/dependency_graph.md"]

    def find_subdirectories(self, base_dir: str) -> list[str]:
        """递归找到 base_dir 下所有包含笔记（非 dependency_graph.md / index.md）的子目录"""
        subdirs = []
        base_path = Path(base_dir)
        for item in sorted(base_path.rglob("*")):
            if item.is_dir():
                if any(p.name not in ("dependency_graph.md", "index.md") for p in item.rglob("*.md")):
                    subdirs.append(str(item))
        return subdirs

    def filter_files_by_directory(self, filepath_list: list[str], dir_path: str) -> list[str]:
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

    def find_all_filepaths(self, dir_path: str) -> list[str]:
        """递归查找目录下所有 .md 文件路径"""
        base_path = Path(dir_path)
        return [str(p) for p in base_path.rglob("*.md")]

    def filter_filepaths(self, filepath_list: list[str], pattern: Optional[str] = None) -> list[str]:
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

    def find_dependencies(self, filepath_list: list[str], pattern: Optional[str] = None) -> dict[str, list[str]]:
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

    def build_note_index(self, filepath_list: list[str]) -> set[str]:
        """收集全部笔记的统一路径（排除 dependency_graph.md）。"""
        notes: set[str] = set()
        for filepath in filepath_list:
            if filepath.endswith("dependency_graph.md") or filepath in self.ignore_filepaths:
                continue
            notes.add(filepath.replace("content/", "").replace(".md", ""))
        return notes

    def resolve_note(self, ref: str, all_notes: set[str], source: str = "") -> str:
        """按最短路径规则将引用解析到真实笔记路径。"""
        if ref in all_notes:
            return ref
        suffix = "/" + ref
        matches = sorted(n for n in all_notes if n.endswith(suffix))
        if len(matches) == 1:
            return matches[0]
        if len(matches) > 1:
            loc = f" (in {source})" if source else ""
            print(f"[歧义引用] {ref}{loc} 匹配多个笔记: {matches}")
        return ref

    def unify_format(
        self, dependencies_dict: dict[str, list[str]], all_notes: Optional[set[str]] = None
    ) -> tuple[dict[str, list[tuple[str, str]]], dict[tuple[str, str, str], list[str]]]:
        """统一格式，返回 (dict[filepath, list[(ref_path, link_type)]], raw_ref_map)。
        link_type 为 'ref'（普通引用）或 'include'（![[...]] 嵌入）。
        raw_ref_map 记录 (filepath, resolved_ref, link_type) -> 原始写法列表，供删除冗余引用时精确匹配。
        """
        result = {}
        raw_ref_map: dict[tuple[str, str, str], list[str]] = {}
        for filepath, reference_list in dependencies_dict.items():
            filepath = filepath.replace("content/", "").replace(".md", "")
            result[filepath] = []
            for raw in reference_list:
                is_include = raw.strip().startswith("!")
                ref = raw.replace("!", "").replace("[", "").replace("]", "")
                # [[路径#标题|显示名]] 中，| 之后只是显示文字，不参与路径
                ref = re.sub(r"\|.*", repl="", string=ref)
                ref = re.sub(r"#.*", repl="", string=ref).strip()
                if ref == "dependency_graph" or ref.endswith("/dependency_graph"):
                    continue
                link_type = "include" if is_include else "ref"
                resolved = self.resolve_note(ref, all_notes, filepath) if all_notes is not None else ref
                result[filepath].append((resolved, link_type))
                raw_ref_map.setdefault((filepath, resolved, link_type), []).append(ref)
        return result, raw_ref_map

    def nodes_tracing_to_foundation(self, dependencies_dict: dict[str, list[tuple[str, str]]]) -> set[str]:
        """沿普通引用回溯，返回能到达 foundation 的节点（含 foundation 自身）。"""
        memo: dict[str, bool] = {}

        def reaches(node: str) -> bool:
            if node == self.foundation:
                return True
            if node in memo:
                return memo[node]
            memo[node] = False
            for ref, link_type in dependencies_dict.get(node, []):
                if link_type == "include":
                    continue
                if reaches(ref):
                    memo[node] = True
                    return True
            return False

        tracing = {node for node in dependencies_dict if reaches(node)}
        tracing.add(self.foundation)
        return tracing

    def _note_url(self, filepath: str) -> str:
        """将统一格式的笔记路径转为 Quartz 站点路径。"""
        segments = [
            re.sub(r"\s", "-", seg).replace("&", "-and-").replace("%", "-percent").replace("?", "").replace("#", "").lower()
            for seg in filepath.split("/")
        ]
        return "/" + "/".join(segments).rstrip("/")

    def generate_mermaid_graph(
        self,
        dependencies_dict: dict[str, list[tuple[str, str]]],
        subdir_prefix: Optional[str] = None,
        trace_dependencies: Optional[dict[str, list[tuple[str, str]]]] = None,
    ) -> str:
        """生成 Mermaid 图：普通引用 [[...]] 用实线 -->，嵌入 ![[...]] 用虚线 -.->。
        传入 subdir_prefix 时为子图着色：叶子、本目录根、跨子图根。
        子图根若在 trace_dependencies 上能回溯到 foundation，则改为绿色。总图不传则不着色。
        """
        result_str = "```mermaid\n"
        result_str += "%%{init: {'flowchart': {'curve': 'stepAfter'}}}%%\n"
        result_str += "graph TD\n"
        name_to_id = {}
        count = 0
        indeg: dict[str, int] = {}
        outdeg: dict[str, int] = {}
        for filepath, reference_list in dependencies_dict.items():
            name_id = name_to_id.get(filepath, None)
            if name_id is None:
                name_id = count
                count += 1
                name_to_id[filepath] = name_id
            indeg.setdefault(filepath, 0)
            outdeg.setdefault(filepath, 0)
            for reference, link_type in reference_list:
                if link_type == "include":
                    continue
                reference_id = name_to_id.get(reference, None)
                if reference_id is None:
                    reference_id = count
                    count += 1
                    name_to_id[reference] = reference_id
                indeg.setdefault(reference, 0)
                outdeg.setdefault(reference, 0)
                outdeg[reference] += 1
                indeg[filepath] += 1

        for filepath, reference_list in dependencies_dict.items():
            for reference, link_type in reference_list:
                if link_type == "include":
                    continue
                result_str += f'{name_to_id[reference]}["{reference}"] --> {name_to_id[filepath]}["{filepath}"]\n'

        if subdir_prefix is not None:
            trace_source = dependencies_dict if trace_dependencies is None else trace_dependencies
            tracing = self.nodes_tracing_to_foundation(trace_source)
            class_ids: dict[str, list[int]] = {"leaf": [], "root": [], "externalRoot": [], "foundationRoot": []}
            for name, node_id in name_to_id.items():
                if indeg.get(name, 0) == 0:
                    if name in tracing:
                        class_ids["foundationRoot"].append(node_id)
                    elif name.startswith(subdir_prefix):
                        class_ids["root"].append(node_id)
                    else:
                        class_ids["externalRoot"].append(node_id)
                elif outdeg.get(name, 0) == 0:
                    class_ids["leaf"].append(node_id)
            styles = {
                "leaf": "fill:#fde68a,stroke:#b45309",
                "root": "fill:#bfdbfe,stroke:#1d4ed8",
                "externalRoot": "fill:#fecaca,stroke:#b91c1c",
                "foundationRoot": "fill:#bbf7d0,stroke:#15803d",
            }
            for class_name, node_ids in class_ids.items():
                if not node_ids:
                    continue
                result_str += f"classDef {class_name} {styles[class_name]}\n"
                result_str += f"class {','.join(str(node_id) for node_id in node_ids)} {class_name}\n"

        for name, node_id in name_to_id.items():
            url = self._note_url(name)
            result_str += f'click {node_id} "{url}" "{name}"\n'

        result_str += "```"
        return result_str

    def transitive_reduction(
        self, dependencies_dict: dict[str, list[tuple[str, str]]]
    ) -> tuple[dict[str, list[tuple[str, str]]], list[tuple[str, str, str]]]:
        """移除冗余依赖：若A可经由其他路径到达C，则移除A对C的直接依赖。
        例如A依赖B和C，B依赖C，则A对C的直接依赖是冗余的，只保留A→B。
        返回 (精简后的依赖字典, 冗余列表[(filepath_unified, ref_unified, link_type)])。
        """

        def reachable_excluding(node: str, exclude_dep: str) -> dict:
            """从node的所有直接依赖（排除exclude_dep）出发DFS，返回 {可达节点: 到达路径}。"""
            visited: dict[str, list] = {}
            stack = [(dep, [node, dep]) for dep, _ in dependencies_dict.get(node, []) if dep != exclude_dep]
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
        redundant: list[tuple[str, str, str]] = []
        for filepath, dep_list in dependencies_dict.items():
            reduced_deps = []
            for ref, link_type in dep_list:
                if link_type == "include":
                    reduced_deps.append((ref, link_type))
                    continue
                reachable = reachable_excluding(filepath, ref)
                if ref not in reachable:
                    reduced_deps.append((ref, link_type))
                else:
                    path_str = " -> ".join(reachable[ref])
                    print(f"[冗余依赖] {filepath} -> {ref}\n           替代路径: {path_str}")
                    redundant.append((filepath, ref, link_type))
            result[filepath] = reduced_deps
        return result, redundant

    def remove_redundant_from_files(
        self,
        redundant_list: list[tuple[str, str, str]],
        raw_ref_map: Optional[dict[tuple[str, str, str], list[str]]] = None,
    ) -> None:
        """从原始 .md 文件中删除作为依赖声明的冗余 wikilink 行。"""
        from collections import defaultdict

        file_to_refs: dict = defaultdict(list)
        for filepath_unified, ref_unified, link_type in redundant_list:
            original_path = "content/" + filepath_unified + ".md"
            raw_candidates = (
                raw_ref_map.get((filepath_unified, ref_unified, link_type), [ref_unified])
                if raw_ref_map is not None
                else [ref_unified]
            )
            for raw_ref in raw_candidates:
                file_to_refs[original_path].append((raw_ref, link_type))

        for original_path, refs_to_remove in file_to_refs.items():
            with open(original_path, "r", encoding="utf-8") as f:
                content = f.read()

            for ref, link_type in refs_to_remove:
                escaped = re.escape(ref)
                if link_type == "include":
                    link_pattern = r"!\[\[" + escaped + r"(?:#[^\]|]*)?(?:\|[^\]]*)?]]"
                else:
                    link_pattern = r"\[\[" + escaped + r"(?:#[^\]|]*)?(?:\|[^\]]*)?]]"
                # 依赖只来自独占一行的顶层列表项；限定删除同样的整行，
                # 避免误删正文中的同名链接或破坏 Markdown 缩进。
                line_pattern = rf"(?m)^- {link_pattern}[ \t]*(?:\r?\n|$)"
                content = re.sub(line_pattern, "", content)

            with open(original_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[已修改] {original_path}")

    def generate_subdirectory_dependency_graph(
        self, all_unified_reduced: dict[str, list[tuple[str, str]]], subdir_path: str
    ) -> dict[str, list[tuple[str, str]]]:
        """从已经 unify_format 且 transitive_reduction 的全局依赖字典中，为子目录生成依赖图。
        目录内节点保留完整依赖并继续展开；跨目录引用只保留直接依赖节点，不再回溯其上游。
        """
        subdir_prefix = subdir_path.replace("content/", "") + "/"

        result: dict[str, list[tuple[str, str]]] = {}
        to_visit: list[str] = []

        # 先把子目录内的所有节点加入，带上完整 dep list
        for filepath, dep_list in all_unified_reduced.items():
            if filepath.startswith(subdir_prefix):
                result[filepath] = dep_list
                to_visit.append(filepath)

        # 目录内继续展开；目录外节点只作为叶子，依赖列表置空
        while to_visit:
            node = to_visit.pop()
            for ref, _ in result.get(node, []):
                if ref in result:
                    continue
                if ref.startswith(subdir_prefix):
                    dep_list = all_unified_reduced.get(ref, [])
                    result[ref] = dep_list
                    to_visit.append(ref)
                else:
                    result[ref] = []

        return result


    def ensure_index_with_graph(self, subdir_path: str) -> None:
        """若子目录下不存在 index.md 则自动创建；若 index.md 中尚未嵌入 dependency_graph，则在正文开头插入。"""
        subdir_obj = Path(subdir_path)
        subdir_rel = subdir_path.replace("content/", "")
        dir_title = subdir_obj.name
        embed_line = f"![[{subdir_rel}/dependency_graph]]"
        index_path = subdir_obj / "index.md"

        if not index_path.exists():
            content = (
                "---\n"
                f"title: {dir_title}\n"
                "tags:\n"
                "  - 索引\n"
                f"  - {dir_title}\n"
                "---\n\n"
                f"{embed_line}\n"
            )
            index_path.write_text(content, encoding="utf-8")
            print(f"[新建索引] {index_path}")
            return

        content = index_path.read_text(encoding="utf-8")
        # 已有任意 dependency_graph 嵌入则更新为当前目录的准确相对路径，避免移动目录后歧义
        embed_pattern = re.compile(r"!\[\[[^\]]*dependency_graph\]\]")
        if embed_pattern.search(content):
            new_content = embed_pattern.sub(embed_line, content, count=1)
            if new_content != content:
                index_path.write_text(new_content, encoding="utf-8")
                print(f"[更新索引] {index_path}")
            return

        # 尚无依赖图嵌入：在 YAML frontmatter 之后（或文件开头）插入
        fm_match = re.match(r"\A(---\r?\n.*?\r?\n---\r?\n*)", content, flags=re.DOTALL)
        if fm_match:
            header = fm_match.group(1).rstrip("\r\n") + "\n\n"
            body = content[fm_match.end() :].lstrip("\r\n")
            new_content = f"{header}{embed_line}\n\n{body}" if body else f"{header}{embed_line}\n"
        else:
            body = content.lstrip("\r\n")
            new_content = f"{embed_line}\n\n{body}" if body else f"{embed_line}\n"

        index_path.write_text(new_content, encoding="utf-8")
        print(f"[插入依赖图] {index_path}")


def main():
    dag_mermiad = DAGMermiad()
    filepath_list = dag_mermiad.find_all_filepaths(dir_path="content")
    all_notes = dag_mermiad.build_note_index(filepath_list)
    dag_mermiad.foundation = dag_mermiad.resolve_note(dag_mermiad.foundation, all_notes)

    filtered_filepath_list = dag_mermiad.filter_filepaths(filepath_list)
    dependencies_dict = dag_mermiad.find_dependencies(filtered_filepath_list)

    unified_dependencies_dict, raw_ref_map = dag_mermiad.unify_format(dependencies_dict, all_notes)
    reduced_dependencies_dict, redundant_list = dag_mermiad.transitive_reduction(unified_dependencies_dict)
    dag_mermiad.remove_redundant_from_files(redundant_list, raw_ref_map)

    # 生成总的依赖图
    print("Generating main dependency graph...")
    mermaid_graph = dag_mermiad.generate_mermaid_graph(reduced_dependencies_dict)
    with open("content/dependency_graph.md", "w") as f:
        f.write(mermaid_graph)

    # 为每个子目录生成依赖图
    subdirs = dag_mermiad.find_subdirectories("content")
    for subdir in subdirs:
        subdir_rel = subdir.replace("content/", "")
        print(f"Generating dependency graph for {subdir_rel}...")

        subdir_dependencies = dag_mermiad.generate_subdirectory_dependency_graph(reduced_dependencies_dict, subdir)

        subdir_graph_path = Path(subdir) / "dependency_graph.md"
        if subdir_dependencies:
            subdir_prefix = subdir.replace("content/", "") + "/"
            subdir_mermaid_graph = dag_mermiad.generate_mermaid_graph(
                subdir_dependencies, subdir_prefix, reduced_dependencies_dict
            )
            with open(subdir_graph_path, "w") as f:
                f.write(subdir_mermaid_graph)
        else:
            with open(subdir_graph_path, "w") as f:
                f.write("```mermaid\n%%{init: {'flowchart': {'curve': 'stepAfter'}}}%%\ngraph TD\n```")

        dag_mermiad.ensure_index_with_graph(subdir)


if __name__ == "__main__":
    main()
