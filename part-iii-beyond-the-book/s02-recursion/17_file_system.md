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
def list_directory(self, path: str=None, depth: int = 1) -> None:
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
```

Two things make this safe:

* The `os.path.isdir()` check separates the branches from the leaves.
* The `skip_files` list lets us ignore folders we don't want to visit, such as
  `.venv` or `__pycache__`. Skipping a folder is a way to limit the recursion.

---

### Measuring Disk Usage

The `disk_usage()` method adds up the size of a file or folder. For a file, the
size is its own size. For a folder, the size is the total of everything inside
it, found by calling the method again on each item:

```python
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
        print(f"{total:<7} {path}")
    return total
```

---

### Trying It

The script crawls the folder it is in, so you can run it right away:

```pwsh
python 17_file_system.py
```

Output:

The listing shows the folder name, then each file and subfolder indented under
it. The final line shows the total number of bytes. Your output will depend on
the folder you run it in.

---

### Try It Yourself

Change `main()` to crawl a different folder, or call `disk_usage(printout=True)`
to print the size of every item. Each folder's total includes everything inside
it, so the top-level total is the last line the printout shows.

---
