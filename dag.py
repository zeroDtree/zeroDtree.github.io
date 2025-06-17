import os
import re
from pathlib import Path
from typing import Dict, Set, List
from my_utils import Sniffer


class DAGMermiad:
    def __init__(self):
        self.pattern = r"(?:!)?\[\[(?![^\]]*\.(?:png|jpg|jpeg|gif|svg|webp))[^\]]*\]\]"
        self.ignore_filepaths = ["content/index.md", "content/dependency_graph.md"]

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


def main():
    dag_mermiad = DAGMermiad()
    filepath_list = dag_mermiad.find_all_filepaths(dir_path="content")
    filtered_filepath_list = dag_mermiad.filter_filepaths(filepath_list)
    dependencies_dict = dag_mermiad.find_dependencies(filtered_filepath_list)
    unified_dependencies_dict = dag_mermiad.unify_format(dependencies_dict)
    mermaid_graph = dag_mermiad.generate_mermaid_graph(unified_dependencies_dict)
    print(mermaid_graph)
    with open("content/dependency_graph.md", "w") as f:
        f.write(mermaid_graph)


if __name__ == "__main__":
    main()
