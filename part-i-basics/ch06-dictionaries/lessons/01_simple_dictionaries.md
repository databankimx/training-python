## Simple Dictionaries

In Python, a dictionary (in some languages called a hashtable) is a collection 
of key/value pairs instead of just values.

You can think of this as an object with properties but without a defined class.

The syntax is very similar to JavaScript/JSON objects using `key : value` 
throughout.

### Declaring and Accessing a Dictionary

Dictionaries are denoted by curly-braces instead of square-brackets.

Syntax:  
`{key_1: value_1, key_2: value_2, ..., key_n: value_n}`

Keys must be unique within a dictionary

Items are accessed by key rather than index.

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

### Dictionary Ordering

Since Python 3.7, dictionaries maintain insertion order. The order you insert
key-value pairs is the order they iterate.

---

### Dictionary Comprehensions

Of course, like lists, you can create dictionaries using comprehensions

```python
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)
```

Output:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---
