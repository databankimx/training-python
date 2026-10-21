## Merging File Contents

Sometimes the line breaks in a text file only organize the file. To work with
the data in a program, we often need to remove them, along with any other
whitespace, and merge the lines into one string.

For this example, I have provided the following text files:

* [pi_digits.txt](./Files/pi_digits.txt)
* [pi_million_digits.txt](./Files/pi_million_digits.txt)

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Merge File Lines into a Single String

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Looping Lines and Concatenating to a String

Here, we'll use the same process we used in the previous lesson to obtain the
text lines. Once we've obtained the lines, we can loop through them and add
each line to an output string.

> Notice that we're using `strip()` instead of `rstrip()` because we need to
> remove the leading spaces from some lines as well as the trailing newline
> characters.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

pi_string = ""
with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
```

Output:

```
3.141592653589793238462643383279
pi_string is 32 characters long.
```

---

### Using the `join()` Method and a Comprehension

Now that we're getting further along in our training, it's worth thinking
about alternative methods to perform a given task.

Here, we pass a generator expression to the `str` class `join()` method. The
expression strips each line as `join()` asks for it, so we never build a separate
list of lines.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    pi_string = "".join(line.strip() for line in file_object)

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
```

Output:

```
3.141592653589793238462643383279
pi_string is 32 characters long.
```

---

### Working with a Larger File

The next example repeats this process with a larger file. There is no difference
in the process, just in the sizes of the file and the resulting merged string.

This snippet reuses `ROOT_DIR` from the first example.

```python
pi_string = ""

file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

with open(file_path, encoding="UTF-8") as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")
```

Output:

```
3.141592653589793238462643383279502884197169399375105
pi_string is 1,000,002 characters long.
```

The slice `pi_string[:53]` prints only the first 53 characters: the `3`, the decimal
point, and the first 51 decimal digits.

The code file adds a blank line after each example, so the output is easier to
read.

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Looping Lines and Concatenating to a String

Here, we'll use the same process we used in the previous lesson to obtain the
text lines. Once we've obtained the lines, we can loop through them and add
each line to an output string.

> Notice that we're using `strip()` instead of `rstrip()` because we need to
> remove the leading spaces from some lines as well as the trailing newline
> characters.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

pi_string = ""
lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
```

Output:

```
3.141592653589793238462643383279
pi_string is 32 characters long.
```

---

### Using the `join()` Method and a Comprehension

Now that we're getting further along in our training, it's worth thinking
about alternative methods to perform a given task.

Here, we pass a generator expression to the `str` class `join()` method. The
expression strips each line as `join()` asks for it, so we never build a separate
list of lines.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

pi_string = "".join(line.strip() for line in text.splitlines())

print(pi_string)
print(f"pi_string is {len(pi_string)} characters long.\n")
```

Output:

```
3.141592653589793238462643383279
pi_string is 32 characters long.
```

---

### Working with a Larger File

The next example uses a larger file, with the same process and a bigger result.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_million_digits.txt", "Files")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text(encoding="UTF-8")

lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")
```

Output:

```
3.141592653589793238462643383279502884197169399375105
pi_string is 1,000,002 characters long.
```

The slice `pi_string[:53]` prints only the first 53 characters: the `3`, the decimal
point, and the first 51 decimal digits.

The code file adds a blank line after each example, so the output is easier to
read.

</details>

---
