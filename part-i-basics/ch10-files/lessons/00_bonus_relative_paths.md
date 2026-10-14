## Bonus Pre-Lesson: Accessing Relative Paths

We're about to learn about file handling.

One obstacle in file handling is locating the path to a file.

---

### Types of Paths

There are two different types of file paths to be aware of:

* Absolute Path: complete path to the target file, typically starting with a 
  drive letter, UNC, or URL
* Relative Path: path to the target file relative to the location of the 
  script calling it

In Visual Studio Code, when you execute a Python script, the starting 
directory for a relative path is the directory you have navigated to in your 
terminal instance.

You can target a file properly by making sure that the terminal is in a 
location where it is available.

Or you can provide the full, absolute path to the target file in your code.

Either will work. However, it's inconvenient to have to navigate in the 
terminal or type in an entire disk path every time you want to interact with a 
file.

---

### Accessing a Relative Path in Code:

Alternately, you can come up with a method to obtain the location of the file 
relative to the script and start from there.

This is my preferred mechanism, and I will use it throughout the lesson
samples in this chapter.

### Resource Notes:

**Third Edition**  
For examples related to the 3rd edition of the textbook, I have provided a module [relative_paths.py](./relative_paths.py) that I will import and use for
each lesson. It exposes a `get_path()` method that we can use.

<details>
<summary>relative_paths.py</summary>

```python
"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str | None=None, parent_levels: int | None=0, debug: bool | None=False) -> str:
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
    file_path = path.join(ROOT_DIR, file_name) if folder == None else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool | None=False) -> None:
    """
    Store the root directory

    Parameters:  
    * **debug**: If True, print debug information (optional - default: False)
    """
    global ROOT_DIR
    if ROOT_DIR != None: return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
```

</details><br>

**Second Edition**  
For examples related to the 2nd edition of the textbook, I have included a
process for accessing a relative path in the code files, which is described
below.

---

### Getting a Relative Path in Code

The process used in the 2nd edition examples follows this pattern:

1. Import the `os` library
   ```python
   import os
   ```
2. Obtain the directory where the script is executing
   ```python
   ROOT_DIR = os.path.dirname(__file__)
   ```
3. Create the path to the file to be opened
   ```python
   file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")
   ```

The process used in the 3rd edition examples follows this pattern:

1. Import my `relative_paths` library
   ```python
   from relative_paths import get_path
   ```
2. Call the `get_path()` function
   ```python
   file_path = get_path("pi_digits.txt", "Files")
   ```

### Reading the Files

Once you have the file path (using either method), the two book editions also
demonstrate different methods to actually read the file itself.

Both methods are valid, but within the lessons related to each edition, I will
use that edition's method throughout the code samples.

**Second Edition**  
For examples related to the 2nd edition of the textbook, we use the following
process based on `with open(file_path) as variable_name`:

```python
with open(file_path) as file:
    text = file.read()
    print(text.rstrip())
```

Output:

```
3.1415926535 
  8979323846 
  2643383279
```

---

**Third Edition**  
For examples related to the 3rd edition of the textbook, we use the following
process based on the `pathlib.Path` class:

```python
from pathlib import Path

file = Path(file_path)
contents = file.read_text()
print(contents.rstrip())
```

Output:

```
3.1415926535 
  8979323846 
  2643383279
```

---

