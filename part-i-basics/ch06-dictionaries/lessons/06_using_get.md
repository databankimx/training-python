## Using the `get()` Method

Sometimes you won't know whether a dictionary has a particular key. If you ask for a key that
isn't there, you get an error, and that can stop your program in its tracks.

---

### Retrieval by Key: An Error

When you access a dictionary's value by key, and the key doesn't exist, Python raises a `KeyError`:

```python
alien = {"color" : "green", "speed" : "slow"}
print(alien["points"])
```

Output:

```
Traceback (most recent call last):
  File "...\get_error.py", line 2, in <module>
    print(alien["points"])
          ~~~~~^^^^^^^^^^
KeyError: 'points'
```

---

### Avoiding Errors with `get()`

The `get()` method doesn't raise an error for a missing key. Instead, it returns a default value
that you choose.

Syntax:
`my_dictionary.get(my_key, my_default_value)`

```python
alien = {"color" : "green", "speed" : "slow"}
point_value = alien.get("points", "No point value assigned")
print(point_value)
```

Output:

```
No point value assigned
```

When the key does exist, `get()` returns its value, just like square brackets would:

```python
alien = {"color" : "green", "speed" : "slow"}
print(alien.get("color", "No color assigned"))
```

Output:

```
green
```

`get()` only reads the dictionary. It doesn't add the missing key, so the dictionary is unchanged
after the call.

```python
alien = {"color" : "green", "speed" : "slow"}
alien.get("points", 0)
print(alien)
```

Output:

```
{'color': 'green', 'speed': 'slow'}
```

---

### Omitting the Default Value

If you leave out the default value, `get()` returns `None` for a missing key:

```python
alien = {"color" : "green", "speed" : "slow"}
point_value = alien.get("points")
print(point_value)
```

Output:

```
None
```

---
