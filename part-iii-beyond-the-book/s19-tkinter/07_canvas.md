## Drawing and Animation with Canvas

A **Canvas** is an area you draw on. Shapes are added as items, and each item
is given a number that you can use to move or change it later:

```python
canvas = tk.Canvas(window, width=400, height=200, bg="white")
canvas.pack()

canvas.create_rectangle(20, 20, 120, 70, outline="#264653", width=2)
canvas.create_oval(150, 20, 250, 90, fill="#e9c46a", outline="")
```

Coordinates start at the top left corner, which is `(0, 0)`. Moving down means
the y value gets bigger.

---

### Animating with after()

To animate, change an item a little and then schedule the next change.
`window.after(16, move_ball)` calls `move_ball` in 16 milliseconds, which is
about 60 frames a second:

```python
def move_ball() -> None:
    """Move the ball one step and bounce it off the edges"""
    nonlocal speed
    canvas.move(ball, speed, 0)
    left, _, right, _ = canvas.coords(ball)
    if right >= WIDTH or left <= 0:
        speed = -speed
    window.after(DELAY_MS, move_ball)
```

`canvas.move()` shifts an item by a number of pixels, and `canvas.coords()`
returns its edges. Checking those edges tells the ball when to bounce, by
reversing its speed.

Use `after()` rather than `time.sleep()`. A sleep would freeze the window,
because the event loop can't run while the program is waiting.

---

### Try It

Change `speed` to make the ball faster or slower, and change `DELAY_MS` to
see how the frame rate affects the motion.

---
