## Handling a `FileNotFoundError`

It's inevitable that sometimes our programs will look for files that aren't 
there.

For this lesson, you'll need to create a path to a file that doesn't exist.

My code uses the relative path `.\Files\alice_missing.txt`

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Handle a `FileNotFoundError`

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### `FileNotFoundError` Thrown During `open(file_path)`

Let's investigate what happens when we look for a missing file.

> Side Note: We want to use the `split()` method, which splits a string into
> a list in two ways:
> * Specifying a split character (in this case `\`)
> * Omitting the splitting character, which defaults to a space ` `

When the file we attempt to open is missing, Python throws a 
`FileNotFoundError`, so we'll handle that in our `except` block.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "alice_missing.txt")

file_name = file_path.split("\\")[-1]

try:
    with open(file_path, encoding='utf-8') as f:
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

### `FileNotFoundError` Thrown During `Path.read_text()`

Let's investigate what happens when we look for a missing file.

> Side Note: We want to use the `split()` method, which splits a string into
> a list in two ways:
> * Specifying a split character (in this case `\`)
> * Omitting the splitting character, which defaults to a space ` `

When the file we attempt to open is missing, Python throws a 
`FileNotFoundError`, so we'll handle that in our `except` block.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("alice_missing.txt", "Files")
file_name = file_path.split("\\")[-1]

try:
    file = Path(file_name)
    contents = file.read_text()
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

---
