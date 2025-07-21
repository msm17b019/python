"""
You are given a directory which contains:
- files and folders
- folders can container more files and folders

Goal: Delete duplicate files based on filename (i.e., if two files have the same name anywhere in the directory tree, keep one and delete the rest).
"""

import os

def delete_duplicate_filenames(root_path):
    seen = set()
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename in seen:
                full_path = os.path.join(dirpath, filename)
                print(f"Deleting duplicate file: {full_path}")
                try:
                    os.remove(full_path)
                except Exception as e:
                    print(f"failed to delete {full_path}: {e}")
            else:
                seen.add(filename)
