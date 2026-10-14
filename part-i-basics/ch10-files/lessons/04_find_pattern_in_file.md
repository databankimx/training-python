## Read a File and Search for a Pattern

Another common file system task for a developer is to search a file to see
if a specific pattern appears in the text.

This is so common that most operating systems include utilities for this task.
In Linux, you have `grep`, in Windows you have `findstr.exe`, and in PowerShell
you have `Select-String`.

For this example, I have provided the following text file:  
[pi_million_digits.txt](./Files/pi_million_digits.txt)

Pi is an irrational number, meaning its decimal part continues forever without
repeating. It is widely believed that every possible pattern of digits
eventually occurs in pi, although this has not been proven. Here, we're going to
check if a 6-digit pattern (a birthday)
appears within the first million digits of pi.

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Search for a Pattern in a File

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Find Pattern in File Data

We'll merge the file content into a string, just like we did in the previous
lesson, and then search the resulting data for the string a user enters.

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "pi_million_digits.txt")

pi_string = ""

with open(file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

birthday = input("Enter your birthday in the form MMDDYY:\n> ")

if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appear in the first million digits of pi.")

print()
```

I'll pretend the user entered `010270`

Output:

```
Enter your birthday in the form MMDDYY:
> 010270
Yay! Your birthday appears in the first million digits of pi!
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Find Pattern in File Data

We'll merge the file content into a string, just like we did in the previous
lesson, and then search the resulting data for the string a user enters.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("pi_million_digits.txt", "Files")

pi_string = ""

path_object = Path(file_path)
text = path_object.read_text()

lines = text.splitlines()
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form MMDDYY:\n> ")

if birthday in pi_string:
    print("Yay! Your birthday appears in the first million digits of pi!")
else:
    print("Aww... Your birthday does not appear in the first million digits of pi.")
```

I'll pretend the user entered `030470`

Output:

```
Enter your birthday in the form MMDDYY:
> 030470
Aww... Your birthday does not appear in the first million digits of pi.
```

</details>

---

