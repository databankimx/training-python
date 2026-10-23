## The Shebang Line

On Linux and macOS, a script whose first line starts with `#!` tells the system
which interpreter should run it. That first line is called the shebang, or
hashbang.

The code for this lesson is in [shebang.py](./shebang.py):

```python
#! python3

# That line starting the script tells the system to use the python3
# interpreter, even if the default is a different version

import sys


def version_example() -> None:
    """Print the version of the Python that runs the script"""
    print(f"Running Python {sys.version_info.major}.{sys.version_info.minor}")


def main() -> None:
    """Run the shebang example"""
    version_example()


if __name__ == "__main__":
    main()
```

---

### What the Line Does

`#! python3` asks the system to run the script with `python3`, even when the
default `python` command points to a different version. The line must be the
very first line of the file.

On Linux and macOS, the script also needs to be marked as executable before it
can be run directly.

---

### On Windows

Windows doesn't use the shebang line to choose an interpreter. Instead, the
`py` launcher picks the version. You can choose a version when you run the script:

```pwsh
py -3 shebang.py
```

The shebang line is still valid Python. It is a comment, so Python ignores it
when it runs the script on Windows.

---

### Output

The script prints the version of the Python that is running it. The shebang
line chooses that version on Linux and macOS, so the output shows whether the
shebang did what you expected:

```
Running Python 3.12
```

The version shown depends on the interpreter, so it will differ between machines.
The shebang line itself is still a comment, so it doesn't print anything.

---
