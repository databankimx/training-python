## Automatic Flag Values

It's both annoying and error-prone to have the programmer be responsible
for setting the values in a `Flag` enum.

The `enum` library provides a mechanism fo automatically setting those
values.

---

### Using `auto()` in a `Flag` Enum

Using the `auto()` function, the values are set as the appropriate
power of two in the order items are added:

> Note: You can use the `auto()` function with regular `Enum` classes as
> well. The items will be numbered in order: 1, 2, 3 rather than powers
> of two.

```python
from enum import Flag, auto

class Weekday(Flag):
    """Defines names for days of the week as bit-flags"""
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY
```

---

### Testing

We can easily validate this:

```python
for day in [Weekday.SATURDAY, Weekday.SUNDAY, Weekday.WEEKEND]:
    print(day, "=", day.value)
```

Output:

```
Weekday.SATURDAY = 32
Weekday.SUNDAY = 64
Weekday.WEEKEND = 96
```

---

### Looping

And since we know we're working with powers of two, we can easily loop 
through the values:

```python
for i in [2 ** n for n in range(7)]:
    print(f"{i:>2}", Weekday(i))
```

Output:

```
 1 Weekday.MONDAY
 2 Weekday.TUESDAY
 4 Weekday.WEDNESDAY
 8 Weekday.THURSDAY
16 Weekday.FRIDAY
32 Weekday.SATURDAY
64 Weekday.SUNDAY
```

---
