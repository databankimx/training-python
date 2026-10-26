## Labels and Buttons

A **label** shows text, and a **button** runs a function when clicked. Both
are widgets, and each one is created with the window as its first argument:

```python
label = tk.Label(window, text="Hello, tkinter!", font=("Segoe UI", 14))
button = tk.Button(window, text="Click me", command=on_click)
```

The widgets don't appear until they're placed in the window. The code below uses
`pack()` for that, which the next lesson covers in detail.

The `command` option is the function to call. Pass the function itself, with
no brackets: `command=on_click`, not `command=on_click()`. The brackets would
run the function straight away.

---

### Changing a Widget

Use `config()` to change a widget's options after it's created:

```python
label.config(text=f"Clicked {clicks} time(s)")
```

The label now shows the new text the next time the window redraws.

---

### Keeping Track of State

The counter lives in a variable inside `main()`. The function `on_click()`
changes it, so it needs `nonlocal` to say that `clicks` belongs to the
enclosing function, not to `on_click`.

Run the script, click the button, and watch the label count the clicks.

---
