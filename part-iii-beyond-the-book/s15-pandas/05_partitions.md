## Pandas Data Partitioning

Often, we want to work with a sample set of the data as opposed to all of 
it. Understanding the size of the overall data and being able to partition
out data selections is important functionality.

For all examples below, we will assume that we have already loaded a
`DataFrame` named `df` with the same data we loaded in the CSV and JSON
lessons.

---

### DataFrame Info

Pandas exposes a the `info()` method to return metadata about the
`DataFrame`:

```python
import pandas as pd

# -- SNIP --

print(f"DataFrame Info:")
print(df.info())
```

Output:

```
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
Index: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 6.6 KB
None
```

---

### Partitioning the DataFrame Head

The `head()` method returns a `DataFrame` containing the first rows in the
existing `DataFrame`.

. . . . . . . . . .

#### Default (5 Rows)

By default, the `head()` method returns the first five rows

```python
import pandas as pd

# -- SNIP --

print(f"Top 5 Rows:")
print(df.head())
```

Output:

```
Top 5 rows:
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
```

. . . . . . . . . .

#### Top *n* Rows

We can pass an optional integer argument for the number of rows desired.

```python
import pandas as pd

# -- SNIP --

print(f"Top 10 Rows:")
print(df.head(10))
```

Output:

```
Top 10 rows:
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.5
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
```

---

### Partitioning the DataFrame Tail

The `tail()` method returns a `DataFrame` containing the last rows in the
existing `DataFrame`.

. . . . . . . . . .

#### Default (5 Rows)

By default, the `tail()` method returns the first five rows

```python
import pandas as pd

# -- SNIP --

print(f"Bottom 5 Rows:")
print(df.tail())
```

Output:

```
Bottom 5 rows:
     Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

. . . . . . . . . .

#### Bottom *n* Rows

We can pass an optional integer argument for the number of rows desired.

```python
import pandas as pd

# -- SNIP --

print(f"Bottom 10 Rows:")
print(df.tail(10))
```

Output:

```
Bottom 10 rows:
     Duration  Pulse  Maxpulse  Calories
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.4
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
```

---
