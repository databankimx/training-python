## Read a File

The simplest file task you can perform in a program is to open and read a
plain text file.

For this example, I have provided the following text file:  
[pi_digits.txt](./Files/pi_digits.txt)

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Read a File

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Using the `open()` Method

Python exposes a function `open()`, which opens the specified file and returns
a file handler `TextIOWrapper` that can be used to read the contents of the
file via its `read()` method. The handler also exposes a `close()` method to
execute when you're done using the file.

> Note: When you read in the content of a text file, it will often end with a
> newline character. To avoid including the extra carriage return, it's often
> useful to use the `rstrip()` method to remove any trailing whitespace
> characters, including newline(s).

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

file_object = open(file_path, encoding="UTF-8")
text = file_object.read()
print(text.rstrip())
file_object.close()
```

Output:

```
3.1415926535
  8979323846
  2643383279
```

The `encoding="UTF-8"` argument tells Python how to turn the bytes in the file
into characters. We'll look at encodings in more detail in the ASCII and UTF-8
bonus lesson.

The code file adds a blank line after each example, so the output is easier to
read.

---

### Using `with open`

Opening the file, doing some work, and then calling `close()` works in most
cases. However, if an error occurs before `close()` is called, the file may stay
open, and on Windows that can stop other programs from using it.

To work around this, Python provides the `with` keyword, which creates a code
block following the `open()` call and automatically closes the file handler
when the block ends, even if there is an error.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    text = file_object.read()
print(text.rstrip())
```

Output:

```
3.1415926535
  8979323846
  2643383279
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Using `pathlib.Path`

The Python library `pathlib` provides an alternative method for reading a file
using its `Path` class. While it may not seem like an improvement on a simple
task, like reading text file content, the `Path` class provides more
streamlined methods to perform file system operations than `open()`.

One advantage is that the functions exposed by `Path` do not require the
developer to explicitly open the file. Opening, closing, and error handling
occur in the library functions, making this a better choice for most
development scenarios.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")
print(text.rstrip())
```

Output:

```
3.1415926535
  8979323846
  2643383279
```

</details>

---
