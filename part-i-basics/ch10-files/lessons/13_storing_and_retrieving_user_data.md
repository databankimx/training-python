## Storing and Retrieving User Data Using a JSON File

The next step in designing a "remember me" process is to combine the
steps in the previous code samples.

The new process should:

* Check to see if a user JSON file exists
   
    * If it does exist:
        1. Load the user data from JSON
        2. Greet the user
        3. Skip further steps...

    * If it does not exist
        1. Prompt the user to enter first and last name
        2. Store a user JSON file
        3. Let the user know that we will remember

---

### Combining the Process

For now, let's just build the logic as a single function.

The function uses `json`, `os`, and `ROOT_DIR` from the earlier lessons, so
those names are assumed in the snippets below.

> Note: the process to obtain file paths is covered here:  
> [00_bonus_relative_paths.md](./00_bonus_relative_paths.md)

The code file clears the terminal and pauses between steps, so you can read each
output before the next one appears.

Select the edition of the textbook you're using below to see the
relevant lesson(s).

---

<details>
<summary>2nd Edition Method</summary>

Create a function that handles the proposed design:

```python
def user_check(filepath: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    try:
        with open(filepath, encoding="UTF-8") as f:
            user = json.load(f)
            print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        with open(filepath, "w", encoding="UTF-8") as f:
            json.dump(user, f)
        print(f"We'll remember you when you come back, {user['username']}")
```

Call the function when a file does not exist...

```python
file_path = os.path.join(ROOT_DIR, "Files", "user.json")
user_check(file_path)
```

Output (entering `John` and `Smith`):

```
Enter your first name:
> John
Enter your last name:
> Smith
We'll remember you when you come back, JSMITH
```

Call the function when a file exists...

```python
user_check(file_path)
```

Output:

```
Welcome back, JSMITH
```

The code file makes both calls in a row, with a pause between them. The first run
only shows the prompts if `user.json` doesn't exist yet. If you ran lesson 12, the
file is already there, so you'll see the "Welcome back" message first. Delete
`user.json` from the `Files` folder to see the prompts again.

</details>

---

<details>
<summary>3rd Edition Method</summary>

Create a function that handles the proposed design:

```python
def user_check_from_path(filepath: str) -> None:
    """
    If a user file exists, get the user from it
    Otherwise, create a new file with user input
    """
    file_object = Path(filepath)
    try:
        user = json.loads(file_object.read_text(encoding="UTF-8"))
        print(f"Welcome back, {user['username']}")
    except FileNotFoundError:
        user = {
            "first_name": input("Enter your first name:\n> "),
            "last_name": input("Enter your last name:\n> ")
        }
        user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()
        file_object.write_text(json.dumps(user), encoding="UTF-8")
        print(f"We'll remember you when you come back, {user['username']}")
```

Call the function when a file does not exist...

```python
file_path = get_path("user.json", "Files")
user_check_from_path(file_path)
```

Output (entering `John` and `Smith`):

```
Enter your first name:
> John
Enter your last name:
> Smith
We'll remember you when you come back, JSMITH
```

Call the function when a file exists...

```python
user_check_from_path(file_path)
```

Output:

```
Welcome back, JSMITH
```

The 3rd edition uses `pathlib` to read and write the file, and the
`get_path()` helper to find it. The logic is the same as the 2nd edition.

The code file makes both calls in a row, with a pause between them, and the same
first-run note applies: delete `user.json` from the `Files` folder to see the
prompts again.

</details>

---
