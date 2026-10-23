## "Hello World" with a Variable

### The Zen of Python

[Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)),
the creator of the TimSort algorithm and a significant contributor to the
Python language, wrote a set of 19 guiding principles for writing programs.
They shaped the design of Python, and code that follows them is called
"Pythonic." Tim published them as PEP 20, which is where you'll find them if
you want the official version.

You can read the principles yourself:

In your terminal, run the following command:

```
python
```

That takes you into the Python interpreter. You'll know you're there when you
see the Python prompt: `>>>`

At the Python prompt, run the following command:

```
import this
```

That command displays this:

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

When you're done, return to your normal command prompt by running:

```
exit()
```

---

### Interpreted, Not Compiled

Many languages are compiled into machine language (the CPU instructions for a
particular chip, which nobody reads for fun) before they run.

Python works differently. A separate program, the Python interpreter, reads your
code and carries it out, one line at a time.

> *Note: Python does compile your code to bytecode behind the scenes. You'll
> see that when we create and import our own modules. It's a detail for now, not
> a reason to worry.

Interpreting has an upside. Your code runs until it reaches a line it can't
handle, so you can usually see where things went wrong. The downside is speed:
an interpreter has more work to do while the program runs, so Python can be
slower than some compiled languages. Compiled languages also catch more problems
before the program starts. Python catches syntax errors when it reads the file,
but most other mistakes only show up when the line runs.

---

### Some Code Conventions

#### Comments

Any line or partial line of code starting with `#` followed by a space is a
comment:

```python
# This is a comment
print("I created a comment!") # This is also a comment
```

Python has no syntax for a multi-line comment. You can fake one with a string
that isn't assigned to anything, which Python reads and then throws away:

```python
def my_function():
    """
    This works as a multi-line comment, too.
    Python keeps a string like this as the function's documentation (its docstring).
    """
```

Notice that Python doesn't throw this one away. It saves it as the function's
documentation, so tools and other developers can read it. For a real comment,
though, use `#` on each line.

---

#### Variable Naming

**Rules:**

- May contain letters, numbers, and underscores
- May not start with a number
- May not contain spaces (use an underscore instead)
- Must not be a Python keyword, such as `if` or `for`
- Should not be the name of a built-in function, such as `print`, even though
  Python won't stop you. Python will let you overwrite it, and then `print()`
  stops working for the rest of the program. It's a small mess, and easy to
  avoid.
- Names are case-sensitive, so `message` and `Message` are different variables

**Recommendations:**

- Use descriptive names. `name` is better than `n`, `student_name` is better
  than `s_n`, and `name_length` is better than `length_of_persons_name`. Future
  you will be grateful.
- Avoid `l` and `O`. In some fonts they look like `1` and `0`.
- Stick to lowercase letters, except where a convention calls for capitals (see
  below). Uppercase letters have special meanings in later chapters.
- Use only ASCII characters. Python 3 accepts Unicode names, but PEP 8, the
  official style guide, recommends ASCII, so most Python code sticks to it.

---

**Conventions:**

`snake_case` is used for:
- modules and packages
- variables
- method and function names

`PascalCase` is used for:
- class names
- type variables
- exceptions (also append "Error")

`ALL_CAP_SNAKE_CASE` is used for:
- "constants." Python doesn't have true constants, so this is a convention that
  warns other developers not to change the value

`camelCase` is not used in Python standards.

`kebab-case` is not used in Python standards, and it won't work at all in
Python, because the hyphens look like subtraction.

---

### Data Types

Variables can store data of different types, and different types can do
different things. In Python, even the basic types are classes.

| Category | Data Types |
|-|-|
| Text Type | `str` |
| Numeric Types | `int`, `float`, `complex` |
| Sequence Types | `list`, `tuple`, `range` |
| Mapping Type | `dict` |
| Set Types | `set`, `frozenset` |
| Boolean Type | `bool` |
| Binary Types | `bytes`, `bytearray`, `memoryview` |
| None Type | `NoneType` |

---

### Using a Variable in "Hello World"

Instead of passing the string `"Hello World"` straight to `print()`, we can
store it in a variable first.

A variable is a name for a spot in memory where a value lives. Working with names
is much easier than tracking memory addresses yourself.

> *Note: This is a simplification. There's a lot going on under the covers, and
> eventually you'll want to understand the `stack`, the `heap`, `pointers`,
> `mutability`, and so on. For now, this is accurate enough.

In Python, you create a variable by assigning a value to a name, with
`name = value`. The variable exists from the moment you assign it. There's no
separate declaration step.

```python
# Store the value in a variable
message = "Hello World"

# Print the value from the variable
print(message)
```

Result:

```
Hello World
```

---

### Changing the Value of a Variable

Assign a different value to a variable, and it changes:

```python
message = "Hello World"
print(message)

message = "Goodbye World"
print(message)
```

Result:

```
Hello World
Goodbye World
```

---

### Changing the Type of a Variable

Python is dynamically typed. You can change the type of a variable while the
program runs, which other languages often won't let you do:

```python
message = "Hello "
print(message + message)

message = 10
print(message + message)
```

Result:

```
Hello Hello
20
```

---

### Type Casting

If you want a specific type, you can ask for it with a casting function:

```python
x = str(3)    # x will be '3'
y = int("3")  # y will be 3
z = float(3)  # z will be 3.0

print(x, y, z)
```

Output:

```
3 3 3.0
```

---

### Identifying Type

The `type()` function tells you what type a variable holds:

```python
msg = "Hello"
t = type(msg)
print(t)
```

Output:

```
<class 'str'>
```

---

### Memory References

The `id()` function returns the memory address where a variable is stored. You
won't need it often, but it's handy for debugging:

```python
msg = "Hello"
loc = id(msg)
print(loc)
```

Output (your result will differ):

```
2635577512688
```

---

### Variables and the `NameError`

Spelling and capitalization both matter for variable names. This code causes an
error:

```python
message = "Hello Python Crash Course reader!"
print(mesage)
```

Output:

```
Traceback (most recent call last):
  File "...\hello_world.py", line 2, in <module>
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

---
