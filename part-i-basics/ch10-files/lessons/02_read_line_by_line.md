## Read a File Line-by-Line

Often, you'll want to read one line at a time from a file. This allows the
developer to review each line's content and potentially perform different tasks
depending on whether or not the line contains specific text.

For this example, I have provided the following text file:  
[pi_digits.txt](./Files/pi_digits.txt)

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Read a File Line-by-Line

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Looping Over the `open()` File Handler

The `TextIOWrapper` object returned by the `open()` function is already
iterable. You can traverse the content as though it were a list, where the
items are the lines (text blocks separated by newline characters).

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        print(line.rstrip())
```

Output:

```
3.1415926535
  8979323846
  2643383279
```

The code file adds a blank line after each example, so the output is easier to
read.

---

### Using the `readlines()` Method

Sometimes you'll do a lot of work on each line, and you'd rather not keep the file
open while you do it. In that case, you can read every line into a list first with
the `readlines()` method, and then close the file before processing the lines.

The trade-off is memory. `readlines()` loads every line into memory at once, which
is fine for a small file like this one, but can be a problem for a very large file.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
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

### Using `splitlines()`

With the `Path` class, after you read the text, you can use the `splitlines()`
method from the `str` class to create a list of lines to parse.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

lines = text.splitlines()
for line in lines:
    print(line.rstrip())
```

Output:

```
3.1415926535
  8979323846
  2643383279
```

</details>

---
