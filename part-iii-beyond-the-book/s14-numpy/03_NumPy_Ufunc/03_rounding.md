## Rounding Decimals

As you probably recall, there are a number of different strategies for 
[rounding](../../../Part%20I%20-%20Basics/Ch08_Functions/Lessons/14_bonus_how_to_round.md).

NumPy implements functions for several of these:

* Truncate
* Fix
* Around
* Floor
* Ceiling

All of these perform rounding element-wise across the array.

---

### Truncate

The `trunc()` function removes the decimal part of the number but performs 
no other rounding operations.

This implements the *truncate* strategy.

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Truncate: {np.trunc(arr)}")
```

Output:

```
Array:    [-3.1666  3.6667]
Truncate: [-3.  3.]
```

---

### Fix

The `fix()` function rounds values to the nearest integer toward zero.

This implements the *floor towards zero* strategy.

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Fix:      {np.fix(arr)}")
```

Output:

```
Array:    [-3.1666  3.6667]
Fix:      [-3.  3.]
```

---

### Around

The `around()` and `round()` functions round values to the specified number of decimal places.

This implements the *banker's rounding* strategy.

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Around:   {np.around(arr, 2)}")
print(f"Round:    {np.around(arr, 2)}")
```

Output:

```
Array:    [-3.1666  3.6667]
Around:   [-3.17  3.67]
Round:    [-3.17  3.67]
```

. . . . . . . . . .

Note: Like the `round()` function in the Python Standard Library, this 
function uses the *banker's rounding* strategy, which means that when the
decimal to be rounded is exactly .5, the number is rounded toward the 
nearest even integer.

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Around:   {np.around(arr)}")
print(f"Round:    {np.around(arr)}")
```

Output:

```
Halves:   [2.5 3.5]
Around:   [2. 4.]
Round:    [2. 4.]
```

This is done to minimize rounding error as data size increases, but you
should be aware and understand this behavior if you will be working with
the raw, rounded data as opposed to statistical computations.

---

### Floor

The `floor()` function returns the floor computation element-wise.

This implements the *floor towards least* strategy.

> Note: As opposed to `fix()`, the `floor()` function does not compute 
> towards zero but instead toward the lowest value, so:
>
> `fix(-2.5)` returns `-2`
> but
> `floor(-2.5)` returns `-3`

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Floor:    {np.floor(arr)}")
```

Output:

```
Array:    [-3.1666  3.6667]
Floor:    [-4.  3.]
```

---

### Ceiling

The `ceil()` function returns the ceiling computation element-wise.

This implements the *ceiling towards greatest* strategy.

```python
import numpy as np

arr = np.array([-3.1666, 3.6667])
print(f"Array:    {arr}")
print(f"Ceil:     {np.ceil(arr)}")
```

Output:

```
Array:    [-3.1666  3.6667]
Ceil:     [-3.  4.]
```

---
