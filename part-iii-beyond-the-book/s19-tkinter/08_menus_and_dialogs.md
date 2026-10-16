## Menus and Dialogs

A **menu bar** sits along the top of the window. Each menu is a `tk.Menu`, and
each item in it runs a function when chosen:

```python
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="About", command=show_about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label="File", menu=file_menu)
window.config(menu=menubar)
```

* `tearoff=0` stops the menu from being torn off into its own window.
* `add_separator()` draws a line between groups of items.
* `add_cascade()` places a menu inside the menu bar.
* `window.destroy` closes the window. Pass it without brackets, as with any
  other command.

---

### Dialogs

Dialogs are small windows for a single job. The `tkinter` modules have ready-made
ones:

```python
name = simpledialog.askstring("Your name", "What is your name?", parent=window)
messagebox.showinfo("About", "A small tkinter demo.", parent=window)
```

`askstring()` returns `None` if the user cancels, so check for that before
using the value. `showinfo()` shows a message and waits for the user to press
OK.

Pass `parent=window` so the dialog opens on top of your window.

---

### Try It

Open the File menu, choose "Ask for name...", and then cancel the dialog. The
label should not change. Choose it again and enter a name.

---
