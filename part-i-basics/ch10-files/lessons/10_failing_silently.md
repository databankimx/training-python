## Failing Silently

Another option when encountering an error is not to inform the user at all.

We can just ignore the error and move on.

For this example, I have provided the following text files:  
• [alice.txt](./Files/alice.txt)  
• [little_women.txt](./Files/little_women.txt)  
• [moby_dick.txt](./Files/moby_dick.txt)  
• [siddhartha.txt](./Files/siddhartha.txt)

All of these text files are public domain and are pulled from 
[Project Gutenberg](https://www.gutenberg.org)

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### Ignoring Errors - Silent Failure

Select the edition of the textbook you're using below to see the 
relevant lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Bypassing the Exception

To tell the interpreter not to do anything, we use the keyword `pass`

> WARNING: This is extremely risky, as you will neither be handling nor 
> recording errors
> 
> * This can result in unexpected issues in downstream code
> * You **will** be required to justify this on code reviews

We'll modify the same function we used in a previous lesson, except that
now we will not provide a message to the user when an error occurs.

```python
import os

ROOT_DIR = os.path.dirname(__file__)

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.\n")
```

We can then call the function to count the words in each of a list of file
names, like this:

```python
file_names = [
    "alice.txt",
    "siddhartha.txt",
    "alice_missing.txt",
    "moby_dick.txt",
    "little_women.txt"
]
for file_name in file_names:
    count_words(file_name)
```

Output:

```
The file alice.txt has about 29465 words.
The file siddhartha.txt has about 42172 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

The output does not mention the missing file.

---

### Logging the Error

We can improve this by logging our errors to a text file.

We'll accomplish this by writing to a new file while we're reading the
text file.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log")

def log_words(file_name):
    """Get the approximate word count from a file."""
    file_path = os.path.join(ROOT_DIR, "Files", file_name)
    try:
        with open(file_path, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        with open(log_path, "a", encoding="utf-8") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "missing.txt"]
for file_name in file_names:
    log_words(file_name)
```

Output:

```
The file alice.txt has about 29465 words.
The file siddhartha.txt has about 42172 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

In `./Files/missing_files.log`

```
Missing File:
"... \Files\alice_missing.txt"

```

Even though the user output doesn't mention the missing file, the data
is now logged, so the `pass` is less of a crime now.

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Bypassing the Exception

To tell the interpreter not to do anything, we use the keyword `pass`

> WARNING: This is extremely risky, as you will neither be handling nor 
> recording errors
> 
> * This can result in unexpected issues in downstream code
> * You **will** be required to justify this on code reviews

We'll modify the same function we used in a previous lesson, except that
now we will not provide a message to the user when an error occurs.

```python
from relative_paths import get_path
from pathlib import Path

def count_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")
```

We can then call the function to count the words in each of a list of file
names, like this:

```python
file_names = [
    "alice.txt",
    "siddhartha.txt",
    "alice_missing.txt",
    "moby_dick.txt",
    "little_women.txt"
]
for file_name in file_names:
    count_words(file_name)
```

Output:

```
The file alice.txt has about 29465 words.
The file siddhartha.txt has about 42172 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

The output does not mention the missing file.

---

### Logging the Error

We can improve this by logging our errors to a text file.

We'll accomplish this by writing to a new file while we're reading the
text file.

```python
from relative_paths import get_path
from pathlib import Path

log_file = Path(get_path("missing_files.log", "Files"))

def log_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        with log_file.open("a", encoding="utf-8") as l:
            l.write(f"Missing File:\n\"{file_path}\"\n\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ["alice.txt", "siddhartha.txt", "alice_missing.txt", "moby_dick.txt", "little_women.txt"]
for file_name in file_names:
    log_words(file_name)
```

Output:

```
The file alice.txt has about 29465 words.
The file siddhartha.txt has about 42172 words.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

In `./Files/missing_files.log`

```
Missing File:
"... \Files\alice_missing.txt"
```

Even though the user output doesn't mention the missing file, the data
is now logged, so the `pass` is less of a crime now.

</details>

---
