# Rolling a D6

## Introduction

A die is a simple model of randomness. A standard six-sided die, or D6, gives each face the same
chance of landing up. In this lesson we model a die as a class, roll it a few times, and print the
results. The next lessons count the results and plot them.

The `Die` class lives in `die.py`, in the same folder as the lessons, so every lesson in this
folder can import it.

---

## The Code

The `Die` class is in `die.py`:

```python
"""Class representing a single die"""

from random import randint

class Die:
    """Class representing a single die"""

    def __init__(self, num_sides = 6):
        """Initialize - Assume 6-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random number between 1 and number of sides"""
        return randint(1, self.num_sides)
```

The lesson script uses the class:

```python
"""Lesson 3.1 - Rolling a D6"""

from die import Die

# Create a D6
die = Die()

# Roll a few times and store in a list
results = []
for _ in range(100):
    results.append(die.roll())

print(results)
```

---

### Walking Through the Code

**The class.** `Die` stores the number of sides. The default is 6, so `Die()` is a standard
die. `Die(10)` would be a ten-sided die.

**Rolling.** `roll()` returns a whole number from 1 up to the number of sides. `randint(1, 6)`
includes both ends, so 1 and 6 can both come up.

**Repeated rolls.** The loop rolls the die 100 times and adds each result to the `results`
list. `_` is a name for a value we don't need, here the loop counter.

**Printing.** `print(results)` shows the whole list.

---

### Output

The terminal prints a list of 100 numbers, each from 1 to 6. The list is different every time the
script runs. A sample run looks like this:

```
[2, 2, 6, 2, 1, 1, 5, 6, 2, 6, 5, 6, 3, 1, 5, 3, 6, 2, 2, 4, 5, 6, 5, 5, 1, 3, 5, 6, 2, 6, 5, 4, 1, 5, 6, 4, 5, 3, 4, 6, 4, 2, 1, 6, 1, 6, 5, 2, 6, 1, 2, 6, 4, 4, 3, 2, 1, 3, 6, 1, 4, 3, 6, 3, 2, 1, 1, 2, 6, 5, 2, 1, 4, 4, 3, 2, 3, 2, 5, 3, 4, 1, 1, 5, 5, 3, 4, 2, 3, 6, 4, 6, 2, 5, 1, 2, 5, 2, 4, 6]
```

---
