"""Create a window"""

import tkinter as tk


def main() -> None:
    """Open a window and wait for the user to close it"""
    window = tk.Tk()
    window.title("My First Window")
    window.geometry("400x200")
    window.mainloop()


if __name__ == "__main__":
    main()
