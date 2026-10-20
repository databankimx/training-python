## Fully Clean the Data File

For our [bad_data.csv](./data/bad_data.csv) file, we now have the tools to clean the file in its entirety for data analysis.

---

### The Program

The cleaning functions from the previous lessons are collected in the support
module [clean_csv.py](./clean_csv.py). The main function `clean_data_file()`
runs each step in order:

1. `load_from_csv()` - read the file, treating `'` as the quote character
2. `drop_duplicates()` - remove repeated rows
3. `format_dates()` - remove stray quotes and convert `Date` to datetime
4. `add_missing_dates()` - fill missing dates from the previous row
5. `add_missing_calories()` - fill missing calories with the average
6. `fix_invalid_durations()` - replace durations that are too large with the average

---

### Testing with Our Data

We can test the program like this:

```python
from utilities import file_path
from clean_csv import clean_data_file

filepath = file_path("bad_data.csv", "data")
df = clean_data_file(filepath)
print("Cleaned data:")
print(df)
```

Output:

```
Cleaned data:
    Duration       Date  Pulse  Maxpulse  Calories
0       60.0 2020-12-01  110.0     130.0    409.10
1       60.0 2020-12-02  117.0     145.0    479.00
2       60.0 2020-12-03  103.0     135.0    340.00
3       45.0 2020-12-04  109.0     175.0    282.40
4       45.0 2020-12-05  117.0     148.0    406.00
5       60.0 2020-12-06  102.0     127.0    300.00
6       60.0 2020-12-07  110.0     136.0    374.00
7       69.0 2020-12-08  104.0     134.0    253.30
8       30.0 2020-12-09  109.0     133.0    195.10
9       60.0 2020-12-10   98.0     124.0    269.00
10      60.0 2020-12-11  103.0     147.0    329.30
11      60.0 2020-12-12  100.0     120.0    250.70
13      60.0 2020-12-13  106.0     128.0    345.30
14      60.0 2020-12-14  104.0     132.0    379.30
15      60.0 2020-12-15   98.0     123.0    275.00
16      60.0 2020-12-16   98.0     120.0    215.20
17      60.0 2020-12-17  100.0     120.0    300.00
18      45.0 2020-12-18   90.0     112.0    306.54
19      60.0 2020-12-19  103.0     123.0    323.00
20      45.0 2020-12-20   97.0     125.0    243.00
21      60.0 2020-12-21  108.0     131.0    364.20
22      45.0 2020-12-22  100.0     119.0    282.00
23      60.0 2020-12-23  130.0     101.0    300.00
24      45.0 2020-12-24  105.0     132.0    246.00
25      60.0 2020-12-25  102.0     126.0    334.50
26      60.0 2020-12-26  100.0     120.0    250.00
27      60.0 2020-12-27   92.0     118.0    241.00
28      60.0 2020-12-28  103.0     132.0    306.54
29      60.0 2020-12-29  100.0     132.0    280.00
30      60.0 2020-12-30  102.0     129.0    380.30
31      60.0 2020-12-31   92.0     115.0    243.00
```

We have handled:

* Missing Data
* Invalid Data Formatting
* Invalid Data Type
* Invalid Data
* Duplicate Data

Short of reprocessing the data from the source, this is as clean as we can make this data for further analysis.

---
