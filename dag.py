import os
import re
from pathlib import Path
from typing import Dict, Set, List
from ls_mlkit.util.sniffer import Sniffer


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
        sniffer = Sniffer()
        filepath_list = sniffer.sniff_file_by_path_pattern(directory_path=dir_path, pattern=".*\.md")
        return filepath_list

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

    def unify_format(self, dependencies_dict: Dict[str, List[str]]) -> Dict[str, List[str]]:
        result = {}
        for filepath, reference_list in dependencies_dict.items():
            filepath = filepath.replace("content/", "").replace(".md", "")
            result[filepath] = []
            for reference in reference_list:
                reference = reference.replace("!", "").replace("[", "").replace("]", "")
                reference = re.sub(pattern="#.*", repl="", string=reference)
                result[filepath].append(reference)
        return result

    def generate_mermaid_graph(self, dependencies_dict: Dict[str, List[str]]) -> str:
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
            for reference in reference_list:
                reference_id = name_to_id.get(reference, None)
                if reference_id is None:
                    reference_id = count
                    count += 1
                    name_to_id[reference] = reference_id

        for filepath, reference_list in dependencies_dict.items():
            for reference in reference_list:
                result_str += f'{name_to_id[reference]}["{reference}"] --> {name_to_id[filepath]}["{filepath}"]\n'
        result_str += "```"
        return result_str

    def generate_subdirectory_dependency_graph(self, all_dependencies_dict: Dict[str, List[str]], subdir_path: str) -> Dict[str, List[str]]:
        """为子目录生成依赖图，包含该子目录内的文件及其依赖关系"""
        # 获取子目录下的所有文件（使用完整路径）
        subdir_files = self.filter_files_by_directory(list(all_dependencies_dict.keys()), subdir_path)
        
        # 收集子目录内的文件及其依赖
        subdir_dependencies = {}
        for filepath in subdir_files:
            if filepath in all_dependencies_dict:
                subdir_dependencies[filepath] = all_dependencies_dict[filepath]
        
        # 统一格式
        unified_subdir_dependencies = self.unify_format(subdir_dependencies)
        
        # 收集所有被引用的文件（统一格式后的路径）
        referenced_files = set()
        for filepath, reference_list in unified_subdir_dependencies.items():
            for reference in reference_list:
                referenced_files.add(reference)
        
        # 添加被引用的文件到依赖图中（如果它们不在子目录中）
        # 需要从 all_dependencies_dict 中找到对应的完整路径，然后统一格式
        all_unified_dict = self.unify_format(all_dependencies_dict)
        for filepath_unified, reference_list in all_unified_dict.items():
            if filepath_unified in referenced_files and filepath_unified not in unified_subdir_dependencies:
                # 这个文件被引用但不在子目录中，需要添加到图中
                unified_subdir_dependencies[filepath_unified] = []
        
        return unified_subdir_dependencies


def main():
    dag_mermiad = DAGMermiad()
    filepath_list = dag_mermiad.find_all_filepaths(dir_path="content")
    filtered_filepath_list = dag_mermiad.filter_filepaths(filepath_list)
    dependencies_dict = dag_mermiad.find_dependencies(filtered_filepath_list)
    
    # 生成总的依赖图
    unified_dependencies_dict = dag_mermiad.unify_format(dependencies_dict)
    mermaid_graph = dag_mermiad.generate_mermaid_graph(unified_dependencies_dict)
    print("Generating main dependency graph...")
    with open("content/dependency_graph.md", "w") as f:
        f.write(mermaid_graph)
    
    # 为每个子目录生成依赖图
    subdirs = dag_mermiad.find_subdirectories("content")
    for subdir in subdirs:
        subdir_name = Path(subdir).name
        print(f"Generating dependency graph for {subdir_name}...")
        
        # 生成子目录的依赖图
        subdir_dependencies = dag_mermiad.generate_subdirectory_dependency_graph(
            dependencies_dict, subdir
        )
        
        # 如果子目录有依赖关系，生成图表
        if subdir_dependencies:
            subdir_mermaid_graph = dag_mermiad.generate_mermaid_graph(subdir_dependencies)
            subdir_graph_path = Path(subdir) / "dependency_graph.md"
            with open(subdir_graph_path, "w") as f:
                f.write(subdir_mermaid_graph)
        else:
            # 如果子目录没有依赖关系，创建一个空的图表
            empty_graph = "```mermaid\ngraph TD\n```"
            subdir_graph_path = Path(subdir) / "dependency_graph.md"
            with open(subdir_graph_path, "w") as f:
                f.write(empty_graph)


if __name__ == "__main__":
    main()
