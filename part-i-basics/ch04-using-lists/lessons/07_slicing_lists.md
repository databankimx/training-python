## Slicing Lists

Python provides a mechanism, the `slice`, for accessing portions of a list.

The syntax for a slice behaves like a range, encapsulated as indices:

```python
slice = list[[start]:[stop][:step]]
```

All of the fields are optional, but the omission of any item affects how the
slice range behaves.

* If `start` is omitted (`list[:stop]`, e.g), the start is assumed to be 0
* If `stop` is omitted (`list[start:]`, e.g), the stop is assumed to be the
  end of the list.
* If `step` is to be included (`list[start:stop:step]`, e.g.), it will always
  be preceded by a second colon, even if `start`, `end`, or both are omitted
  (`list[::step]`, e.g)

---

### Accessing a Part of a List

You can access a portion (slice) of a list all at the same time

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])
```

Output:

```
['martina', 'michael']
```

---

### Omitting `start`

If you omit an argument, the slice goes all the way to the omitted end of the 
list

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:3])
```

Output:

```
['charles', 'martina', 'michael']
```

---

### Omitting `stop`

If you omit an argument, the slice goes all the way to the omitted end of the 
list

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])
```

Output:

```
['michael', 'florence', 'eli']
```

---

### Including `step`

You can specify the increment (`step`) with a third argument

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::2])
```

Output:

```
['charles', 'michael', 'eli']
```

---

Using a negative increment, you can slice in reverse order from the end

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::-2])
```

Output:

```
['eli', 'michael', 'charles']
```

---

### Looping over Slices

You can loop across a slice (since even a subset of a list is a list)

```python
players = ["charles", "martina", "michael", "florence", "eli"]
for player in players[:3]:
    print(player)
```

Output:

```
charles
martina
michael
```

---

### BONUS - Reversing a String

Even though a string is not technically a list, we can use slicing on a string.

This gives us a really elegant way to reverse a string using the -1 increment.

```python
word = "python"
print(word[::-1])
```

Output:

```
nohtyp
```

---
