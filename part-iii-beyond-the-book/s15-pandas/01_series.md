## Pandas Data Series

In Pandas, the `Series` is the smallest data component on which we can 
perform analysis.

The easiest way to think of a series is as a single ***column*** of data. 
The `Series` can contain any number of *rows*.

---

### Creating a Series from a List

Since a series can contain multiple rows, we can create one using a list
as the input data.

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
print("Create a Series from a list:")
print(f"List: {data}")
series = pd.Series(data)
print(f"Series:\n{series}")
```

Output:

```
Create a Series from a list:
List: [1, 2, 3, 4, 5]
Series:
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

---

### Accessing Series Data

We can read from a series by index, just like a list:

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("View the indices of a Series:")
for i in range(len(series)):
    print(f"series[{i}] = {series[i]}")
```

Output:

```
View the indices of a Series:
series[0] = 1
series[1] = 2
series[2] = 3
series[3] = 4
series[4] = 5
```

---

### Labeling Series Data

We can provide labels for the data in the series by passing a list of
names into the `index` keyword parameter.

> Note!  
> The list of names must be the same length as the data list.

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
names = ["a", "b", "c", "d", "e"]
series = pd.Series(data, index=names)
print("View the values of a Series with named indices:")
for name in names:
    print(f"series[{name}] = {series[name]}")
```

Output:

```
View the values of a Series with named indices:
series[a] = 1
series[b] = 2
series[c] = 3
series[d] = 4
series[e] = 5
```

---

### Creating a Series from a Dictionary

When we load from a dictionary instead of a list, the keys are 
automatically assigned as the indices.

```python
import pandas as pd

print("Create a Series from a dictionary:")
data = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5 }
print(f"Dictionary: {data}")
series = pd.Series(data)
print(f"Series:\n{series}")
```

Output:

```
Create a Series from a dictionary:
Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
Series:
a    1
b    2
c    3
d    4
e    5
dtype: int64
```

---

### Create Series with Filter

We can filter which keys are included in the series by also passing an
array of indices matching some or all of the keys.

```python
import pandas as pd

print("Create a filtered Series from a dictionary:")
data = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5 }
print(f"Dictionary: {data}")
filter = ["a", "c", "e"]
print(f"Filter: {filter}")
series = pd.Series(data, index=filter)
print(f"Series:\n{series}")
```

Output:

```
Create a filtered Series from a dictionary:
Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
Filter: ['a', 'c', 'e']
Series:
a    1
c    3
e    5
dtype: int64
```

---
