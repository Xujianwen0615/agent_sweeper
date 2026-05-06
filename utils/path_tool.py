"""
为整个工程提供统一的绝对路径
"""

import os

# 获取文件所在的根目录
def get_project_root():
    # 当前文件的绝对路径
    current_file = os.path.abspath(__file__)

    # 获取工程根目录
    current_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(current_dir)

    return project_root

# 由相对路径获取到绝对路径
def get_abs_path(relative_path):
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)

if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))
    