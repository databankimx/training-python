## Merging File Contents

Sometimes the line breaks in a text file are only there to organize the file,
and the data we need to work with in a program has to remove them (and any
other whitespace) and merge the results into a single string.

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
with open(file_path) as file_object:
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

Here, we can create a list of the stripped lines using a comprehension and
simply merge them using the `str` class `join()` method.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_digits.txt")

with open(file_path) as file_object:
    pi_string = "".join(l.strip() for l in file_object)

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

The textbook has us repeat this process with a larger file.

There is no difference in the process, just in the sizes of the file and the
resulting merged string.

```python
pi_string = ""

file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

with open(file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")
```

Output:

Note: We used a slice to only print the first fifty decimal places

```
3.141592653589793238462643383279502884197169399375105
pi_string is 1,000,002 characters long.
```

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
text = path_object.read_text()

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

Here, we can create a list of the stripped lines using a comprehension and
simply merge them using the `str` class `join()` method.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text()

pi_string = "".join(l.strip() for l in text.splitlines())

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

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_million_digits.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text()

pi_string = ""
lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

print(pi_string[:53])
print(f"pi_string is {len(pi_string):,} characters long.\n")
```

Output:

Note: We used a slice to only print the first fifty decimal places

```
3.141592653589793238462643383279502884197169399375105
pi_string is 1,000,002 characters long.
```

</details>

---
