## Numeric Lists and the `range()` Function

The `range()` function generates a sequence of numbers without storing them
all in memory at once.

Syntax:

```python
range([start,] stop[, step])
```

Rules:

- `stop` must be one higher than the last value you want - this is "off-by-one" behavior
- `step` specifies the increment between values
- With one argument: that value is `stop`; `start` defaults to `0`, `step` to `1`
- With two arguments: `start` and `stop`; `step` defaults to `1`

---

#### Only `stop` specified

```python
for i in range(3):
    print(i)
```

Output:

```
0
1
2
```

---

#### `start` and `stop` specified

```python
for i in range(1, 4):
    print(i)
```

Output:

```
1
2
3
```

---

#### `start`, `stop`, and `step` specified

```python
for i in range(2, 7, 2):
    print(i)
```

Output:

```
2
4
6
```

---

#### Using `range()` to build a list

```python
squares = []
for value in range(1, 6):
    squares.append(value ** 2)
print(squares)
```

Output:

```
[1, 4, 9, 16, 25]
```

---

#### Converting `range()` directly to a list

```python
numbers = list(range(1, 6))
print(numbers)
```

Output:

```
[1, 2, 3, 4, 5]
```

---
