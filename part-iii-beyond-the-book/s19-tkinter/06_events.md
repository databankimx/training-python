## Responding to Events

tkinter calls your functions when something happens, such as a key press or a
mouse click. These are called **events**, and you connect a function to one
with `bind()`:

```python
window.bind("<Key>", on_key)
window.bind("<Button-1>", on_click)
```

The first argument is the event name in angle brackets. `<Button-1>` is the
left mouse button, and `<Key>` is any key press. The second argument is the
function to call.

---

### The Event Object

tkinter passes an **event** object to your function. Its attributes depend on
the event:

* `event.keysym` is the name of the key pressed, such as `"a"` or `"Return"`.
* `event.x` and `event.y` are the mouse position in the window, in pixels.

```python
def on_key(event: tk.Event) -> None:
    key_label.config(text=f"You pressed: {event.keysym}")
```

---

### Focus

Key events go to the widget that has **focus**. `window.focus_set()` gives
focus to the window, so key presses reach the `<Key>` binding without you
clicking first.

---

### Try It

Run the script and press some keys, including Shift and the arrow keys. Click
in different places and read the coordinates.

---
