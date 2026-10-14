## Command-Line Arguments

One of the common tasks required of a terminal program is to accept user 
arguments entered on the command line.

This allows you to take in information from the user and define program 
behaviors based on that data.

---

### Reading Script Name from `sys.argv`

In the built-in `sys` (system functionality) library, Python exposes the
`argv` element, which contains (as a list) the arguments entered on the command line.

We can review the list with the following code:

```python
import sys

print(len(sys.argv))
print(sys.argv)
```

When we call this using `python .\filename.py`, we see the following output:

```
1
['.\\01_command_args.py']
```

This shows that the script name itself (passed to the Python interpreter) is
included in the command-line arguments and will always be `argv[0]`

---

### Parsing the Script Name

Depending on the context in which you run the script, `argv[0]` may contain
a longer (and arguably less useful) file path.

We can modify our code to parse out just the file name using:

Code:

```python
import sys

# Paths may be separated with either forward or backward slashes
separator = "\\" if "\\" in sys.argv[0] else "/"
script_name = sys.argv[0].split(separator)[-1] 
print(f"I am running {script_name}")
```

Command:

```pwsh
python .\filename.py
```

Output:

```
I am running filename.py
```

---

### Reading Additional Arguments

The command line is split into arguments on any space character outside of
delimiting quotation marks

To read the remaining command-line arguments, we'll loop over the arguments
list starting from index `1`, since we don't need the file path.

Code:

```python
import sys

separator = "\\" if "\\" in sys.argv[0] else "/"
script_name = sys.argv[0].split(separator)[-1] 
print(f"I am running {script_name}")

print("My command line arguments are")

for i in range(1, len(sys.argv)):
    print(f" - {sys.argv[i]}")
```

Command:

```
python .\filename.py arg1 "arg 2"
```

Output:

```
I am running 01_command_args.py
My command line arguments are
 - arg1
 - arg 2
```

Note how enclosing the second argument in quotation marks allowed the enclosed
space to be part of `argv[2]` and not split it into two arguments.

---

### Requiring Arguments

Sometimes your program can't run without some argument(s).

Typically the solution to this is to first verify that enough arguments were 
passed and, if not, provide a message to the user showing the required usage.
The program should only proceed if the proper number of arguments are passed.

We'll imagine a program that expects the user's first and last names as 
arguments.

```python
def greet_user() -> None:
    """Read the user's first and last names from the command line and greet"""

    if len(sys.argv) < 3:
        print("Usage: filename.py first_name last_name")
        exit()

    first_name = sys.argv[1].title()
    last_name = sys.argv[2].title()

    print(f"Hello, {first_name} {last_name}")

greet_user()
```

Bad Command:

```pwsh
python .\filename.py
```

Output:

```
Usage: filename.py first_name last_name
```

---

Good Command:

```
python .\filename.py john smith
```

Output:

```
Hello, John Smith
```

---
