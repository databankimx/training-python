## Slicing Lists

A slice accesses a portion of a list using index notation.

Syntax:

```python
list[start:stop:step]
```

All three fields are optional:

- Omit `start` - slice begins at index 0
- Omit `stop` - slice runs to the end of the list
- Include `step` - always preceded by a second colon, even when `start` or `stop` are omitted

---

### Accessing a Portion of a List

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

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::2])
```

Output:

```
['charles', 'michael', 'eli']
```

Using a negative step slices in reverse:

```python
print(players[::-2])
```

Output:

```
['eli', 'michael', 'charles']
```

---

### Looping over a Slice

A slice is itself a list, so you can loop over it directly:

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

### Bonus - Reversing a String

Strings support slicing too, which gives us an elegant way to reverse one:

```python
word = "python"
print(word[::-1])
```

Output:

```
nohtyp
```

---
