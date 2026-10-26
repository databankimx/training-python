## Working with JSON Files

JSON (JavaScript Object Notation) is a text format for representing an object or
collection of objects as a string.

The structure of JSON is very similar to the structure of a dictionary and allows
storing values, lists, and nested objects or dictionaries.

For example, if I have a dictionary like this:

```python
my_dict = {
    "name": {
        "first": "john",
        "last": "doe"
    },
    "age": 25,
    "subjects": ["python", "json files"]
}
```

The JSON representation would look nearly identical to the dictionary:

```json
{
    "name": {
        "first": "john",
        "last": "doe"
    },
    "age": 25,
    "subjects": ["python", "json files"]
}
```

The main differences are in the special values. JSON uses `true`, `false`, and
`null` where Python uses `True`, `False`, and `None`. Keep that in mind when you
move values between the two.

This makes JSON a good fit for storing data in external files between executions.

---

### How to Work with JSON

Python provides the `json` module in the Python Standard Library, which exposes
functions for reading and writing JSON files.

The code file clears the terminal and pauses between sections, so you can read each
output before the next one appears.

---

<details>
<summary>2nd Edition Method</summary>

### Writing JSON to a File

Here, we'll store a simple object as JSON in a file.

For this, we'll import the `json` module and use the `json.dump` function to write
it to a file.

```python
import json
import os

ROOT_DIR = os.path.dirname(__file__)

numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)
with open(file_path, "w", encoding="UTF-8") as f:
    json.dump(numbers_object, f)

print(f"Stored JSON file [{file_name}]")

with open(file_path, encoding="UTF-8") as f:
    print(f.read().rstrip())
```

Output:

```
Stored JSON file [numbers.json]
{"numbers": [2, 3, 5, 7, 11, 13]}
```

---

### Loading JSON from a File

The `json` module also exposes the `json.load()` method, which reads JSON from a
file and stores its result in a dictionary.

```python
import os
import json

ROOT_DIR = os.path.dirname(__file__)

file_name = "numbers.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path, encoding="UTF-8") as f:
    numbers_object = json.load(f)

print(numbers_object)
```

Output:

```
{'numbers': [2, 3, 5, 7, 11, 13]}
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Writing JSON to a File

Here, we'll store a simple object as JSON in a file.

For this, we'll import the `json` module. Since we are using a `Path` object, we'll
convert the data to a string with the `json.dumps()` method before writing it to the
file, because `write_text()` writes text.

```python
import json
from relative_paths import get_path
from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]
numbers_object = {"numbers" : numbers}

file_name = "numbers.json"
file_path = get_path("numbers.json", "Files")

contents = json.dumps(numbers_object)
file = Path(file_path)
file.write_text(contents, encoding="UTF-8")

print(f"Stored JSON file [{file_name}]")

print(file.read_text(encoding="UTF-8"))
```

Output:

```
Stored JSON file [numbers.json]
{"numbers": [2, 3, 5, 7, 11, 13]}
```

---

### Loading JSON from a File

The `json` module also exposes the `json.loads()` method, which reads JSON from a
string (in this case, the text read from a file) and stores its result in a
dictionary.

```python
from relative_paths import get_path
from pathlib import Path
import json

file_name = "numbers.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
numbers_object = json.loads(file.read_text(encoding="UTF-8"))

print(numbers_object)
```

Output:

```
{'numbers': [2, 3, 5, 7, 11, 13]}
```

</details>

---
