## Using `if` with Lists

### Mitigating Redundancy

A list with a loop avoids repetitive conditional statements.

```python
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
```

Output:

```
Adding mushrooms.
Adding green peppers.
Adding extra cheese.
Finished making your pizza!
```

---

### Comparing Against Specific Values

```python
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
```

Output:

```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza!
```

---

### Comparing Against a List of Specific Values

```python
out_of_stock = ["green peppers", "anchovies"]
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in out_of_stock:
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")
```

Output:

```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza!
```

---

### Comparing an Empty List

When an `if` statement uses a list as its condition, it evaluates to `True`
if the list is non-empty and `False` if it is empty. This is the *falsy*
concept - several data types have specific values that evaluate as `False`
in a Boolean context.

| Data Type | Falsy Value | Truthy Values |
|-|-|-|
| `int` | `0` | any non-zero value |
| `float` | `0.0` | any non-zero value |
| `list` | `[]` | non-empty collection |
| `tuple` | `()` | non-empty collection |
| `dict` | `{}` | non-empty collection |
| `set` | `set()` | non-empty collection |
| `str` | `""` | non-empty string |
| `range` | `range(0)` | non-empty range |
| `None` | `None` | any non-None value |
| `bool` | `False` | `True` |

```python
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("Finished your plain pizza.")
```

Output:

```
Finished your plain pizza.
```

---

### Comparing Against Multiple Lists

```python
available_toppings = ["mushrooms", "olives", "green peppers",
                      "pepperoni", "pineapple", "extra cheese"]
out_of_stock = ["green peppers", "mushrooms"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        if requested_topping in out_of_stock:
            print(f"Sorry, we're out of {requested_topping}.")
        else:
            print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't offer {requested_topping}.")
print("Finished making your pizza!")
```

Output:

```
Sorry, we're out of mushrooms.
Sorry, we don't offer french fries.
Adding extra cheese.
Finished making your pizza!
```

---
