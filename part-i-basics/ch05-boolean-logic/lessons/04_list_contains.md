## Check if a List Contains a Value

You will often obtain lists from external data instead of populating them 
yourself.

When working with this type of data, it's useful to be able to check if a
certain value appears in the list.

Python provides the `in` operator to make this easy.

---

### The ~~Bad~~ er... "Other" Way

Using what we already know, we could loop through a list to see if it contains
a desired value, like so:

```python
toppings = ["mushrooms", "onions", "pineapple"]
seek = "anchovies"
found = False
for item in toppings:
    if item == seek:
        found = True
print(found)
```

Output:

```
False
```

---

### Using the `in` Operator

With the `in` operator, however, we can accomplish this in less code and
more readability.

```python
toppings = ["mushrooms", "onions", "pineapple"]
seek = "anchovies"
print(seek in toppings)
```

Output:

```
False
```

---

### Adding the `not` Operator

If we want to check for the opposite condition (the list does not contain 
the value), we can add the `not` operator.

```python
toppings = ["mushrooms", "onions", "pineapple"]
seek = "anchovies"
print(seek not in toppings)
```

Output:

```
True
```

---

### Looping with `in`

A common use case would be the scenario where you have two lists and need 
to check each value in one against the other.

```python
banned_users = ["andrew", "carolina", "david"]
active_users = ["marie", "andrew"]
for user in active_users:
    if user not in banned_users:
        print(f"{user.title()}, you can post a response.")
    else:
        print(f"{user.title()}, you cannot post responses!")
```

Output:

```
Marie, you can post a response.
Andrew, you cannot post responses!
```

---
