## Using a Loop to Move/Remove List Items

Often, when working with collections of data, a developer will need to either
move or remove each item out of the collection as it is handled.

One good strategy for handling this is to use a `while` loop

---

### Moving Items from one List to another

We can use a `while` loop to move items from one List to another as long as
items remain in the first list.

```python
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

Output:

```
Verifying user: Alice
Verifying user: Brian
Verifying user: Candace

The following users have been confirmed:
Alice
Brian
Candace
```

---

### Removing Items from a List

Recall that the `remove()` method only removes the first instance of the
specified value from a list.

In order to remove all instances, we can use a `while` loop to continue
removing items until no instances of the value remain in the list.

```python
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")
    
print(pets)
```

Output:

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

> Think About It: Why can't we use the `set()` trick to avoid the loop?

---
