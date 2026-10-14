## Pandas DataFrame

In Pandas, the `DataFrame` is the fundamental data structure. A `DataFrame`
is a row-indexed multi-dimensional table.

You can think of a `DataFrame` as a collection of `Series` objects.

---

### Sample DataFrame

Let's create and view a simple `DataFrame` object. We'll use a dictionary
to provide the non-tabulated data.

We'll use' the `DataFrame()` constructor, which expects a dictionary as 
its input.

```python
import pandas as pd
import json

print("Create a DataFrame:")
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [24, 30, 28, 26],
    "City": ["New York", "Tokyo", "New York", "London"]
}
print(f"Data: {json.dumps(data, indent=4)}")
df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")
```

Output:

```
Create a DataFrame:
Data: {
    "Name": [
        "John",
        "Anna",
        "Peter",
        "Linda"
    ],
    "Age": [
        24,
        30,
        28,
        26
    ],
    "City": [
        "New York",
        "Tokyo",
        "New York",
        "London"
    ]
}
DataFrame:
    Name  Age      City
0   John   24  New York
1   Anna   30     Tokyo
2  Peter   28  New York
3  Linda   26    London
```

Note: For the remaining examples, I will assume that we have already created this DataFrame as variable `df`

---

### Locating a Row in the DataFrame Table

Pandas provides the `loc[]` property to allow us to access a single row of
data from the `DataFrame` table:

```python
import pandas as pd

# -- SNIP --

print("Locate DataFrame Row:")
row = df.loc[0]
print(f"Row 0:\n{row}")
```

Output:

```
Locate DataFrame Row:
Row 0:
Name        John
Age           24
City    New York
Name: 0, dtype: object
```

---

### Locating Multiple Rows in the DataFrame Table

We can locate multiple rows simultaneously by passing a list of indices to
the the `loc[]` indexer.

```python
import pandas as pd

# -- SNIP --

print("Locate Multiple DataFrame Rows:")
rows = df.loc[[0, 2]]
print(f"Rows 0 & 2:\n{rows}")
```

Output:

```
Locate Multiple DataFrame Rows:
Rows 0 & 2:
    Name  Age      City
0   John   24  New York
2  Peter   28  New York
```

---

### Labeling DataFrame Table Rows

We can alter the labels on the table rows using the `index` argument:

```python
import pandas as pd

# -- SNIP --

print("Label DataFrame Rows:")
df = pd.DataFrame(data, index=["1st", "2nd", "3rd", "4th"])
print(df)
```

Output:

```
Label DataFrame Rows:
      Name  Age      City
1st   John   24  New York
2nd   Anna   30     Tokyo
3rd  Peter   28  New York
4th  Linda   26    London
```

---

### Labeling DataFrame Table Columns

When we create the `DataFrame` using a dictionary, the keys are
automatically used as the column labels. We can override this with
specified labels by setting the `columns` attribute with a list of names.

```python
import pandas as pd

# -- SNIP --

print("Label DataFrame Columns:")
df.columns = ["Person", "Years", "Home"]
print(df)
```

Output:

```
Label DataFrame Columns:
  Person  Years      Home
0   John     24  New York
1   Anna     30     Tokyo
2  Peter     28  New York
3  Linda     26    London
```

---
