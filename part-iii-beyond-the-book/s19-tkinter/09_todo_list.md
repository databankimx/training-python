## Putting It Together: A To-Do List

This lesson uses the widgets from the earlier lessons in one small program. It
has three parts:

* An **Entry** for typing a task, with an Add button beside it
* A **Listbox** that shows the tasks
* A button that removes the selected task

---

### Adding a Task

The Add button and the Enter key both call `add_task()`. Pressing Enter in the
entry is one more event binding, the same kind as in the events lesson:

```python
task_entry.bind("<Return>", add_task)
```

`add_task()` ignores blank input, so a stray Enter doesn't add an empty line:

```python
def add_task(event: tk.Event | None = None) -> None:
    text = task_entry.get().strip()
    if text:
        tasks.insert(tk.END, text)
        task_entry.delete(0, tk.END)
```

The Enter binding passes an event to the function, which is why `event` is a
parameter. The Add button doesn't pass one, so the parameter has a default of
`None`.

---

### Removing a Task

`curselection()` returns a tuple with the index of each selected item. An empty
tuple means nothing is selected, so check before deleting:

```python
selection = tasks.curselection()
if selection:
    tasks.delete(selection[0])
```

---

### Layout

The layout uses `grid()` throughout. The window's row and column weights make
the list grow when the window is resized, and the buttons stay the size of
their text.

---

### Try It

Add a few tasks by pressing Enter, then select one and remove it. Try pressing
Add with the box empty, and resize the window to see the list grow.

---
