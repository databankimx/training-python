## List Statistics

Python provides several functions to expose information about a list.


|Function|Effect|
|-|-|
|`len(list)`|Returns the number of elements in the list|
|`min(list)`|Returns the lowest value in the list|
|`max(list)`|Returns the highest value in the list|
|`sum(list)`|Returns the sum of the values in the list|

```python
digits = list(range(10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
```

Output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
List Length:  10
Minimum:      0
Maximum:      9
Sum:          45
```

---

Of course, we can take those values and calculate the other information, like a
mean average.

```python
digits = list(range(10))
print(digits)
print(f"Average:      {sum(digits) / len(digits)}")
```

Output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Average:      4.5
```

---

Because calculating the average uses division, the result is a float, even if
the value is an integer.

```python
tens = list(range(10, 101, 10))
print(tens)
print(f"Average:      {sum(tens) / len(tens)}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55.0
```

---

We can work around this in one of two ways:

We can import the `statistics` module and use its `mean()` function

```python
import statistics

tens = list(range(10, 101, 10))
print(tens)
print(f"Average:      {statistics.mean(tens)}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55
```

---

Or we can leverage modulo arithmetic and a conditional (coming in chapters 
5 and 8) to eliminate the float when it is not needed.

```python
tens = list(range(10, 101, 10))
print(tens)
avg = sum(tens) / len(tens)
mean = int(avg) if (avg * 10) % 10 == 0 else avg
print(f"Average:      {mean}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55
```

---
