## Conditions

In Python, a *condition* is an expression that Python checks for truth. Most conditions
evaluate to `True` or `False`, and these are called Boolean values, after George Boole,
who developed the logic behind them.

Python is a little more relaxed than that. In an `if` statement, it doesn't need a
Boolean. It looks at the truth value of whatever you give it. Empty lists, `0`, and empty
strings all count as `False`, and most other values count as `True`. We'll use that later
in the chapter, so keep it in mind.

---

### Branching

The main use of conditionals is to branch your code into different paths, depending on the
state of a variable or a group of variables.

The most common tool for this is the `if`-`else` statement. The code takes one path (`if`)
when the condition is `True`, and a different path (`else`) when it's `False`.

Like loops, `if` and `else` branches are blocks. A colon `:` starts the block, and the lines
inside it are indented.

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

