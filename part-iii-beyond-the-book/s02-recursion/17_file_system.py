"""Module for file system crawler"""

import os

class DirectoryCrawler():
    """Class for file system crawler"""
    def __init__(self, path: str, skip_files: list[str]=None) -> None:
        self.path = path
        self.skip_files = [] if skip_files is None else skip_files

    def list_directory(self, path: str=None, depth: int = 1) -> None:
        """List files in a directory and its subdirectories"""
        if path is None:
            path = self.path
        try:
            if depth == 1:
                print(path.split("\\")[-1])
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                bullet = f"{'  ' * depth}" if depth else ""
                is_dir = os.path.isdir(item_path)
                name = (item_path).split("\\")[-1] if is_dir \
                    else os.path.basename(item_path)
                print(f"{bullet}{name}{'/' if is_dir else ''}")
                if name in self.skip_files:
                    if is_dir:
                        print(f"  {bullet}...")
                    continue
                if is_dir:
                    self.list_directory(item_path, depth + 1)
        except FileNotFoundError:
            print(f"Directory '{path}' not found.")

    def disk_usage(self, path: str=None, printout: bool=False) -> int:
        """Return bytes used by a file/folder and any descendants."""
        if path is None:
            path = self.path
        total = os.path.getsize(path)
        if os.path.isdir(path):
            for filename in os.listdir(path):
                child_path = os.path.join(path, filename)
                total += self.disk_usage(child_path)
        if printout:
            print (f"{total:<7} {path}")
        return total

SKIP_FILES = [".venv", "__pycache__", "12dicts_dictionaries",
              ".pytest_cache"]

def main() -> None:
    """Test file system crawler"""
    crawler = DirectoryCrawler("C:\\Training\\python-impractical",
                               SKIP_FILES)
    crawler.list_directory()
    usage = crawler.disk_usage()
    print(f"\nDisk Usage: {usage:,} bytes")

if __name__ == "__main__":
    main()
