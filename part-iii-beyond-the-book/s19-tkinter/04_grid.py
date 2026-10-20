"""Arrange widgets with grid()"""

import tkinter as tk


def main() -> None:
    """Show a 3 by 3 grid of buttons that stretch with the window"""
    window = tk.Tk()
    window.title("Grid")
    window.geometry("360x300")

    for row in range(3):
        for column in range(3):
            tk.Button(window, text=f"{row}, {column}").grid(
                row=row, column=column, padx=4, pady=4, sticky="nsew")

    for index in range(3):
        window.columnconfigure(index, weight=1)
        window.rowconfigure(index, weight=1)

    window.mainloop()


if __name__ == "__main__":
    main()
