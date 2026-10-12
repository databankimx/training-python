## Numeric Lists and the `range()` Function

The `range()` function allows you to access a sequential, numeric list without 
declaring it as a variable.

Syntax:

```python
range([start,] stop[, step])
```

Rules:

* The `stop` value must be one higher than the last value you want to process
    * This is known as "off-by-one" behavior
* The `step` value specifies the increment between one value and the next value
* If only one parameter is specified:
    * The specified value is `stop`
    * The `start` value defaults to `0`
    * The `step` value defaults to `1`
* If two parameters are specified
    * The specified values are `start` and `stop`
    * The `step` value defaults to `1`

---

Examples:

#### A `range` with only `stop` specified

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

#### A `range` with `start` and `stop` specified

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

#### A `range` with `start`, `stop`, and `step` specified

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

#### A loop using a `range` to create a list

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
