"""
Identify current directory
"""

import os


def get_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir


if __name__ == '__main__':
    dir_path = get_path()
    print("Print current Path", dir_path)
