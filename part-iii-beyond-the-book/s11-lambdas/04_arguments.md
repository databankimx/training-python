## Lambda Parameters and Arguments

Lambdas support all argument forms:

* positional-only arguments (marked with `/`)
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

### Positional and Keyword Arguments

A lambda can be called with some arguments by position and one by keyword,
just like a regular function:

```python
print((lambda x, y, z: x + y + z)(1, 2, z=3))
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
keyword-only by placing a bare `*` before them. The `*` is a marker, not a
parameter, and the arguments after it can only be passed by keyword:

```python
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
```

Output:

```
6

```

> Note: the code file prints a heading before each result (for example,
> "Positional arguments:"). Those headings are left out of the outputs in this lesson.
> The code file also clears the terminal and pauses between sections, and it turns off
> a Pylint warning (`unnecessary-direct-lambda-call`) on each lambda call. Those
> comments stay in the code file.

---
