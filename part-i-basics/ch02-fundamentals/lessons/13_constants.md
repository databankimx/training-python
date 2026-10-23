## A Word on Constants

Some values should never change while your program runs. Think of the number of
days in a week, or the value of pi. A variable that never changes is a bit of a
contradiction, but the idea is called a *constant*, and programmers use constants
all the time.

### Python Doesn't Have Constants

Python has no way to make a variable constant. You can't lock a name so that
nothing can reassign it.

Some data types are *immutable*, meaning you can't change the value they hold.
Strings and numbers are examples. But immutability is a property of the value, not
the variable. The name can still be pointed at something else entirely.

### Indicating the Intent to Be Constant

Since Python won't stop anyone from changing a variable, we tell other developers
our intent with the name. A value that shouldn't change gets written in
`ALL_CAPS_SNAKE_CASE`, and the capitals say "please leave this alone."

Here's an example. We define a constant for *π* and use it to find the area of a
circle, first with a radius of 2, then with a radius of 3. Since we never want
*π* to change, we name it `PI`, not `pi`:

```python
PI = 3.14159

r = 2
print(f"A circle with radius {r} has an area of {PI * r ** 2}")

r = 3
print(f"A circle with radius {r} has an area of {PI * r ** 2}")
```

Output:

```
A circle with radius 2 has an area of 12.56636
A circle with radius 3 has an area of 28.27431
```

Notice that `r` changes, and that's fine. `r` is a normal variable. `PI` is the
one that stays put.

---

> **Want a little more help?** Since Python 3.8, you can use `Final` from the
> `typing` module to mark a name as "don't reassign." Nothing stops the program
> from running. But a type checker such as `mypy` will flag any reassignment
> before you run the code. It's still a convention enforced by tools, not by the
> language itself.

---
