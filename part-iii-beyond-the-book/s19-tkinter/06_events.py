"""Respond to keyboard and mouse events"""

import tkinter as tk


def main() -> None:
    """Show the last key pressed and the last mouse click"""
    window = tk.Tk()
    window.title("Events")
    window.geometry("420x180")

    key_label = tk.Label(window, text="Press any key", font=("Segoe UI", 12))
    key_label.pack(pady=20)
    click_label = tk.Label(window, text="Click anywhere in this window")
    click_label.pack()

    def on_key(event: tk.Event) -> None:
        """Show the key that was pressed"""
        key_label.config(text=f"You pressed: {event.keysym}")

    def on_click(event: tk.Event) -> None:
        """Show where the mouse was clicked"""
        click_label.config(text=f"Clicked at ({event.x}, {event.y})")

    window.bind("<Key>", on_key)
    window.bind("<Button-1>", on_click)
    window.focus_set()

    window.mainloop()


if __name__ == "__main__":
    main()
