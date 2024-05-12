import os
import shutil


def remove_python_cache_files():
    IGNORE_FOLDERS = ['.venv']  # List of folders to ignore
    
    for root, dirs, files in os.walk(os.getcwd()):
        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for name in files + dirs:
            if name.endswith(('.pyc', '.pyo')) or name == '__pycache__':
                path = os.path.join(root, name)
                if os.path.isfile(path):
                    os.remove(path)
                elif os.path.isdir(path):
                    # Remove all files and subdirectories within the directory
                    shutil.rmtree(path)


if __name__ == "__main__":
    remove_python_cache_files()
