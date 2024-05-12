import os
from pathlib import Path
import shutil
import toml


def find_the_absolute_path(path: str, relative_file: str):
    """
    This method is used to find the absolute path for the specified relative path
    Ex
    +-- project
        +-- sub_project_1
            +-- file_1.py
        +-- sub_project_2
            +-- file_2.py
            +-- file_3.py
            +-- sub_project_3
                +-- file_4.py
        +-- setup.py

    Requirement -> absolute file path for the root-project "project" -> /project
    But we are in sub_project_3 and want to get the path for the root then we can use the following function in the following format

    Usage:
    find_the_absolute_path(<path_of_current_file>: /project/sub_project_2/sub_project_3/file_4.py, <relative_file>: "setup.py")
    """
    if relative_file == "":
        return None
    path_segments = list(Path(path).parts)
    for segment_index in range(0, len(path_segments)):
        sub_segments = path_segments[0: len(path_segments)-segment_index]
        sub_segment_path = os.path.join(*sub_segments)
        if os.path.isdir(sub_segment_path):
            files = os.listdir(sub_segment_path)
            for file in files:
                if relative_file == file:
                    return sub_segment_path
    return None


def search_file_path(path_to_start, target_file):
    """
    This function will return the complete path to the specified target file

    Args:
        path_to_start <str> -> Sets the boundary path to search the target file
        target_file <str> -> File name to be searched

    Returns:
        Complete path for the target file <str>
    """
    contents = os.listdir(path_to_start)

    if len(contents) == 0:
        return None

    inner_contents = []
    for content in contents:
        if content == target_file:
            return path_to_start + "/" + content
        else:
            if os.path.isdir(path_to_start + "/" + content):
                inner_contents.append(content)

    for inner_content in inner_contents:
        contents = os.listdir(path_to_start + "/" + inner_content)
        identified_path = search_file_path(
            path_to_start + "/" + inner_content, target_file)
        if identified_path != None:
            return identified_path


class Operations:
    @staticmethod
    def does_file_or_dir_exists(absolute_path: str):
        return os.path.exists(absolute_path)


class FileOperations(Operations):
    """
    This class is responsible to have all the functionalities related to file manipulations
    We will keep methods as static to class
    """

    @staticmethod
    def create_file(file_path):
        try:
            with open(file_path, "x") as file:
                pass
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def delete_file(file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:
            return False

    # TOML extension, file operations

    @staticmethod
    def read_from_toml(file_path):
        try:
            with open(file_path, "r") as toml_file:
                toml_contents = toml.load(toml_file)
                return toml_contents
        except FileNotFoundError:
            return False

    @staticmethod
    def write_to_toml(file_path, toml_content):
        try:
            with open(file_path, "w") as toml_file:
                toml.dump(toml_content, toml_file)
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def create_toml_file_with_default_content(file_path, default_content):
        try:
            FileOperations.create_file(file_path)
            FileOperations.write_to_toml(file_path, default_content)
        except FileNotFoundError:
            return False

    # .TXT extension, file operations
    @staticmethod
    def read_text_file(file_path):
        content = None
        with open(file_path, "r") as file:
            content = file.read()
        return content

    @staticmethod
    def write_text_file(file_path, contents: list):
        with open(file_path, "w") as file:
            for content in contents:
                file.write(f"{content}\n")

    @staticmethod
    def append_text_file(file_path, contents: list):
        with open(file_path, "a") as file:
            for content in contents:
                file.write(f"{content}\n")


class DIROperations(Operations):
    """
    This class is responsible to have all the functionalities / behaviors related to DIR manipulations
    We will keep methods as static to class

    For successful operations we will return True else False 
    """

    @staticmethod
    def make_dir(path):
        try:
            os.mkdir(path)
            return True
        except FileExistsError:
            return False

    @staticmethod
    def remove_dirs(path):
        shutil.rmtree(path)
