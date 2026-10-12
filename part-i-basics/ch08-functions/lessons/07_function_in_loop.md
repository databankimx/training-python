## Executing a Function in a Loop

Another common use case is performing a repetitive operation on each item in a 
group or sequence.

For this type of solution, it's useful to place the operation(s) in a separate
function and call the function in the loop instead of nesting the operational
code.

---

### Calling a function in a `for` Loop

When performing a repetitive operation on a sequence or across a collection,
the logical choice is to use a `for` loop.

Here, we create a simple function to square a number and call it for each
value in a range:

```python
def square(n):
    """Return the square of the integer passed"""
    return n ** 2

for n in range(1, 6):
    print(f"{n}² = {square(n)}")
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

### Calling a function in a `while` Loop

For an unbounded sequence or when acting until some condition is met, the same
principle of moving the repeated actions into a function can be used with calls
from a `while` loop.

```python
def get_formatted_name(first_name, last_name, middle_name = ""):
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

Output:

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
