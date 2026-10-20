## Layout with pack()

When you call `pack()` on a widget, tkinter places it against one side of
the space left in the window. Widgets are packed in the order you call
`pack()`:

```python
tk.Label(window, text="Top").pack(side=tk.TOP, fill=tk.X)
tk.Label(window, text="Left").pack(side=tk.LEFT, fill=tk.Y)
```

The main options are:

* `side`: which side of the remaining space to use (`TOP`, `BOTTOM`, `LEFT`,
  or `RIGHT`)
* `fill`: stretch the widget to fill its space (`X`, `Y`, or `BOTH`)
* `expand=True`: take a share of any spare space when the window is resized
* `padx` and `pady`: space around the widget, in pixels

---

### Try It

Run the script and resize the window. The centre label grows, because it's
packed with `expand=True` and `fill=tk.BOTH`. The top and bottom bars stay the
height of their text.

Then change the `side` of one label, and watch how the others move to fit.

---
