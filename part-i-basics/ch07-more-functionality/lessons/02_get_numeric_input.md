## Getting Numeric Input

Getting numeric input from a user has an extra layer of challenge. The Python
`input()` function accepts whatever a user types in, which could include any
UTF-8 characters: letters, numbers, punctuation, or even emojis.

Because of this, user data is always read in as a string. And though Python is
(as we've discussed before) only loosely typed (you can change the data type
held by a variable on the fly, e.g.), values themselves are strongly typed. A
string is a string and an int is an int.

Consider this code that will result in an error:

```python
num = input("Enter a number: ")
print(num > 10)
```

User Prompt:

```
Enter a number: _
```

Let's assume that the user enters a valid number, say `15` + `<ENTER>`

Even with a valid input, we get this output:

```
Traceback (most recent call last):
  File "... SNIP PATH ...\02_get_numeric_input.py", line 5, in <module>
    print(num > 10)
          ^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

This is an error because the input result is always of type `str`, and we 
cannot perform the `>` comparison when the operands are of different types.

---

### The `int()` Function

Python provides a set of functions that are used to cast one data type as
another. We've already used some of these (like `set()` and `list()`). One such
function `int()` casts another type as an integer.

```python
age = input("How old are you?\n> ")
age = int(age)
print(age >= 18)
```

User Prompt:

```
Enter a number: _
```

Let's assume that the user types `15` + `<ENTER>`

Output:

```
False
```

---

### Using `int()` on `input()`

Although it ignores the case where a user enters non-numeric data (don't worry 
— we'll cover that in a later chapter), we can apply the `int()` function
directly to the `input()` rather than storing the string in an intermediate
variable.

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

Let's assume the user types `66` + `<ENTER>`

Output:

```
You're tall enough to ride!
```

---

### The `float()` Function

Python also exposes the `float()` function for when the entered data may not
be an integer (for example, when working with currency).

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

Let's assume the user types either `2.00` or `2` + `<ENTER>`

Output:

```
Your change is $0.25
```

---
