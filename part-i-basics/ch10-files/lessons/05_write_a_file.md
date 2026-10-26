## Write a File

Of course, file interaction would be meaningless without the ability to create,
write, and edit files.

The examples in this lesson write to `programming.txt` in the `Files` folder. The
file doesn't exist yet, and writing to it creates it.

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

---

### How to Write to a File

Select the edition of the textbook you're using below to see the relevant
lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Setting the Mode with `open()`

When using the `open()` function, you can specify one of several modes in this
form:  
`open(file_path, mode)`

|Code|Mode|Description|
|:-:|-|-|
|`r`|read|open the file as read-only<br>This is the default mode if the argument is omitted|
|`w`|write|open the file as write-only - any existing data will be replaced|
|`a`|append|open the file and write to the end - any existing data will be retained|
|`r+`|read/write|open the file to both read and write|

There are also a couple of important rules to follow:

* The `TextIOWrapper` doesn't expose a `write_line` method, so you need to
  append your own newline characters.
    * e.g.: `file.write("some line\n")`
* Only strings can be written to file, so numerical data must be converted
  first.
    * e.g.: `file.write(str(12345))`
* Write mode `w` will create the file if it doesn't exist

---

### Writing the File

We will use this code to write the file:

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "programming.txt")

with open(file_path, "w", encoding="UTF-8") as file:
    file.write("I love programming!\n")
    file.write("I love creating new games!\n")
```

### Verifying the File

After writing, we can use the technique we learned already to read the file and
verify that it contains the text we are expecting.

```python
# -- SNIP --

with open(file_path, "r", encoding="UTF-8") as file:
    print(file.read())
```

Output:

```
I love programming!
I love creating new games!

```

---

### Creating a `write_line()` Function

Of course, since we know how to create functions now, it is relatively trivial
to create a `write_line()` function ourselves, so that we don't need to
manually append newline characters every time we write to a file.

```python
def write_line(output_file, text):
    """Write a line to a file"""
    output_file.write(f"{text}\n")
```

Now we can perform our file writing (and verification) like this:

```python
# -- SNIP --

with open(file_path, "w", encoding="UTF-8") as file:
    write_line(file, "I love coding!")
    write_line(file, "I love creating new applications!")

with open(file_path, "r", encoding="UTF-8") as file:
    print(file.read())
```

Output:

```
I love coding!
I love creating new applications!

```

---

### Appending to a File

Often, we don't want to replace the existing content when we write information
to a file. Instead, we may want to append data after the already stored text.

A common case for appending would be when your application is writing to a
log file. You would want to retain all previous log entries in addition to the
new data being written.

For this, we use the `a` mode.

```python
# -- SNIP --

with open(file_path, "a", encoding="UTF-8") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(file_path, "r", encoding="UTF-8") as file_object:
    print(file_object.read())
```

Output:

```
I love coding!
I love creating new applications!
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.

```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Using the `write_text()` Method

The `Path` type exposes a `write_text()` method that we can use to write to a
file.

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("programming.txt", "Files")

file = Path(file_path)

file.write_text("I love programming!\n", encoding="UTF-8")
```

And then we can verify the text we wrote.

```python
print(file.read_text(encoding="UTF-8"))
```

Output:

```
I love programming!

```

---

### Creating a `write_line_to_file()` Function

Like we did with traditional files in the 2nd edition section, we can create
a helper function for ourselves. This one is named `write_line_to_file()`, so it
doesn't clash with the `write_line()` function from the 2nd edition section.

```python
def write_line_to_file(path_object, text):
    """Write a line to a file"""
    path_object.write_text(f"{text}\n")
```

Then we can write to the file without appending a newline every time.

```python
# -- SNIP --

content = """I love programming!
I love creating new games.
I also love working with data."""

write_line_to_file(file, content)

print(file.read_text(encoding="UTF-8"))
```

Output:

```
I love programming!
I love creating new games.
I also love working with data.

```

---

### Appending to a File

Often, we don't want to replace the existing content when we write information
to a file. Instead, we may want to append data after the already stored text.

A common case for appending would be when your application is writing to a
log file. You would want to retain all previous log entries in addition to the
new data being written.

The `Path` class does not expose an append method. However, like a file
handler in the 2nd edition, you can call the `open()` method on a path.

The syntax is a bit different: `with path_object.open(mode)`, but it allows
opening with the `a` (append) mode.

```python
# -- SNIP --

content = "I also love finding meaning in large datasets.\n"
content += "I love creating apps that can run in a browser.\n"

with file.open("a", encoding="UTF-8") as f:
    f.write(content)

print(file.read_text(encoding="UTF-8"))
```

Output:

```
I love programming!
I love creating new games.
I also love working with data.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.

```

</details>

---
