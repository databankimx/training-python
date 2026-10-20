## Layout with grid()

`grid()` places widgets in rows and columns, like a table. It's often easier
than `pack()` for forms and button panels:

```python
tk.Button(window, text="0, 0").grid(row=0, column=0)
tk.Button(window, text="0, 1").grid(row=0, column=1)
```

* `row` and `column` start at 0.
* `sticky` pulls the widget to the edges of its cell. `"nsew"` means north,
  south, east, and west, so the widget fills the cell.
* `padx` and `pady` add space around each cell.

---

### Letting the Grid Grow

By default, cells keep their size when the window is resized. Give a row or
column a `weight` to let it take a share of the spare space:

```python
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
```

Every column and row in this script has a weight of 1, so the buttons grow
evenly when you resize the window.

---

### Try It

Change one button's `column` to 2 and run it again. That cell already has a
button, so the two overlap. Give every button its own row and column.

---
