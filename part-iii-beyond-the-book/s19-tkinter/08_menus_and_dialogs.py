"""Menus and dialogs"""

import tkinter as tk
from tkinter import messagebox, simpledialog


def main() -> None:
    """Build a menu bar with a dialog and a message box"""
    window = tk.Tk()
    window.title("Menus and Dialogs")
    window.geometry("360x160")

    status = tk.Label(window, text="Choose an option from the File menu", font=("Segoe UI", 11))
    status.pack(expand=True)

    def ask_name() -> None:
        """Ask for a name and show it in the status label"""
        name = simpledialog.askstring("Your name", "What is your name?", parent=window)
        if name:
            status.config(text=f"Nice to meet you, {name}.")

    def show_about() -> None:
        """Show a message box with some information"""
        messagebox.showinfo("About", "A small tkinter demo.", parent=window)

    menubar = tk.Menu(window)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Ask for name...", command=ask_name)
    file_menu.add_command(label="About", command=show_about)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=file_menu)
    window.config(menu=menubar)

    window.mainloop()


if __name__ == "__main__":
    main()
