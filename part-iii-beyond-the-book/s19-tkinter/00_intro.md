## Introduction to tkinter

Python includes a GUI toolkit called **tkinter**. It's part of the standard
library, so there's usually nothing extra to install (some Linux distributions
ship it as a separate package), and it runs on Windows, macOS, and Linux.

A tkinter program is a window that waits for things to happen. You create
the window and its widgets (buttons, labels, text boxes, and so on), and then
you hand control to the **event loop**. The loop watches for clicks, key
presses, and timers, and calls the functions you attached to them.

Each lesson in this chapter adds one idea to a small program:

* Creating a window
* Labels and buttons
* Arranging widgets with `pack()` and `grid()`
* Getting text from the user
* Responding to events
* Drawing and animation on a canvas
* Menus and dialogs
* Putting it all together in a to-do list

---

### Running the Lessons

Each lesson opens a window. Close the window to end the program, or press
Escape in this runner to stop it.

Because the window waits for your input, the output pane may stay empty
while a lesson is running. That's expected.

---
