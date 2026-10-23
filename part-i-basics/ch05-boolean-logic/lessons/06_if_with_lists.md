## Using `if` with Lists

Repeating the same code over and over is not a good habit. Python lists give you an easy
way to avoid clunky, repetitive code.

### Mitigating Redundancy

A list and a loop let you handle many items without writing a separate `if` for each one:

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

Often, you want to do something different only when an item matches a specific value.

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

There could be a second list of values that should trigger the alternate behavior. Use `in`
to check membership:

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

### Checking for an Empty List

When you use a list as the condition in an `if`, the condition is `True` if the list has at
least one element, and `False` if it's empty. That's a handy shortcut.

This is an important idea in Boolean logic. Many data types can be used as Boolean
expressions, and some values count as *falsy*. Those values evaluate as `False` in a
condition, even though they aren't of the `bool` type:

|Data Type|Falsy Value|Truthy Values|
|-|-|-|
|`int`|`0`|any non-zero value|
|`float`|`0.0`|any non-zero value|
|`complex`|`0j`|any non-zero value|
|`list`|empty: `[]`|non-empty collection|
|`tuple`|empty: `()`|non-empty collection|
|`dictionary`|empty: `{}`|non-empty collection|
|`set`|empty: `set()`|non-empty collection|
|`string`|empty: `""`|non-empty string|
|`range`|empty: `range(0)`|non-empty range|
|`None`|null: `None`|any non-None value|
|`bool`|`False`|`True`|

Here's the empty-list check in action:

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

Sometimes you have more than one optional behavior, depending on which list an item appears in.
Nested `if` blocks handle that cleanly:

```python
available_toppings = [
    "mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"
]
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
