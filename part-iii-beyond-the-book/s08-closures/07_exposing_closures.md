## Exposing Closures

Normally, the captured variables in a closure are completely hidden from the 
calling code.

However, you can provide getter and setter inner functions for these
variables, extending the utility of the closure.

---

### Closure Without Accessors

First, let's create a closure like we've done thus far:

```python
def make_point(x: int, y: int) -> callable:
    """Generates a point with access to its coordinate values"""
    def point():
        """Defines a point"""
        print(f"Point({x}, {y})")
    return point
```

As you can see, the closure will capture `x` and `y` from the outer function.

```python
point = make_point(1, 2)
point()
```

Output:

```
Point(1, 2)
```

---

### Attempting to Modify Without Accessors

If we want to modify `x` or `y` though, we can't. Even though they are
captured by the closure, we can't access them from the calling code:

```python
point = make_point(1, 2)
point.x = 5
point()
print(point.x)
```

Output:

```
Point(1, 2)
```

The attempt to change the value of `x` did not change the captured value.

---

### Adding Getters and Setters

We can add accessors to expose the `x` and `y` variables to the calling code.

---

#### Adding Getters

To create getters for the `x` and `y` variables, we need to add additional
inner functions.

```python
# -- SNIP --

    def get_x() -> int:
        """Getter function for x"""
        return x
    
    def get_y() -> int:
        """Getter function for y"""
        return y
```

And then we need to assign them to the closure itself.

```python
# -- SNIP --

    point.get_x = get_x
    point.get_y = get_y
```

---

#### Using Getters

Now, in the calling code, we can access the values of `x` and `y` thus:

```python
point = make_point(1, 2)
point()
print(f"x = {point.get_x()}")
print(f"y = {point.get_y()}")
```

Output:

```
Point(1, 2)
x = 1
y = 2
```

---

#### Adding Setters

We'll create additional inner functions as setters for `x` and `y`

```python
# -- SNIP --

    def set_x(val: int) -> None:
        """Setter function for x"""
        nonlocal x
        x = val
        
    def set_y(val: int) -> None:
        """Setter function for y"""
        nonlocal y
        y = val
```

And of course, we'll add them to the closure

```python
# -- SNIP --

    point.set_x = set_x
    point.set_y = set_y
```

---

#### Using Setters

And now we can modify as well as read `x` and `y` in our calling code:

```python
point = make_point(1, 2)
point()
print(f"x = {point.get_x()}")
print(f"y = {point.get_y()}\n")
point.set_x(42)
point.set_y(7)
point()
print(f"x = {point.get_x()}")
print(f"y = {point.get_y()}")
```

Output:

```
Point(1, 2)
x = 1
y = 2

Point(42, 7)
x = 42
y = 7
```

---
