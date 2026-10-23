## Recursion on the File System

A folder on your computer is a tree. Folders are branches, and files are
leaves. To list everything inside a folder, or to add up the size of a folder,
you have to visit every branch and every leaf. This is a natural job for
recursion.

The code for this lesson is in [17_file_system.py](./17_file_system.py).

---

### The Pattern

The directory tree has the same shape as the nested lists we saw in
[Traversing a Nested List](./07_nested_lists.md):

* If an item is a file, it is a *base case*: there is nothing more to visit.
* If an item is a directory, we call the same function on that directory.

---

### Listing a Directory

The `list_directory()` method prints every item it finds. When it reaches a
directory, it calls itself on that directory, and it passes `depth + 1` so the
output is indented:

```python
def list_directory(self, path: str | None = None, depth: int = 1) -> None:
    """List files in a directory and its subdirectories"""
    if path is None:
        path = self.path
    try:
        if depth == 1:
            print(os.path.basename(path))
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            bullet = f"{'  ' * depth}" if depth else ""
            is_dir = os.path.isdir(item_path)
            name = os.path.basename(item_path)
            print(f"{bullet}{name}{'/' if is_dir else ''}")
            if name in self.skip_files:
                if is_dir:
                    print(f"  {bullet}...")
                continue
            if is_dir:
                self.list_directory(item_path, depth + 1)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except PermissionError:
        print(f"Permission denied: '{path}'.")
```

Two things make this safe:

* The `os.path.isdir()` check separates the branches from the leaves.
* The `skip_files` list lets us ignore folders we don't want to visit, such as
  `.venv` or `__pycache__`. Skipping a folder is a way to limit the recursion.

The `PermissionError` case matters on Windows, where some folders can't be read
by a regular user. Without it, one locked folder would stop the whole listing.

---

### Measuring Disk Usage

The `disk_usage()` method adds up the size of a file or folder. For a file, the
size is its own size. For a folder, the size is the total of everything inside
it, found by calling the method again on each item:

```python
def disk_usage(self, path: str | None = None, printout: bool = False) -> int:
    """Return bytes used by a file/folder and any descendants."""
    if path is None:
        path = self.path
    try:
        total = os.path.getsize(path)
        if os.path.isdir(path):
            for filename in os.listdir(path):
                if filename in self.skip_files:
                    continue
                child_path = os.path.join(path, filename)
                total += self.disk_usage(child_path)
    except PermissionError:
        print(f"Permission denied: '{path}'.")
        return 0
    if printout:
        print(f"{total:<7} {path}")
    return total
```

The skip list applies here too. Without it, the total would include large folders
such as `.venv`, which are usually not part of the project's own size. Skipped
folders also don't get a printout line.

> Caveat: `os.path.isdir()` and `os.path.getsize()` follow symbolic links. A link
> that points back up the tree would make this recursion run forever. The skip
> list can prevent that, or the link can be skipped in the code.

---

### Trying It

The script crawls the folder it is in, so you can run it right away:

```pwsh
python 17_file_system.py
```

The listing shows the folder name, then each file and subfolder indented under
it. The final line shows the total number of bytes. The exact output depends on
the folder you run it in, so this is only an illustration:

```
s02-recursion/
  17_file_system.py
  07_nested_lists.md
  ...

Disk Usage: 48,213 bytes
```

---

### Try It Yourself

Change `main()` to crawl a different folder, or call `disk_usage(printout=True)`
to print the size of every item. Each folder's total includes everything inside
it, so the top-level total is the last line the printout shows.

---
