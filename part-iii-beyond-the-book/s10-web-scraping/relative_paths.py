"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str | None=None, parent_levels: int | None=0,
             debug: bool | None=False) -> str:
    """
    Find the relative path to a specified file

    Parameters:  
    * **file_name**: The name of the file
    * **folder**: The folder the file is stored in (optional - default: None)
    * **parent_levels**: The number of levels above the current directory (optional - default: 0)
    * **debug**: If True, print debug information (optional - default: False)

    **Returns**:  
    The file's relative path
    """
    initialize(debug)
    for _ in range(parent_levels):
        file_name = path.join("..", file_name)
    file_path = path.join(ROOT_DIR, file_name) if folder is None \
        else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool | None=False) -> None:
    """
    Store the root directory

    Parameters:  
    * **debug**: If True, print debug information (optional - default: False)
    """
    # pylint: disable=global-statement
    global ROOT_DIR
    if ROOT_DIR is not None:
        return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
