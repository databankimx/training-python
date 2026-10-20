"""A small to-do list that puts the earlier lessons together"""

import tkinter as tk


def main() -> None:
    """Add items to a list, and remove the selected item"""
    window = tk.Tk()
    window.title("To-Do List")
    window.geometry("360x320")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)

    entry_frame = tk.Frame(window)
    entry_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    entry_frame.columnconfigure(0, weight=1)

    task_entry = tk.Entry(entry_frame)
    task_entry.grid(row=0, column=0, sticky="ew", padx=(0, 6))

    tasks = tk.Listbox(window, font=("Segoe UI", 11))
    tasks.grid(row=1, column=0, sticky="nsew", padx=10)

    def add_task(event: tk.Event | None = None) -> None: # pylint: disable=unused-argument
        """Add the typed text to the list and clear the box"""
        text = task_entry.get().strip()
        if text:
            tasks.insert(tk.END, text)
            task_entry.delete(0, tk.END)

    def remove_task() -> None:
        """Remove the selected task, if one is selected"""
        selection = tasks.curselection()
        if selection:
            tasks.delete(selection[0])

    tk.Button(entry_frame, text="Add", command=add_task).grid(row=0, column=1)
    tk.Button(window, text="Remove selected", command=remove_task).grid(
        row=2, column=0, pady=10)

    task_entry.bind("<Return>", add_task)
    task_entry.focus_set()

    window.mainloop()


if __name__ == "__main__":
    main()
