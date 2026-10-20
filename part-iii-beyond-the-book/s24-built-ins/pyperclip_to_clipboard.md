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

# Copies to the clipboard
pyperclip.copy("Hello")

# Pastes from the clipboard
my_var = pyperclip.paste()
print(my_var)
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

The script copies `"Hello"` and then reads it back, so the output is the text it
just copied. Because the clipboard is shared with other programs, pasting can
return text you copied elsewhere. Copy something else between runs to see that.

---
