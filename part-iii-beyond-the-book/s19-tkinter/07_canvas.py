"""Draw on a canvas and animate with after()"""

import tkinter as tk

WIDTH = 400
HEIGHT = 200
DELAY_MS = 16


def main() -> None:
    """Draw some shapes and bounce a ball across the canvas"""
    window = tk.Tk()
    window.title("Canvas")

    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()

    canvas.create_rectangle(20, 20, 120, 70, outline="#264653", width=2)
    canvas.create_oval(150, 20, 250, 90, fill="#e9c46a", outline="")
    canvas.create_line(280, 20, 380, 90, fill="#2a9d8f", width=3)
    canvas.create_text(200, 150, text="Bouncing ball", font=("Segoe UI", 12))

    ball = canvas.create_oval(10, 110, 40, 140, fill="#e76f51", outline="")
    speed = 4

    def move_ball() -> None:
        """Move the ball one step and bounce it off the edges"""
        nonlocal speed
        canvas.move(ball, speed, 0)
        left, _, right, _ = canvas.coords(ball)
        if right >= WIDTH or left <= 0:
            speed = -speed
        window.after(DELAY_MS, move_ball)

    move_ball()
    window.mainloop()


if __name__ == "__main__":
    main()
