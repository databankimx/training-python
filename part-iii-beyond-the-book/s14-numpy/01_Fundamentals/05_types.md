## Data Types

While Python is a loosely-typed language, data types play a significant 
role in NumPy.

---

### Python Data Types

It's worth having a quick review of the data types available in the Python
standard library.

Python provides a limited set of data types:

**Scalar Types**

|Type|Name|Description|
|-|-|-|
|`int`|integer|integer numbers: ..., `-2`, `-1`, `0`, `1`, `2`, ...|
|`float`|floating point|real numbers: `1.5`, `3.14159`, e.g.|
|`bool`|Boolean|Logical values: `True` or `False`|
|`complex`|complex numbers|`1.0 + 2.0j`, e.g.|
|`None`|null|Python's implementation of a defined non-value|

**Sequence Types**

|Type|Name|Description|
|-|-|-|
|`str`|string|collection of characters|
|`list`|linked list|mutable ordered collection of data items|
|`tuple`|tuple|immutable ordered collection of data items|

**Mapping Types**

|Type|Name|Description|
|-|-|-|
|`dict`|dictionary|unordered* collection of key/value pairs|

**Set Types**

|Type|Name|Description|
|-|-|-|
|`set`|set|unordered collection of distinct hashable objects|
|`frozenset`|frozen set|immutable implementation of set|

\* In Python 3.6 and later, dictionaries are ordered collections

---

### NumPy Data Types

NumPy makes a couple of changes to the approach to data types.

* It adds several new data types
* It creates a single-character shorthand for type indicators

**NumPy Types**

|Abbreviation|Type|Description if New|
|-|-|-|
|`i`|`int`|Coupled with bit-size: `i64`, e.g.|
|`b`|`bool`||
|`u`|unsigned `int`|Differs from `int` where all values are signed|
|`f`|`float`|Coupled with bit-size: `f32`, e.g.|
|`c`|`complex`||
|`m`|`timedelta`|Difference between two `datetime` values|
|`M`|`datetime`|Similar to implementation in `datetime` library|
|`O`|`object`|Primary parent to all classes|
|`S`|`str`|Coupled with (max) length|
|`U`|Unicode `str`|Non-ANSI string - Coupled with (max) length|
|`V`|void|Fixed memory chunk for another type|

---

### Identifying Types in NumPy

NumPy's `ndarray` type exposes a property `dtype` that identifies the
data type stored in the array.

Let's take a look at a few examples:

---

#### Integer Array

For an integer array initialized without specifying the data type, the
default type will be `int64` (64-bit integer).

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr, "type =", arr.dtype)
```

Output:

```
[1 2 3 4] type = int64 
```

---

#### String Array

For a string array initialized without specifying the data type, the
default type will be `Un` (where `n` is the largest string's byte size).

```python
import numpy as np

arr = np.array(["apple", "banana", "cherry"])
print(arr, "type =", arr.dtype)
```

Output:

```
['apple' 'banana' 'cherry'] type = <U6
```

---

#### Explicit Array Types

**integer**

For an array initialized with integers, we can specify the data type.

The syntax for specifying type uses the `dtype` keyword argument with
a string containing the data type abbreviation and (optionally) the
number of bytes to allocate per value.

For example, with these values, a single byte (int8) is sufficient. There
is no reason to use 8-byte integers, like the default did.

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="i1")
print(arr, "type =", arr.dtype)
```

Output:

```
[1 2 3 4] type = int8
```

---

**float**

Even when we initialize an array with integer values, we can include the
`dtype` keyword argument to convert the data type to a float 

```python
import numpy as np

arr = np.array(["apple", "banana", "cherry"], dtype="f")
print(arr, "type =", arr.dtype)
```

Output:

```
[1. 2. 3. 4.] type = float32
```

---

#### Conversion Errors

If any value(s) in the array cannot be converted to the explicit type,
NumPy will raise a ValueError.

```python
import numpy as np

arr = np.array(["a", "2", "3"], dtype="i")
print(arr, "type =", arr.dtype, "\n")
```

Output:

```
Traceback (most recent call last):
  File "...\05_types.py", line 52, in <module>
    main()
  File "...\05_types.py", line 43, in main
    arr = np.array(["a", "2", "3"], dtype="i")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'a'
```

---

### Changing Data Type

The NumPy `astype()` method returns a copy of the array with its values
converted to a specified type

Here, we'll state with a `float64` array and:

* Obtain an array with its values converted to `int8`
* Obtain a second array with the values converted to `int64`
* Obtain a third array with the second array's values converted to `bool`

Note: We can use the NumPy abbreviations (like `"i32"`) Python type names 
(like `bool`), or NumPy type names (like `np.int16`) for the type 
argument.

```python
import numpy as np

arr = np.array([0.1, 2.1, 3.1])
print("Original:", arr, "type =", arr.dtype, "\n")

new_arr = arr.astype("i1")
print("New ('i1'):", new_arr, "type =", new_arr.dtype)

new_arr = arr.astype(int)
print("New (int):", new_arr, "type =", new_arr.dtype)

new_arr = arr.astype(np.int16)
print("New (np.int16):", new_arr, "type =", new_arr.dtype)

new_arr = new_arr.astype(bool)
print("New from new (bool):", new_arr, "type =", new_arr.dtype)

print("\nOriginal:", arr, "type =", arr.dtype, "\n")
```

Output:

```
Original: [0.1 2.1 3.1] type = float64 

New ('i1'): [0 2 3] type = int8
New (int): [0 2 3] type = int64
New (np.int16): [0 2 3] type = int16
New from new (bool): [False  True  True] type = bool

Original: [0.1 2.1 3.1] type = float64
```

Note: After creating the re-typed array copies, the original array is 
unchanged.

---
