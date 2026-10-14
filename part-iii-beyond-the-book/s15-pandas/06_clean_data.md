## Data Cleaning

Data cleaning means fixing bad data in your data set.

Bad data could be:

* Empty cells
* Data in wrong format
* Wrong data
* Duplicates

Let's look at a small data file that contains bad data
[bad_data.csv](./data/bad_data.csv)

Last 10 rows of bad_data.csv:

```
45,null,100,119,282.0
60,'2020/12/23',130,101,300.0
45,'2020/12/24',105,132,246.0
60,'2020/12/25',102,126,334.5
60,2020/12/26,100,120,250.0
60,'2020/12/27',92,118,241.0
60,'2020/12/28',103,132,null
60,'2020/12/29',100,132,280.0
60,'2020/12/30',102,129,380.3
60,'2020/12/31',92,115,243.0
```

We can see some suspect data in the last 10 rows of the CSV file

---

Example:

```python
import pandas as pd

df = pd.read_csv(./data/bad_data.csv)
print("Obtained bad data:")
print(df.tail(10), "\n")
```

Output:

```
Obtained bad data:
    Duration          Date  Pulse  Maxpulse  Calories
22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60    2020/12/26    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
```

Looking at the last 10 rows of the data, we can see several bad values

* Line 22: No Date (CSV contains `null`)
* Line 26: Missing quotes around Date
* Line 28: Missing Calories (CSV contains `null`)

If we tried to process this data for statistics, our results would be off.

---
