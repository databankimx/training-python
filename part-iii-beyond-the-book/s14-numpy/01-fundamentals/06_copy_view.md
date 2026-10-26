## Array Views and Copies

NumPy provides functions for creating views and copies of arrays.

Some NumPy operations return a view and others return a copy. The difference
matters because a change to one array shows up in a view, but not in a copy.

A `copy` creates a new array with its own data in memory. A `view` is a new
array object that shares the same data in memory as the original array.

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

The new array object shares the original's data, and it does not own any
data of its own, because no new data is created.

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
print("view:", x)
```

Output:

```
Create view and change original:
array: [42  2  3  4  5]
view: [42  2  3  4  5]
```

As you can see, since both share the same data in memory, a modification
affects both.

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
print("view:", x)
```

Output:

```
Create view and change view:
array: [31  2  3  4  5]
view: [31  2  3  4  5]
```

---

### The `base` Property

A view's `base` property is the array whose data it shares. A copy owns its
data, so its `base` is `None`. The original array also has a `base` of `None`,
because it owns its data.

Let's have a look:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print("Copy versus view `base` property:")
print("array base =", arr.base)
print("copy base =", x.base)
print("view base =", y.base)
```

Output:

```
Copy versus view `base` property:
array base = None
copy base = None
view base = [1 2 3 4 5]
```

---
