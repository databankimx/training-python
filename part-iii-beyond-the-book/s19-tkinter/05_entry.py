"""Get text from the user with an Entry widget"""

import tkinter as tk


def main() -> None:
    """Ask for a name and show a greeting"""
    window = tk.Tk()
    window.title("Greeting")
    window.geometry("360x160")

    tk.Label(window, text="What is your name?").pack(pady=(16, 4))
    name_entry = tk.Entry(window, width=30)
    name_entry.pack()

    greeting = tk.Label(window, text="", font=("Segoe UI", 12))
    greeting.pack(pady=12)

    def say_hello() -> None:
        """Read the name and show a greeting, ignoring blank entries"""
        name = name_entry.get().strip()
        greeting.config(text=f"Hello, {name}!" if name else "Please enter a name.")

    tk.Button(window, text="Say hello", command=say_hello).pack()

    window.mainloop()


if __name__ == "__main__":
    main()
