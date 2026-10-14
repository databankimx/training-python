## Array Views and Copies

NumPy provides functions for creating views and copies of arrays.

These functions exist in order to avoid the perplexing complexity of 
creating copy slices from oddly shaped multidimensional arrays.

The difference between the two is that a `copy` creates a clone of the 
array in memory and assigns it to a new variable, while a `view` creates
only a reference to the original variable (similar to the way passing a
mutable variable to a function only passes a reference).

---

### Array Copy

When we use the `array.copy()` method, we're creating an entirely new set
of values in a different memory location.

This means that the variable where the copy is assigned owns the new data,
which is wholly decoupled from the original array.

Let's see this in practice:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print("Create copy and change original:")
print("array:", arr)
print("copy:", x)
```

Output:

```
Create copy and change original:
array: [42  2  3  4  5]
copy: [1 2 3 4 5]
```

Making a change to the original array had no effect on the copy.

---

### Array View

Using the `array.view()` method produces exactly what you would expect.

The new variable has the ability to access the original array, but it does
not own any data, because no new data is created.

This means that modifying one (either the array or view) affects the
other.

#### Modifying the Original Array

Here's an example where we modify the array after creating a view:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print("Create view and change original:")
print("array:", arr)
print("view:", x, "\n")
```

Output:

```
Create view and change original:
array: [42  2  3  4  5]
view: [42  2  3  4  5]
```

As you can see, since they both point to the same object in memory, a
modification affects both.

---

#### Modifying the View

And here's what happens when we modify the view.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print("Create view and change view:")
print("array:", arr)
print("view:", x, "\n")
```

Output:

```
Create view and change view:
array: [31  2  3  4  5]
view: [31  2  3  4  5]
```

---

### The `base` Property

When working with a view, the original array is exposed as `view.base`.

A copy (or even the original array) has a `base` property, but when a 
variable owns the data, the value of `base` is `None`

Let's have a look:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print("Copy versus view `base` property:")
print("array base =", arr.base)
print("copy base =", x.base)
print("view base =", y.base, "\n")
```

Output:

```
Copy versus view `base` property:
array base = None
copy base = None
view base = [1 2 3 4 5]
```

---
