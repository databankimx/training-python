"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str=None, parent_levels: int=0, debug: bool=False) -> str:
    """Returns a relative path to a specified file"""
    initialize(debug)
    for _ in range(parent_levels):
        file_name = path.join("..", file_name)
    file_path = path.join(ROOT_DIR, file_name) if folder is None \
        else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool) -> None:
    """Store the root directory"""
    # pylint: disable=global-statement
    global ROOT_DIR
    if ROOT_DIR is not None:
        return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
