## Modifying List Values

You can change any item in a list in place. Pick the position, and assign a new
value to it. The list stays the same list, with one item swapped out.

```python
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati" # Modify the value in place
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

Notice that the list still has three items. We replaced the first one, and nothing
else moved.

---

### You Can't Assign to a Position That Doesn't Exist

Assigning to a position works only when the position is already there. The list
above has positions `0`, `1`, and `2`. Trying to assign to position `3` doesn't add
a new item. It fails:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[3] = "ducati"
```

Output:

```
Traceback (most recent call last):
  File "...\index_assign.py", line 2, in <module>
    motorcycles[3] = "ducati"
    ~~~~~~~~~~~^^^
IndexError: list assignment index out of range
```

To add an item to the end of a list, you use a different tool. We'll get to it in
the next lesson.

---

### A Quick Word on `len()`

The `.py` file for this lesson uses `len()`, which returns the number of items in a
list. It's handy for checking a list's size, and you'll see it often:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
print(len(motorcycles))
```

Output:

```
3
```

---

