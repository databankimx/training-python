## Using a Loop to Move or Remove List Items

Often, when you work with a collection of data, you need to move or remove each item as you handle it.

One good strategy for this is a `while` loop.

---

### Moving Items from One List to Another

You can use a `while` loop to move items from one list to another, for as long as items remain in
the first list.

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

Remember that the `remove()` method only removes the first instance of the value you name.

To remove every instance, use a `while` loop that keeps removing items until none of the value
is left in the list:

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

> **Think About It:** Why can't we use the `set()` trick to avoid the loop?
>
> *Answer:* `set()` removes every duplicate, not just the cats, so it would also remove the second
> dog. It also doesn't keep the list's original order, and it returns a new collection rather than
> changing the list in place.

---

