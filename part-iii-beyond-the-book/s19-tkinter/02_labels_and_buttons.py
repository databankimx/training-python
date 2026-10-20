"""Labels and buttons"""

import tkinter as tk


def main() -> None:
    """Show a label that counts clicks on a button"""
    window = tk.Tk()
    window.title("Labels and Buttons")

    label = tk.Label(window, text="Hello, tkinter!", font=("Segoe UI", 14))
    label.pack(pady=20)

    clicks = 0

    def on_click() -> None:
        """Count a click and update the label"""
        nonlocal clicks
        clicks += 1
        label.config(text=f"Clicked {clicks} time(s)")

    button = tk.Button(window, text="Click me", command=on_click)
    button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
