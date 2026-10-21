## Getting Numeric Input

Getting numeric input from a user comes with an extra wrinkle. Python's `input()` function accepts
whatever the user types, which can include any UTF-8 characters: letters, numbers, punctuation, or
even emojis.

Because of that, user data always comes back as a string. Python is loosely typed, which means you
can change the type of data a variable holds whenever you like. The values themselves are still
strongly typed, though. A string is a string, and an integer is an integer.

Consider this code, which causes an error:

```python
num = input("Enter a number: ")
print(num > 10)
```

User Prompt:

```
Enter a number: _
```

Let's assume the user enters a valid number, such as `15` + `<ENTER>`.

Even with a valid input, we get this output:

```
Traceback (most recent call last):
  File "... SNIP PATH ...\02_get_numeric_input.py", line 5, in <module>
    print(num > 10)
          ^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

The input is always a `str`, and Python won't compare a string with an integer using `>`. The two
types don't match, so the comparison fails.

---

### The `int()` Function

Python provides a set of functions for converting one type into another. We've already used a few of
them, like `set()` and `list()`. The `int()` function converts a value into an integer:

```python
age = input("How old are you?\n> ")
age = int(age)
print(age >= 18)
```

User Prompt:

```
How old are you?
> _
```

Let's assume the user types `15` + `<ENTER>`.

Output:

```
False
```

> **What can `int()` convert?**
> 
> `int()` accepts a string holding a whole number, and it raises a `ValueError` for a string with a
> decimal point, such as `"3.5"`. For decimal input, use `float()` instead.
> 
> Technically, `int()` can accept other types:
> * Strings holding a whole number, with an optional sign and surrounding spaces, such as `" -7 "`.
>   Underscores are allowed too, so `"1_000"` works.
> * Floats, which are truncated toward zero. `int(3.9)` is `3`, and `int(-3.9)` is `-3`.
> * Booleans. `int(True)` is `1`, and `int(False)` is `0`.
> * Any object that defines an `__int__` method. Custom types use this to support `int()`.

---

### Using `int()` on `input()`

You don't need the intermediate variable. You can call `int()` directly on the result of `input()`:

```python
height = int(input("How tall are you in inches?\n> "))
if height >= 48:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older...")
```

User Prompt:

```
How tall are you in inches?
> _
```

Let's assume the user types `66` + `<ENTER>`.

Output:

```
You're tall enough to ride!
```

> Note: this code doesn't check for non-numeric input. If the user types `tall`, `int()` raises an
> error and the program stops. We'll handle that in a later chapter.

---

### The `float()` Function

Use the `float()` function when the value might not be a whole number, such as when you're working
with money:

```python
price = 1.75
paid = float(input("\nEnter the amount paid:\n> "))
if paid > price:
    print(f"Your change is ${(paid - price):.2f}")
elif paid < price:
    print(f"You still owe ${(price - paid):.2f}")
else:
    print("Thank you.")
```

User Prompt:

```
Enter the amount paid:
> _
```

Let's assume the user types either `2.00` or `2` + `<ENTER>`.

Output:

```
Your change is $0.25
```

---

