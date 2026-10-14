## Creating `ufunc` Functions

Sometimes it's necessary to create your own `ufunc` functions.

To this end, NumPy exposes the `frompyfunc()` function that converts a 
Python function into a `ufunc`.

The syntax is:

```python
import numpy as np

name = np.frompyfunc(function_name, arg_num, out_num)
```

---

### Example: An Adding Function

let's assume that we've defined a function that adds two integers or lists 
of integers:

```python
def add_up(x: int|list[int], y: int|list[int]) -> int:
    """Add two integers or lists of integers"""
    return x + y
```

----

#### Calling the Traditional Function

We can just consume the function as-is, like this:

```python
print("Calling add_up without a ufunc:")
print(f"{add_up.__name__} type: {type(add_up).__name__}")
x, y = 5, 3
print(f"add_up({x}, {y}) yields: {add_up(x, y)}")
lx, ly = [1, 2, 3], [4, 5, 6]
print(f"add_up({lx}, {ly}) yields: {add_up(lx, ly)}\n")
```

Output:

```
Calling add_up without a ufunc:
add_up type: function
add_up(5, 3) yields: 8
add_up([1, 2, 3], [4, 5, 6]) yields: [1, 2, 3, 4, 5, 6]
```

Note: The `type()` function returns `function` as the type for `add_up`

---

#### Creating and Calling a `ufunc`

Or we can convert the function and call it as a `ufunc`

```python
import numpy as np
print("Calling add_up using a ufunc:")
adder = np.frompyfunc(add_up, 2, 1) # Create ufunc
print(f"{adder.__name__} type: {type(adder).__name__}")
x, y = 5, 3
print(f"adder({x}, {y}) yields: {adder(x, y)}")
lx, ly = [1, 2, 3], [4, 5, 6]
print(f"adder({lx}, {ly}) yields: {adder(lx, ly)}\n")
```

Output:

```
Calling add_up using a ufunc:
add_up (vectorized) type: ufunc
adder(5, 3) yields: 8
adder([1, 2, 3], [4, 5, 6]) yields: [5 7 9]
```

Note how for `adder`, the `__name__` attribute is `add_up (vectorized)`
and the type is `ufunc`

Note: When passing arrays or lists, this implements the NumPy `add`
behavior as opposed to concatenating the lists.

---
