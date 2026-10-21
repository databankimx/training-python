## Slicing Lists

Sometimes you want a portion of a list, not the whole thing. Python calls that a *slice*.
You describe the part you want with a start, a stop, and an optional step, all inside
the square brackets.

The general form is:

```python
my_list[start:stop:step]
```

Each part is optional, and leaving one out changes how the slice behaves:

* If you leave out `start`, the slice begins at position 0, the front of the list.
  For example, `my_list[:stop]`.
* If you leave out `stop`, the slice runs to the end of the list. For example,
  `my_list[start:]`.
* If you want a `step`, you need the second colon, even when you leave out `start`
  and `stop`. For example, `my_list[::step]`.

The `stop` position works the same way it does in `range()`. It's the first position
you *don't* get.

---

### Accessing a Part of a List

You can grab a portion of a list in one step:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])
```

Output:

```
['martina', 'michael']
```

Position 1 is included, and position 3 isn't.

---

### Omitting `start`

Leave out `start`, and the slice begins at the front of the list:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:3])
print(players[:4])
```

Output:

```
['charles', 'martina', 'michael']
['charles', 'martina', 'michael', 'florence']
```

---

### Omitting `stop`

Leave out `stop`, and the slice runs to the end of the list:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])
print(players[-3:])
```

Output:

```
['michael', 'florence', 'eli']
['michael', 'florence', 'eli']
```

Both lines give the same result. The last three players start at position 2, and so does
`-3`, counting from the end.

---

### Including `step`

Use a third value to set the increment:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::2])
```

Output:

```
['charles', 'michael', 'eli']
```

A negative step slices in reverse, starting from the end:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::-2])
```

Output:

```
['eli', 'michael', 'charles']
```

---

### A Slice Makes a Copy

A slice gives you a new list. The original is untouched, so changing the slice doesn't
change the list it came from:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
first_three = players[:3]
first_three.append("tim")
print(first_three)
print(players)
```

Output:

```
['charles', 'martina', 'michael', 'tim']
['charles', 'martina', 'michael', 'florence', 'eli']
```

We'll look at copying lists more closely in the next lesson.

---

### Slicing Past the End Doesn't Raise an Error

Lesson 3.2 showed that a position past the end of a list raises an `IndexError`. A slice
handles that differently. It takes whatever part of the list exists, and it quietly stops:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[3:99])
```

Output:

```
['florence', 'eli']
```

---

### Looping over Slices

A slice is a list, so you can loop over it like any other:

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first 3 players on my team")
for player in players[:3]:
    print(player)
```

Output:

```
Here are the first 3 players on my team
charles
martina
michael
```

---

### Bonus: Reversing a String

A string isn't a list, but it's a sequence of characters, and slicing works on it too.
A step of `-1` gives you a reversed copy of the string, which is about as elegant as
Python gets:

```python
name = "Scott"
print(name[::-1])
```

Output:

```
ttocS
```

---

