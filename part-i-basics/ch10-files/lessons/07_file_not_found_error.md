## Handling a `FileNotFoundError`

It's inevitable that sometimes our programs will look for files that aren't
there.

The examples in this lesson look for `alice_missing.txt` in the `Files` folder.
That file doesn't exist, which is the point of this lesson.

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Handle a `FileNotFoundError`

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### `FileNotFoundError` Raised During `open(file_path)`

Let's investigate what happens when we look for a missing file.

> Side Note: We use the `split()` method to get just the file name from the full
> path. Splitting the path on the backslash (`\`) separator and taking the last
> piece gives us `alice_missing.txt`.
>
> The backslash is the Windows separator. On other operating systems, the separator
> is `/`, so `os.path.basename()` is a more portable choice for getting the file name.

When the file we attempt to open is missing, Python raises a
`FileNotFoundError`, so we'll handle that in our `except` block. The `else` block
runs only when the file opens successfully.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "alice_missing.txt")

file_name = file_path.split("\\")[-1]

try:
    with open(file_path, encoding="UTF-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    print(f"Found file: {file_name}")
```

Output:

```
Sorry, the file [alice_missing.txt] does not exist.
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### `FileNotFoundError` Raised During `Path.read_text()`

Let's investigate what happens when we look for a missing file.

> Side Note: We use the `split()` method to get just the file name from the full
> path. Splitting the path on the backslash (`\`) separator and taking the last
> piece gives us `alice_missing.txt`.
>
> The backslash is the Windows separator. On other operating systems, the separator
> is `/`, so `os.path.basename()` is a more portable choice for getting the file name.

When the file we attempt to open is missing, Python raises a
`FileNotFoundError`, so we'll handle that in our `except` block. The `else` block
runs only when the file is read successfully.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("alice_missing.txt", "Files")
file_name = file_path.split("\\")[-1]

try:
    file = Path(file_path)
    contents = file.read_text(encoding="UTF-8")
except FileNotFoundError:
    print(f"Sorry, the file [{file_name}] does not exist.")
else:
    print(f"Found file: {file_name}")
```

Output:

```
Sorry, the file [alice_missing.txt] does not exist.
```

</details>

---
