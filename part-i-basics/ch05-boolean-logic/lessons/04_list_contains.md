## Check if a List Contains a Value

You'll often get lists from external data, rather than typing them yourself. When you do,
it's useful to check whether a particular value appears in the list.

Python provides the `in` operator for exactly that.

---

### The Bad... er, "Other" Way

You could already do this with what you know. Loop through the list, and set a flag when you
find the value:

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

The `in` operator does the same job in less code, and it reads more clearly:

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

To check for the opposite, where the list does *not* contain the value, add `not`:

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

### Two Things to Watch For

`in` checks for whole items in the list, and it's case-sensitive. A capital letter makes a
difference:

```python
toppings = ["mushrooms", "onions", "pineapple"]
print("Mushrooms" in toppings)
print("mushrooms" in toppings)
print("mushrooms".title() in toppings)
```

Output:

```
False
True
False
```

The second line works, and the first doesn't, because `"Mushrooms"` isn't the same string as
`"mushrooms"`. The third line fails for the same reason: `.title()` gives `"Mushrooms"`, which
isn't in the list. If you need a case-insensitive check, lower-case both sides, as we did in
the case lesson.

```python
print("Mushrooms".lower() in toppings)
```

Output:

```
True
```

When the value is a string, `in` can also check for a substring, which is a piece of the
text rather than a whole item. Be careful with this one, because a substring can match where
you didn't mean it to:

```python
print("an" in "banana")
print("an" in ["banana"])
```

Output:

```
True
False
```

The first line finds `"an"` inside `"banana"`. The second looks for `"an"` as a whole item in a
list that has only `"banana"`, so it's `False`.

---

### Looping with `in`

A common case is checking each value in one list against another. Here, we compare a list of
active users with a list of banned users:

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
