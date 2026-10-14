## Lambda Parameters and Arguments

Lambdas support all argument forms:

* positional arguments
* keyword arguments
* arbitrary positional arguments (*args)
* arbitrary keyword arguments (*kwargs)
* keyword-only arguments

---

### Positional Arguments

As we've already seen, we can include a comma separated list of 
positional arguments:

```python
print((lambda x, y, z: x + y + z)(1, 2, 3))
```

Output:

```
6
```

---

### Positional Arguments Including Default Value(s)

Like a traditional function, we can specify default values for positional
arguments:

```python
print((lambda x, y, z=3: x + y + z)(1, 2))
```

Output:

```
6
```

---

### Arbitrary Positional Arguments

We can also include an arbitrary number of positional arguments.

```python
print((lambda *args: sum(args))(1, 2, 3))
```

Output:

```
6
```

---

### Arbitrary Keyword Arguments

We can also include an arbitrary number of keyword arguments.

```python
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
```

Output:

```
6
```

---

### Keyword-Only Arguments

Just like in a regular function, we can specify some arguments as
keyword-only by preceding them with the `*` parameter:

```python
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
```

Output:

```
6
```

---
