## Using the `get()` Method

Sometimes you will not know which of several possible keys have values in a 
dictionary. This can complicate the retrieval of the values.

---

### Retrieval by Key : Error

When accessing elements in a dictionary, if you attempt to retrieve the value
for a key that does not exist, you will receive a KeyError.

```python
alien = {"color" : "green", "speed" : "slow"}
print(alien["points"])
```

Output:

```
Traceback (most recent call last):
  File "... \06_using_get.py", line 7, in <module>
    print(alien["points"])
          ~~~~~^^^^^^^^^^
KeyError: 'points'
```

---

### Avoiding Errors with `get()`

By contrast, the `get()` method does not throw an error for a missing key.
Instead, it returns a specified default value.

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

---

### Omitting the Default Value

If you omit the default value, Python will substitute `None`

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
