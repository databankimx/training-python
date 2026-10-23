## Ch 1 - Lesson 1: Run a "Hello World" Program

The simplest (and most ubiquitous) program in most languages is simply to
print a message on the screen.

Commonly, the first program a fledgling developer writes is one that prints
the string "Hello World." Think of it as a smoke test. If this little program
runs, your Python and your editor are at least on speaking terms.

In your code editor, create a file called `hello_world.py` and add the
following code to it:

```python
print("Hello World!")
```

To create the file in VS Code, open a folder for your work, choose
**File > New File**, and save it as `hello_world.py`. The `.py` ending is how
Python knows the file is Python. Editors are clever, but not that clever.

In the code above, `print()` is a function (don't worry too much about that
for now - we'll learn a lot about functions as we forge ahead). Typically,
parentheses in Python indicate that we're calling a function.

### Running it from a terminal

Open a terminal in the folder where you saved the file. In VS Code,
**Terminal > New Terminal** puts you in the right folder already. Type this and
press Enter:

```
python hello_world.py
```

Python reads the file, runs it, and prints the message. Nothing fancy, which is
the point.

When you run the program, your terminal should display:

```
Hello World!
```

---

### The Python prompt

You can also skip the file altogether. Type `python` by itself in the terminal,
and you'll get the `>>>` prompt. That's Python saying, "Go on, I'm listening."
Type a line of code, press Enter, and it runs right away:

```
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```

Don't type the `>>>`. That part is just the prompt, not something you're meant
to enter. The prompt is handy for trying one line at a time, which beats saving
a file every time you want to test a thought. Type `exit()` and press Enter when
you're done.

---

And that's all there is to it. You've written (and executed) your first
program. From now on, you're a Python programmer. *No backsies!*

---
