## Conditions

In Python (as in most programming languages) a *condition* is any 
expression that evaluates to `True` or `False`.

These are known as Boolean values (after George Boole, the creator of
Boolean Algebra, which we'll discuss in lesson 3).

---

### Branching

The main use of conditionals in programming is to branch code into 
different paths, depending on the state (or condition) of a variable or
group of variables.

This is most commonly handled by using `if`-`else` statements, where the
code traverses one path (`if`) when the condition is `True` and a different
path (`else`) when the condition is `False`.

Like loops, `if` and `else` branches are blocks, denoted by a colon `:` to 
start the block and indented lines for code within the block.

```python
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        # Path when condition is `True`
        print(car.upper())
    else:
        # Path when condition is `False`
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
