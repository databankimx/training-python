## Getting Text from the User

An **Entry** is a single line of text that the user can type into. Read its
contents with `get()`:

```python
name_entry = tk.Entry(window, width=30)
name = name_entry.get()
```

`get()` always returns a string, even if the user typed a number. Convert it
with `int()` or `float()` when you need a number.

---

### Checking the Input

Users often type spaces, or press the button without typing anything. Call
`strip()` to remove the spaces around the text, then check that something is
left:

```python
name = name_entry.get().strip()
greeting.config(text=f"Hello, {name}!" if name else "Please enter a name.")
```

The conditional expression picks one of two messages. An empty string counts
as false, so a blank name takes the second branch.

---

### Try It

Run the script, type a name, and press the button. Then press the button with
the box empty, and with only spaces in it.

---
