## Working with Multiple Files

Often, working with a single, specific file will not meet the needs of a program. Working with lists of files is frequently necessary.

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

### How to Process a List of Files

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### A File Processing Function

For this lesson, we'll take the logic we previously created to handle a
missing file and use it while we loop over a list of files.

Let's start by creating a function that will count the number of words in a
text file. If the file is missing, it will use the logic we previously created 
to gracefully handle a missing file

> Note: In the call to `open()`, we are specifying the keyword argument
> `encoding="utf-8"`. This is necessary because some of the text files include
> accented characters that do not occur in the ASCII encoding.
>
> See [09_bonus_ascii_and_utf8.md](./09_bonus_ascii_and_utf8.md) for a brief
> discussion of text encoding.

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
        print(f"Sorry, the file {file_name} does not exist.\n")
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
Sorry, the file alice_missing.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### A File Processing Function

For this lesson, we'll take the logic we previously created to handle a
missing file and use it while we loop over a list of files.

Let's start by creating a function that will count the number of words in a
text file. If the file is missing, it will use the logic we previously created 
to gracefully handle a missing file.

> Note: In the call to `open()`, we are specifying the keyword argument
> `encoding="utf-8"`. This is necessary because some of the text files include
> accented characters that do not occur in the ASCII encoding.
>
> See [09_bonus_ascii_and_utf8.md](./09_bonus_ascii_and_utf8.md) for a brief
> discussion of text encoding.

```python
from relative_paths import get_path
from pathlib import Path

def count_file_words(file_name):
    """Get the approximate word count from a file."""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        contents = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    except Exception as ex:
        print(ex)
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
    count_file_words(file_name)
```

Output:

```
The file alice.txt has about 29465 words.
The file siddhartha.txt has about 42172 words.
Sorry, the file alice_missing.txt does not exist.
The file moby_dick.txt has about 215830 words.
The file little_women.txt has about 189079 words.
```

</details>

---

