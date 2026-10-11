## Conditions

In Python (as in most programming languages) a *condition* is any expression
that evaluates to `True` or `False`.

These are known as Boolean values, after George Boole, the creator of Boolean
Algebra.

---

### Branching

The main use of conditionals is to branch code into different paths depending
on the state of a variable or group of variables. This is most commonly handled
with `if`-`else` statements.

Like loops, `if` and `else` branches are blocks, denoted by a colon `:` and
indented lines.

```python
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
```

Output:

```
Audi
BMW
Subaru
Toyota
```

---
