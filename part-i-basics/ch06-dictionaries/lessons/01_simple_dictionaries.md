## Simple Dictionaries

A dictionary, sometimes called a hash table in other languages, is a collection of key/value
pairs instead of a plain list of values.

You can think of a dictionary as an object with properties, but without a class defined
for it. The syntax looks a lot like a JavaScript object or JSON, using `key : value` pairs
throughout.

### Declaring and Accessing a Dictionary

Dictionaries use curly braces instead of square brackets.

Syntax:
`{key_1: value_1, key_2: value_2, ..., key_n: value_n}`

Items are accessed by key rather than by position. Use the key in square brackets:

Syntax:
`my_dictionary[my_key]`

```python
alien = {"color" : "green", "points" : 5}
print(alien["color"])
print(alien["points"])
```

Output:

```
green
5
```

---

### Keys Are Unique

Every key in a dictionary must be unique. If you use the same key twice, the later value
quietly replaces the earlier one. Python doesn't warn you:

```python
alien = {"color": "green", "points": 5, "color": "red"}
print(alien)
```

Output:

```
{'color': 'red', 'points': 5}
```

The first `"color"` is gone. If you need to store two values under one name, a dictionary
isn't the right shape. A list of values under a single key is a better fit.

---

### What Can Be a Key?

Keys have to be a type that Python can't change in place, such as a string, a number, or a
tuple. A list can't be a key, because lists are mutable:

```python
alien = {["color"]: "green"}
```

Output:

```
Traceback (most recent call last):
  File "...\list_key.py", line 1, in <module>
    alien = {["color"]: "green"}
            ^^^^^^^^^^^
TypeError: unhashable type: 'list'
```

Values can be any type, including lists and other dictionaries. Only the keys have this rule.

---

### Looking Up a Key That Doesn't Exist

Asking for a key that isn't there raises a `KeyError`:

```python
alien = {"color": "green", "points": 5}
print(alien["speed"])
```

Output:

```
Traceback (most recent call last):
  File "...\missing_key.py", line 2, in <module>
    print(alien["speed"])
          ~~~~~^^^^^^^^^
KeyError: 'speed'
```

Lesson 6.6 shows `get()`, which returns a default value instead of raising an error. Before
you get there, check that a key exists with `in`.

---

### Checking for a Key with `in`

The `in` operator checks whether a key is in the dictionary:

```python
alien = {"color": "green", "points": 5}
print("color" in alien)
print("speed" in alien)
```

Output:

```
True
False
```

When you use `in` with a dictionary, it looks only at the keys, not the values. So
`"green" in alien` is `False`, even though `"green"` is one of the values.

---

### Dictionary Ordering

Since Python 3.7, dictionaries keep their insertion order. The order you add key-value pairs
is the order they come back when you loop over them.

---

### Dictionary Comprehensions

Like lists, you can build dictionaries with comprehensions:

```python
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)
```

Output:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---
