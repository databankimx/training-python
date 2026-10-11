## Check if a List Contains a Value

When working with lists obtained from external data, it is useful to check
whether a certain value appears in the list. Python provides the `in` operator.

---

### Using the `in` Operator

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

### Adding `not`

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

A common pattern: check each value in one list against another.

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
