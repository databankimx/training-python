## Using `if` with Lists

Redundancy (adding the same code more than once) is not a best practice when
coding. Python lists provide a great way to avoid otherwise clunky, repetitive 
code.

### Mitigating Redundancy

Using a list (with a loop) reduces the need to type redundant conditional 
statements.

```python
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print( f"Adding {requested_topping}.")
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

When working with a list, often you want to perform a different task only if a
value matches something specific.

```python
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print( f"Adding {requested_topping}.")
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

Similarly, there could be a second list of specific values that need to trigger
the alternate behavior.

```python
out_of_stock = ["green peppers", "anchovies"]
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in out_of_stock:
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print( f"Adding {requested_topping}.")
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

When you use `if` with a list as its condition, the condition is `True` if the
list contains at least one element and `False` if it is empty.

This is an important concept in Boolean logic. A number of data types can be
evaluated as Boolean expressions, where specific values are *falsy* (that is,
they will evaluate as `False` in a Boolean condition even though they are not
strictly of the `bool` type).

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

```python
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print( f"Adding {requested_topping}.")
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

Sometimes, you may have multiple optional behaviors, depending on whether an
item appears in one of multiple lists.

```python
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
out_of_stock = ["green peppers", "mushrooms"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        if requested_topping in out_of_stock:
            print(f"Sorry, we're out of {requested_topping}.")
        else:
            print( f"Adding {requested_topping}.")
    else:
        print( f"Sorry, we don't offer {requested_topping}.")
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
