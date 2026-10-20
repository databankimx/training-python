"""Arrange widgets with pack()"""

import tkinter as tk


def main() -> None:
    """Show five labels arranged with pack()"""
    window = tk.Tk()
    window.title("Pack")
    window.geometry("420x260")

    tk.Label(window, text="Top", bg="#f4a261").pack(side=tk.TOP, fill=tk.X)
    tk.Label(window, text="Left", bg="#2a9d8f").pack(side=tk.LEFT, fill=tk.Y, padx=6, pady=6)
    tk.Label(window, text="Centre (expands)", bg="#e9c46a").pack(side=tk.LEFT, expand=True,
                                                                 fill=tk.BOTH, pady=6)
    tk.Label(window, text="Bottom", bg="#264653", fg="white").pack(side=tk.BOTTOM, fill=tk.X)

    window.mainloop()


if __name__ == "__main__":
    main()
