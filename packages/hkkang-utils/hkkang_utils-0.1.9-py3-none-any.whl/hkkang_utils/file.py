import os
import json

from typing import Optional

def get_files_in_directory(dir_path: str, filter_func: Optional[callable] = None) -> list:
    """Get paths of files in a directory
    :param dir_path: path of directory that you want to get files from
    :type dir_path: str
    :param filter_func: function that returns True if the file name is valid
    :type filter_func: callable
    :return: list of file paths in the directory which are valid
    :rtype: list
    """
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and (filter_func is None or filter_func(f))]

def get_files_in_all_sub_directories(root_dir_path: str, filter_func: Optional[callable] = None) -> list:
    """Get paths of files in all sub directories
    :return: list of file paths in all sub directories which are valid
    :rtype: list
    """
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(root_dir_path) for f in filenames if (filter_func is None or filter_func(f))]

def read_json_file(file_path: str) -> dict:
    """Read a json file

    :param file_path: json file path
    :type file_path: str
    :return: json data
    :rtype: dict
    """
    with open(file_path, 'r') as f:
        return json.load(f)