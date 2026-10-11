## Combining Multiple Conditionals

Often it is necessary to check multiple conditions simultaneously. Python
provides logical operators to handle this cleanly.

---

### Logical `and`

Returns `True` only when both conditions are `True`.

| p | `and` | q |
|:-:|:-:|:-:|
| T | **T** | T |
| T | F | F |
| F | F | T |
| F | F | F |

```python
min_val = 10
max_val = 20
n = 15
if n > min_val and n < max_val:
    print("OK")
else:
    print("ERROR")
```

Output:

```
OK
```

Evaluation:
1. `n > min_val` -> `True`
2. `n < max_val` -> `True`
3. `True and True` -> `True`

---

### Logical `or`

Returns `True` when at least one operand is `True`. Only `False` when both are
`False` (inclusive or).

| p | `or` | q |
|:-:|:-:|:-:|
| T | **T** | T |
| T | **T** | F |
| F | **T** | T |
| F | F | F |

```python
min_val = 10
max_val = 20
n = 15
if n < min_val or n > max_val:
    print("ERROR")
else:
    print("OK")
```

Output:

```
OK
```

---

### Logical `not`

Takes a single operand and returns the opposite value.

| `not` | p |
|:-:|:-:|
| F | T |
| T | F |

```python
print(not True)
print(not False)
```

Output:

```
False
True
```

---

### Logical Operator Precedence

`and` has higher precedence than `or`. Evaluate `and` first, then `or`.
Use parentheses to override.

```python
lst = [1, 2, 3, 4, 5]
if len(lst) > 3 or lst[0] == 1 and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")
```

Output:

```
OK
```

Evaluation (resolving `and` first):
1. `lst[0] == 1 and lst[-1] == 2` -> `True and False` -> `False`
2. `len(lst) > 3 or False` -> `True or False` -> `True`

With parentheses forcing `or` first:

```python
if (len(lst) > 3 or lst[0] == 1) and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")
```

Output:

```
ERROR
```

---

### Bonus - Simulating XOR

Python has no `xor` keyword. XOR means `or` but not `and` - `True` only
when exactly one operand is `True`.

| p | XOR | q |
|:-:|:-:|:-:|
| T | F | T |
| T | **T** | F |
| F | **T** | T |
| F | F | F |

```python
p = True
q = False
p_xor_q = (p or q) and not (p and q)
print(f"{p} XOR {q} = {p_xor_q}")
```

Output:

```
True XOR False = True
```

---

### Bonus - Chaining Inequalities

Python allows chaining multiple inequalities without `and`:

```python
s = 1
m = 5
l = 10
m_between = s < m < l
print(m_between)
```

Output:

```
True
```

Chain only in one direction - mix `<` and `>` in the same chain at your peril.

---
