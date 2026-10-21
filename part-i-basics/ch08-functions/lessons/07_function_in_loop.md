## Executing a Function in a Loop

Another common use case is running the same operation on each item in a group or sequence.

For this kind of task, it helps to put the operation in a separate function, and call that function
inside the loop, rather than nesting the operation's code in the loop.

---

### Calling a Function in a `for` Loop

When you repeat an operation over a sequence or a collection, a `for` loop is the natural choice.

Here, we create a simple function that squares a number, and call it for each value in a range:

```python
def square(n):
    """Return the square of the integer passed"""
    return n ** 2

for num in range(1, 6):
    print(f"{num}² = {square(num)}")
```

Output:

```
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
```

---

### Calling a Function in a `while` Loop

When the sequence has no fixed end, or you want to keep going until some condition is met, you can
use the same idea with a `while` loop. Move the repeated work into a function, and call it from the
loop.

The `get_formatted_name()` function below is the same one from the previous lesson:

```python
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

Output (the `...` stands for the rest of the conversation, which is left out):

```
Please tell me your name:
(enter 'q' at any time to quit)
First name: John
Last name: Smith

Hello, John Smith!

Please tell me your name:
(enter 'q' at any time to quit)
First name: Mary
Last name: Doe

Hello, Mary Doe!

...

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

---

