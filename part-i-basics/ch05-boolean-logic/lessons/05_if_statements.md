## Using `if` Statements

### One `if` Condition

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

Output:

```
You are old enough to vote!
Have you registered to vote yet?
```

---

### Handling the `False` Case with `else`

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

Output:

```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

---

### Handling More Conditions with `elif`

`elif` blocks handle the case where the `if` condition is `False` but some
other condition is `True`.

```python
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")
```

Output:

```
Your admission cost is $25
```

---

### Separating the Print Operation

A cleaner pattern stores the result and prints once after all conditions are
evaluated.

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")
```

---

### Multiple `elif` Blocks

```python
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")
```

---

### `else` is Optional

A common pattern uses a default value and omits `else`:

```python
age = 70
price = 20  # default
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}")
```

Output:

```
Your admission cost is $20
```

---

### Checking Independent Conditions

When you need to check another condition regardless of earlier results, use
another `if`, not `elif`. Confusing these is one of the most common errors
for new developers.

```python
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms...")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni...")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese...")
print("Finished making your pizza!")
```

Output:

```
Adding mushrooms...
Adding extra cheese...
Finished making your pizza!
```

---

### Bonus - Using `else` with a Loop

An `else` block can be appended to a loop. It executes when the loop finishes
normally (not via `break`).

```python
for i in range(1, 6):
    print(i)
else:
    print("This ran when I exhausted the range.")
```

Output:

```
1
2
3
4
5
This ran when I exhausted the range.
```

---
