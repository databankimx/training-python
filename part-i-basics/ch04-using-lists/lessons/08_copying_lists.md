## Copying Lists

Copying a list is easy to get wrong, because the obvious approach doesn't always do what
you expect. Here's how it works, and the one tool you need.

---

### Assigning a List Doesn't Copy It

If you assign a list to a new variable, both names point to the same list in memory:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods # This assigns a reference, not a copy
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake', 'gyros']
```

Appending to `other_foods` changed `my_foods` too, because both names point to the same
list. A variable doesn't hold the list itself. It holds a reference, which is the address
where the list lives. Copying a whole list takes more memory and more time, so Python
copies the reference instead.

That rule applies to every assignment in Python. A name always points to an object, and
two names can point to the same one. For mutable objects like lists and dictionaries,
that matters, because you can change the object through either name. Immutable objects,
like strings and numbers, can't be changed in place. So assigning one looks like a copy,
but it's the same mechanism underneath.

---

### Taking a Slice Makes a Copy

To get an independent list, take a slice with `[:]`. The unbounded slice makes a new
list:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
print(my_foods)
other_foods = my_foods[:] # The slice makes a new list
other_foods.append("gyros")
print(other_foods)
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
['pizza', 'falafel', 'carrot cake', 'gyros']
['pizza', 'falafel', 'carrot cake']
```

Appending to the copy didn't touch the original.

---

### The `copy()` Method

Lists also have a `copy()` method, which does the same job as `[:]`. It reads more
clearly, so you may prefer it:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
other_foods = my_foods.copy()
other_foods.append("gyros")
print(my_foods)
```

Output:

```
['pizza', 'falafel', 'carrot cake']
```

---

### Comparing Both Approaches Side by Side

Here's the difference in one place. Each list gets a new item, and we print both
versions at each stage:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
```

Output:

```
My favorite foods are:          ['pizza', 'falafel', 'carrot cake']
My friend's favorite foods are: ['pizza', 'falafel', 'carrot cake']
My favorite foods are:          ['pizza', 'falafel', 'carrot cake', 'cannoli']
My friend's favorite foods are: ['pizza', 'falafel', 'carrot cake', 'ice cream']
```

Now compare that with the assignment version, where there's no copy:

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")

print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
```

Output:

```
My favorite foods are:          ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
My friend's favorite foods are: ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```

Both names point to one list, so both prints show the same items. That's the whole
lesson, in two outputs.

---

### Shallow Copies

A slice or `copy()` makes a *shallow* copy. The new list is independent, but any mutable
objects inside it, such as nested lists, are still shared with the original. For a list
of strings or numbers, that doesn't matter. With nested structures, you'd want
`copy.deepcopy()` from the `copy` module, which copies the nested objects too.

---

