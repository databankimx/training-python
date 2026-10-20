## Refactoring Code

Thus far, we have created a program with a function that performs the 
following operational processes:

* Generate a file path to `./Files/user.json`
* Check to see if the `user.json` file exists
* Read the `user.json` file and greet the returning user if it exists
* Request data from the user and store a new `user.json` file if it doesn't
  exist.

This code works, but it is only useful for one specific use-case.

This is where refactoring comes in.

---

### Best Practices

The following guidelines are considered best practices when programming in 
Python (or most programming languages for that matter):

* No operational processes should exist outside of functions
* Each function should perform one and only one operational process.
* Variable values should not be hard-coded in functions

In order to make our code follow these guidelines, we need to deconstruct the
single function into multiple functions that perform the individual tasks and
ensure that outside the functions, our code is only calling functions and
presenting results to the user (plus setting any necessary constants).

This process of breaking down and rebuilding the code into modular components
is called *refactoring*.

Below, we'll refactor our existing solution.

> Note: For this lesson, I have split the 2nd and 3rd edition code samples
> into two different python files to prevent name collisions and provide (in
> each case) a complete file showing our solution.

Select the edition of the textbook you're using below to see the 
relevant lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

### Import Libraries

It's best to import any needed libraries at the beginning of the file, so
we'll start with this:

```python
import os
import json
```

---

### Global Constants

Since the program needs to know what file to look for, and we want to avoid 
hard-coding that in the function, we'll set constant values for the filename
and the directory containing it like so:

```python
USER_FILE = "user.json"
USER_DIR = "Files"
```

---

### Function to Get the File Path

Let's create a function that returns the path to the `user.json` file.

```python
def get_user_path() -> str:
    """Returns the path to the user JSON file"""
    root_dir = os.path.dirname(__file__)
    return os.path.join(root_dir, USER_DIR, USER_FILE)
```

---

### Function to Read the File

Now we'll move the process of reading in the user dictionary from the file
into another function:

```python
def read_user_file(file_path: str) -> dict[str, str]:
    """Reads the user JSON file and returns the `user` dictionary"""
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
```

---

### Function to Write the File

Of course, we need a function to write a new JSON file as well

```python
def write_user_file(user: dict[str, str], file_path: str) -> None:
    """Writes the `user` dictionary to the user JSON file"""
    with open(file_path, "w") as f:
        json.dump(user, f)
```

---

### Function to Get Data from the User

And a function is required for getting data from user input

```python
def get_user_input() -> dict[str, str]:
    user = {
        "first_name": input("Enter your first name:\n> "),
        "last_name": input("Enter your last name:\n> ")
    }
    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
    return user
```

---

### Function to Check for a Returning User

Lastly, we need a function to check if this is a new or returning user and
display the appropriate greeting.

```python
def check_returning_user() -> None:
    path = get_user_path()
    user = read_user_file(path)
    if user is None:
        user = get_user_input()
        write_user_file(user, path)
        print(f"We'll remember you next time, {user['username']}")
    else:
        print(f"Welcome back, {user['username']}!")
```

Note how this function calls all of the previous functions at points in its 
process.

---

### Calling our Refactored Code

Now, the only code external to the functions that we have to call is this:

```python
check_returning_user()
```

Output if `user.json` does not exist:

```
Enter your first name:
> john
Enter your last name:
> smith
We'll remember you next time, JSMITH
```

Output if `user.json` does exist:

```
Welcome back, JSMITH!
```

Content of `./Files/user.json`:

```
{"first_name": "john", "last_name": "smith", "username": "JSMITH"}
```

</details>

---

<details>
<summary>3rd Edition Method</summary>

### Import Libraries

It's best to import any needed libraries at the beginning of the file, so
we'll start with this:

```python
from relative_paths import get_path
from pathlib import Path
import json
```

---

### Global Constants

Since the program needs to know what file to look for, and we want to avoid 
hard-coding that in the function, we'll set constant values for the filename
and the directory containing it like so:

```python
USER_FILE = "user.json"
USER_DIR = "Files"
```

---

### Function to Get the File Path

Let's create a function that returns the path to the `user.json` file.

```python
def get_user_path() -> str:
    """Returns the path to the user JSON file"""
    return get_path(USER_FILE, USER_DIR)
```

---

### Function to Read the File

Now we'll move the process of reading in the user dictionary from the file
into another function:

```python
def read_user_file(file_path: str) -> dict[str, str] | None:
    """Reads the user JSON file and returns the `user` dictionary"""
    try:
        path_obj = Path(file_path)
        return json.loads(path_obj.read_text())
    except FileNotFoundError:
        return None
```

---

### Function to Write the File

Of course, we need a function to write a new JSON file as well

```python
def write_user_file(user: dict[str, str], file_path: str) -> None:
    """Writes the `user` dictionary to the user JSON file"""
    path_obj = Path(file_path)
    path_obj.write_text(json.dumps(user))
```

---

### Function to Get Data from the User

And a function is required for getting data from user input

```python
def get_user_input() -> dict[str, str]:
    user = {
        "first_name": input("Enter your first name:\n> "),
        "last_name": input("Enter your last name:\n> ")
    }
    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
    return user
```

---

### Function to Check for a Returning User

Lastly, we need a function to check if this is a new or returning user and
display the appropriate greeting.

```python
def check_returning_user() -> None:
    path = get_user_path()
    user = read_user_file(path)
    if user is None:
        user = get_user_input()
        write_user_file(user, path)
        print(f"We'll remember you next time, {user['username']}")
    else:
        print(f"Welcome back, {user['username']}!")
```

Note how this function calls all of the previous functions at points in its 
process.

---

### Calling our Refactored Code

Now, the only code external to the functions that we have to call is this:

```python
check_returning_user()
```

Output if `user.json` does not exist:

```
Enter your first name:
> john
Enter your last name:
> smith
We'll remember you next time, JSMITH
```

Output if `user.json` does exist:

```
Welcome back, JSMITH!
```

Content of `./Files/user.json`:

```
{"first_name": "john", "last_name": "smith", "username": "JSMITH"}
```

</details>

---

