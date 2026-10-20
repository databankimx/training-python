## Storing User Data as JSON

One common use case for storing data between executions is maintaining
information about the user or the state of the application.

Users tend to expect to some degree that an application will "remember"
them the next time they use it.

---

### How to Store User Information

Let's create a mechanism that allows us to accept input from the user
and store it to a file as a JSON string.

First, we'll request information about the user.

```python
user = {}
user["first_name"] = input("Enter your first name:\n> ")
user["last_name"] = input("Enter your last name:\n> ")
user["username"] = \
    f"{user['first_name'][0]}{user['last_name']}".upper()
```

Output:

```
Enter your first name:
> john
Enter your last name:
> smith
```

We can use this code with both the 2nd and 3rd edition processes below.

Select the edition of the textbook you're using below to see the 
relevant lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Remembering a User

Now, we'll store the JSON file containing the user
information we obtained:

```python
import os
import json

ROOT_DIR = os.path.dirname(__file__)
file_name = "user.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

with open(file_path, "w") as f:
    json.dump(user, f)
print(f"We'll remember you when you come back, {user['username']}")
```

Output:

```
We'll remember you when you come back, JSMITH
```

Content of `user.json` file:

```
{"first_name": "john", "last_name": "smith", "username": "JSMITH"}
```

---

### Retrieving a Remembered User

To retrieve data from a remembered user, we open the same JSON file and load
its contents back into a dictionary. Here, the code reads the file directly,
without a separate function. In the next lesson, we'll move this logic into
functions.

```python
with open(file_path) as f:
    user = json.load(f)
print(f"Welcome back, {user['username']}")
```

Output:

```
Welcome back, JSMITH
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Remembering a User

Now, we'll store the JSON file containing the user
information we obtained:

```python
from relative_paths import get_path
from pathlib import Path
import json

file_name = "user.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)
file.write_text(json.dumps(user))

print(f"We'll remember you when you come back, {user['username']}")
```

Output:

```
We'll remember you when you come back, JSMITH
```

Content of `user.json` file:

```
{"first_name": "john", "last_name": "smith", "username": "JSMITH"}
```

---

### Retrieving a Remembered User

To retrieve data from a remembered user, we read the same JSON file with
`pathlib` and load its contents back into a dictionary. Here, the code reads
the file directly, without a separate function. In the next lesson, we'll move
this logic into functions.

```python
user = json.loads(file.read_text())
print(f"Welcome back, {user['username']}")
```

Output:

```
Welcome back, JSMITH
```

</details>

---
