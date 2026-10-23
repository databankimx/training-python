## Detecting and Cleaning Invalid Data

"Bad data" does not have to be empty cells or wrong format. It can just be 
wrong, like if someone registered `199` instead of `1.99`.

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

If you take a look at the same bad data set we have been using, you can see that in row 7, the duration is 450, but in the rows shown, all the other durations are between 30 and 60.

```
Obtained bad data:
   Duration          Date  Pulse  Maxpulse  Calories
0        60  '2020/12/01'    110       130     409.1
1        60  '2020/12/02'    117       145     479.0
2        60  '2020/12/03'    103       135     340.0
3        45  '2020/12/04'    109       175     282.4
4        45  '2020/12/05'    117       148     406.0
5        60  '2020/12/06'    102       127     300.0
6        60  '2020/12/07'    110       136     374.0
7       450  '2020/12/08'    104       134     253.3
8        30  '2020/12/09'    109       133     195.1
9        60  '2020/12/10'     98       124     269.0
```

It isn't necessarily wrong, but taking into consideration that this is the 
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
data. Here, we'll assume anything greater than 120 minutes is invalid.

```python
df = df.drop(df[df["Duration"] > 120].index)
print("Dropped invalid durations:")
print(df.head(10))
```

Output:

```
Dropped invalid durations:
   Duration          Date  Pulse  Maxpulse  Calories
0        60  '2020/12/01'    110       130     409.1
1        60  '2020/12/02'    117       145     479.0
2        60  '2020/12/03'    103       135     340.0
3        45  '2020/12/04'    109       175     282.4
4        45  '2020/12/05'    117       148     406.0
5        60  '2020/12/06'    102       127     300.0
6        60  '2020/12/07'    110       136     374.0
8        30  '2020/12/09'    109       133     195.1
9        60  '2020/12/10'     98       124     269.0
10       60  '2020/12/11'    103       147     329.3
```

We've dropped row 7 in its entirety.

---

### Replacing Bad Data

Depending on the size of the data set, it may be better to replace the
data.

This time, instead of setting a static value, we'll compute the mean and
assume that invalid data is anything more than twice the average duration.

Because the previous step removed row 7, we load the data again so that the
bad value is still there to replace.

```python
df = pd.read_csv("./data/bad_data.csv")

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
   Duration          Date  Pulse  Maxpulse  Calories
0        60  '2020/12/01'    110       130     409.1
1        60  '2020/12/02'    117       145     479.0
2        60  '2020/12/03'    103       135     340.0
3        45  '2020/12/04'    109       175     282.4
4        45  '2020/12/05'    117       148     406.0
5        60  '2020/12/06'    102       127     300.0
6        60  '2020/12/07'    110       136     374.0
7        68  '2020/12/08'    104       134     253.3
8        30  '2020/12/09'    109       133     195.1
9        60  '2020/12/10'     98       124     269.0
```

We could get even cleverer and round to the nearest 15 minute interval, 
but for data analysis, using the mean should be sufficient.

---
