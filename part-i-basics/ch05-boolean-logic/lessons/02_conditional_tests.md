## Conditional Tests (Comparisons)

A conditional test is a comparison between two values.

| Operator | Comparison | Result |
|:-:|-|-|
| `==` | equal | `True` when both operands contain the same value |
| `!=` | not equal | `True` when the operands contain different values |
| `<` | less than | `True` when the left value is less than the right value |
| `<=` | less than or equal | `True` when the left value is less than or equal to the right value |
| `>` | greater than | `True` when the left value is more than the right value |
| `>=` | greater than or equal | `True` when the left value is more than or equal to the right value |
| `is` | same object | `True` when both operands point to the same object in memory |
| `is not` | different object | `True` when the operands point to different objects in memory |
| `not` | inverse/negation | `True` when the right (and only) operand is `False` |

---

### Equivalency (`==`)

The most commonly used test. The data must be identical, including type (with
one exception: an integer can equal a float when the float's decimal part is
zero, e.g. `2 == 2.0` returns `True`).

#### Equivalency with Numbers

```python
num = 1
print(num == 1)
print(num == 1.0)
print(num == 2)
print(num != 2)
```

Output:

```
True
True
False
True
```

---

#### Equivalency with Strings

String comparisons are case-sensitive. Use `upper()` or `lower()` to normalize
before comparing.

```python
car = "bmw"
print(car == "bmw")
print(car == "BMW")
print(car.upper() == "BMW")
```

Output:

```
True
False
True
```

---

### Object Equivalency (`is`)

`is` checks that two operands point to the same object in memory, not just
that their values are equal.

```python
lst = [1, 2, 3]
ref = lst
print(ref == lst)
print(ref is lst)
cpy = lst[:]
print(cpy == lst)
print(cpy is lst)
print(cpy is not lst)
```

Output:

```
True
True
True
False
True
```

---

### Inequalities (`>`, `>=`, `<`, `<=`)

#### With Numbers

```python
age = 21
print(age > 18)
print(age < 18)
print(age >= 25)
print(age <= 25)
```

Output:

```
True
False
False
True
```

---

#### With Strings

String inequalities compare ASCII values, not alphabetical order. Any lower
case letter always evaluates as greater than any upper case letter (lower case
letters start at ASCII 97, upper case at 65). Normalize with `upper()` or
`lower()` before comparing when you want alphabetical ordering.

```python
left = "apple"
right = "Zebra"
print(right > left)
print(right.upper() > left.upper())
```

Output:

```
False
True
```

---
