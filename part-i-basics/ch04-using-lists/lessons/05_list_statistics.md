## List Statistics

Python provides several built-in functions for getting information about a
numeric list.

| Function | Effect |
|-|-|
| `len(list)` | Number of elements |
| `min(list)` | Lowest value |
| `max(list)` | Highest value |
| `sum(list)` | Sum of all values |

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

### Computing an Average

Division always returns a float in Python, even when the result is a whole
number:

```python
digits = list(range(10))
print(f"Average: {sum(digits) / len(digits)}")
```

Output:

```
Average: 4.5
```

---

### Using the `statistics` Module

The standard library's `statistics` module provides a `mean()` function that
returns an integer when the result is whole:

```python
import statistics

tens = list(range(10, 101, 10))
print(f"Average: {statistics.mean(tens)}")
```

Output:

```
Average: 55
```

---

### Eliminating the Unnecessary Float Manually

You can also use modulo arithmetic to strip the `.0` when not needed:

```python
tens = list(range(10, 101, 10))
avg = sum(tens) / len(tens)
mean = int(avg) if (avg * 10) % 10 == 0 else avg
print(f"Average: {mean}")
```

Output:

```
Average: 55
```

---
