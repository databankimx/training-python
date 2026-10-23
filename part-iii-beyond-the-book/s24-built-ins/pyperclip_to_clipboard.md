## The Clipboard with `pyperclip`

The `pyperclip` library copies text to the system clipboard, and reads it back.
Python's standard library doesn't include clipboard access, so the library needs
to be installed first:

```pwsh
python -m pip install pyperclip
```

The code for this lesson is in
[pyperclip_to_clipboard.py](./pyperclip_to_clipboard.py):

```python
"""Copy to the clipboard and paste from it!"""

import pyperclip


def copy_example() -> None:
    """Copy text to the clipboard"""
    # Copies to the clipboard
    pyperclip.copy("Hello")


def paste_example() -> None:
    """Paste text from the clipboard and print it"""
    # Pastes from the clipboard
    my_var = pyperclip.paste()
    print(my_var)


def main() -> None:
    """Copy the text, then paste it back"""
    copy_example()
    paste_example()


if __name__ == "__main__":
    main()
```

---

### Copying

`pyperclip.copy()` puts the text it is given onto the clipboard. Any text that
was there before is replaced.

### Pasting

`pyperclip.paste()` returns whatever text is currently on the clipboard. The
script stores it in `my_var` and prints it.

---

### Output

```
Hello
```

The script copies `"Hello"` and then reads it back, so the output is always the
text it just copied. To see paste return text from elsewhere, comment out the
`copy()` line, copy something in another program first, and then run the script.

---
