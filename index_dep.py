#!/usr/bin/env python3
"""
检测每个目录的 index.md 文件是否包含依赖图引用，
如果没有则在开头（frontmatter 之后）插入。
"""

import os
import re
from pathlib import Path


def has_dependency_graph(content: str, dir_name: str) -> bool:
    """检查内容是否包含该目录的依赖图引用"""
    # 匹配格式: ![[目录名/dependency_graph]]
    pattern = rf'!\[\[{re.escape(dir_name)}/dependency_graph\]\]'
    return bool(re.search(pattern, content))


def insert_dependency_graph(content: str, dir_name: str) -> str:
    """在 frontmatter 之后插入依赖图引用"""
    # 匹配 frontmatter: ---\n...\n---\n
    frontmatter_pattern = r'^(---\n.*?\n---\n)'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        # 有 frontmatter，在之后插入
        frontmatter = match.group(1)
        rest = content[len(frontmatter):]
        # 如果 rest 开头有换行，保留；否则添加一个
        if rest.startswith('\n'):
            return frontmatter + f'![[{dir_name}/dependency_graph]]\n' + rest
        else:
            return frontmatter + f'\n![[{dir_name}/dependency_graph]]\n\n' + rest
    else:
        # 没有 frontmatter，在开头插入
        if content.startswith('\n'):
            return f'![[{dir_name}/dependency_graph]]' + content
        else:
            return f'![[{dir_name}/dependency_graph]]\n\n' + content


def create_index_file(dir_name: str) -> str:
    """创建新的 index.md 文件内容"""
    return f"""---
title: {dir_name}
---

![[{dir_name}/dependency_graph]]

"""


def process_directory(content_dir: Path):
    """处理 content 目录下的所有子目录"""
    processed = []
    created = []
    skipped = []
    
    # 遍历所有子目录
    for item in content_dir.iterdir():
        if not item.is_dir():
            continue
        
        dir_name = item.name
        index_file = item / 'index.md'
        dependency_graph_file = item / 'dependency_graph.md'
        
        # 检查是否有 dependency_graph.md 文件
        if not dependency_graph_file.exists():
            continue
        
        # 检查是否有 index.md 文件
        if not index_file.exists():
            # 创建新的 index.md 文件
            try:
                new_content = create_index_file(dir_name)
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✨ {dir_name}: 已创建 index.md 并插入依赖图引用")
                created.append(dir_name)
                continue
            except Exception as e:
                print(f"❌ {dir_name}: 创建文件失败 - {e}")
                skipped.append(dir_name)
                continue
        
        # 读取 index.md 内容
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ {dir_name}: 读取文件失败 - {e}")
            continue
        
        # 检查是否已有依赖图引用
        if has_dependency_graph(content, dir_name):
            print(f"✓   {dir_name}: 已包含依赖图引用")
            continue
        
        # 插入依赖图引用
        new_content = insert_dependency_graph(content, dir_name)
        
        # 写回文件
        try:
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {dir_name}: 已插入依赖图引用")
            processed.append(dir_name)
        except Exception as e:
            print(f"❌ {dir_name}: 写入文件失败 - {e}")
    
    print(f"\n总结:")
    print(f"  - 已创建: {len(created)} 个 index.md 文件")
    print(f"  - 已更新: {len(processed)} 个目录")
    print(f"  - 已跳过: {len(skipped)} 个目录（处理失败）")
    if created:
        print(f"\n已创建 index.md 的目录: {', '.join(created)}")
    if processed:
        print(f"已插入依赖图的目录: {', '.join(processed)}")


def main():
    """主函数"""
    # 获取脚本所在目录
    script_dir = Path(__file__).parent
    content_dir = script_dir / 'content'
    
    if not content_dir.exists():
        print(f"❌ 错误: content 目录不存在: {content_dir}")
        return
    
    print(f"开始处理目录: {content_dir}\n")
    process_directory(content_dir)


if __name__ == '__main__':
    main()
