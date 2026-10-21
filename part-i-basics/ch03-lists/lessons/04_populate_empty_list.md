## Populating an Empty List

Many programs start with an empty list and fill it as they go. The items usually
come from user input or from a loop, and you don't know in advance how many there
will be. So you start with `[]` and add to it.

```python
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
motorcycles.append("triumph")
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
```

Each `append()` adds one item to the end. That's the tool to reach for when you're
adding one item at a time.

---

### Adding Several Items at Once with `extend()`

`extend()` is the other tool for adding to a list. It takes something you can loop
over, such as another list, and adds each of its items to the end of your list:

```python
motorcycles = []
motorcycles.extend(["honda"])
motorcycles.extend(["yamaha"])
motorcycles.extend(["suzuki", "triumph"])
print(motorcycles)
```

Output:

```
['honda', 'yamaha', 'suzuki', 'triumph']
```

The last line adds two items in one call, which is where `extend()` earns its keep.
For a single item, though, `append()` is the more direct choice. Wrapping one item in
a list just to call `extend()` works, but it's roundabout.

---

### Watch Out for Strings

Because `extend()` adds each item from what you give it, a string is a sequence of
characters. Pass it a string without the brackets, and you get one character per
item:

```python
motorcycles = []
motorcycles.extend("honda")
print(motorcycles)
```

Output:

```
['h', 'o', 'n', 'd', 'a']
```

If you meant to add the word `honda`, use `append("honda")`, or wrap it in brackets
as `extend(["honda"])`.

---

