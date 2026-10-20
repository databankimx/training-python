## Creating a Window

Every tkinter program starts with a **root window**. Create it with `tk.Tk()`,
then give it a title and a size:

```python
import tkinter as tk

window = tk.Tk()
window.title("My First Window")
window.geometry("400x200")
window.mainloop()
```

* `tk.Tk()` creates the root window.
* `title()` sets the text in the title bar.
* `geometry("400x200")` sets the width and height in pixels.
* `mainloop()` starts the event loop. It doesn't return until the window is
  closed, so put it last.

Run the script to see a 400 by 200 window with the title "My First Window".

---

### The Event Loop

Nothing in the window responds until `mainloop()` runs. Any code placed after
it only runs once you close the window. Keep your setup code before
`mainloop()`, and your reactions to events in functions called from it.

---
