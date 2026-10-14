## Detecting and Cleaning Invalid Data

"Bad data" does not have to be empty cells or wrong format. It can just be 
wrong, like if someone registered `199` instead of `1.99`.

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

If you take a look at our the same bad data set we have been using, you can see that in row 7, the duration is 450,but for all the other rows the duration is between 30 and 60.

```
Obtained bad data:
   Duration        Date  Pulse  Maxpulse  Calories
0      60.0  2020/12/01  110.0     130.0     409.1
1      60.0  2020/12/02  117.0     145.0     479.0
2      60.0  2020/12/03  103.0     135.0     340.0
3      45.0  2020/12/04  109.0     175.0     282.4
4      45.0  2020/12/05  117.0     148.0     406.0
5      60.0  2020/12/06  102.0     127.0     300.0
6      60.0  2020/12/07  110.0     136.0     374.0
7     450.0  2020/12/08  104.0     134.0     253.3
8      30.0  2020/12/09  109.0     133.0     195.1
9      60.0  2020/12/10   98.0     124.0     269.0
```

It isn't necessarily wrong, but taking in consideration that this is the 
data set of someone's workout sessions, we can safely assume that this 
person's workout session was probably not seven and a half hours long.

Let's assume that we have already run the following to load the `DataFrame`

```python
import pandas as pd

df = pd.read_csv("./data/bad_data.csv")
```

---

### Removing Invalid Data

Of course, one available strategy is to remove any rows containing bad 
data. here, we'll assume anything greater than 120 minutes is invalid.

```python
df.drop(df[df["Duration"] > 120].index, inplace=True)
print("Dropped invalid durations:")
print(df.head(10))
```

Output:

```
Dropped invalid durations:
    Duration        Date  Pulse  Maxpulse  Calories
0       60.0  2020/12/01  110.0     130.0     409.1
1       60.0  2020/12/02  117.0     145.0     479.0
2       60.0  2020/12/03  103.0     135.0     340.0
3       45.0  2020/12/04  109.0     175.0     282.4
4       45.0  2020/12/05  117.0     148.0     406.0
5       60.0  2020/12/06  102.0     127.0     300.0
6       60.0  2020/12/07  110.0     136.0     374.0
8       30.0  2020/12/09  109.0     133.0     195.1
9       60.0  2020/12/10   98.0     124.0     269.0
10      60.0  2020/12/11  103.0     147.0     329.3
```

We've dropped row 7 in its entirety.

---

### Replacing Bad Data

Depending on the size of the data set, it may be better to replace the
data.

This time, instead of setting a static value, we'll compute the mean and
assume that invalid data is anything more than twice the average duration.

```python
avg_dur = df["Duration"].mean()
max_dur = avg_dur * 2
for i in df.index:
    if df.loc[i, "Duration"] > max_dur:
        df.loc[i, "Duration"] = round(avg_dur)
print("Fixed invalid durations:")
print(df.head(10))
```

Output:

```
Fixed invalid durations:
   Duration        Date  Pulse  Maxpulse  Calories
0      60.0  2020/12/01  110.0     130.0     409.1
1      60.0  2020/12/02  117.0     145.0     479.0
2      60.0  2020/12/03  103.0     135.0     340.0
3      45.0  2020/12/04  109.0     175.0     282.4
4      45.0  2020/12/05  117.0     148.0     406.0
5      60.0  2020/12/06  102.0     127.0     300.0
6      60.0  2020/12/07  110.0     136.0     374.0
7      68.0  2020/12/08  104.0     134.0     253.3
8      30.0  2020/12/09  109.0     133.0     195.1
9      60.0  2020/12/10   98.0     124.0     269.0
```

We could get even cleverer and round to the nearest 15 minute interval, 
but for data analysis, using the mean should be sufficient.

---
