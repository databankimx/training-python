## Logical Comparisons with Enums

Logical comparisons using Enums can be a bit complicated if we don't 
understand what we're looking at.

---

### Understanding Types

#### `Enum` is Not an Integer

In some languages, an enum is natively of the integer type declared. In
Python, that is not the case.

Let's look at the simple version of our `Weekday` enum.

```python
from enum import Enum

class Weekday(Enum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    HUMP_DAY = 3
```

Let's interrogate its type:

```python
print("type(Weekday.MONDAY):", 
      type(Weekday.MONDAY))
print("isinstance(Weekday.MONDAY, int):",
      isinstance(Weekday.MONDAY, int))
print("type(Weekday.MONDAY.value):", 
      type(Weekday.MONDAY.value))
print("isinstance(Weekday.MONDAY.value, int):",
      isinstance(Weekday.MONDAY.value, int))
```

Output:

```
type(Weekday.MONDAY): <enum 'Weekday'>
isinstance(Weekday.MONDAY, int): False
type(Weekday.MONDAY.value): <class 'int'>
isinstance(Weekday.MONDAY.value, int): True
```

We can see that the type is our class and that Python does not treat
the variant as an integer.

Its value, however *is* an integer.

That's a little limiting, because it means that many comparisons can
only be made using the `.value` attribute.

---

#### `IntEnum` is an Integer (Sort of)

The `enum` library provides a separate `IntEnum` type that is 
specifically designed to be treated as an integer.

Repeating the above test with an `IntEnum` yields this:

```python
from enum import IntEnum

class IntWeekday(IntEnum):
    """Defines names for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    HUMP_DAY = 3

print("type(IntWeekday.MONDAY):",
        type(IntWeekday.MONDAY))
print("isinstance(IntWeekday.MONDAY, int):",
        isinstance(IntWeekday.MONDAY, int))
print("type(IntWeekday.MONDAY.value):", 
    type(IntWeekday.MONDAY.value))
print("isinstance(IntWeekday.MONDAY.value, int):",
    isinstance(IntWeekday.MONDAY.value, int))
```

Output:

```
type(IntWeekday.MONDAY): <enum 'IntWeekday'>
isinstance(IntWeekday.MONDAY, int): True
type(IntWeekday.MONDAY.value): <class 'int'>
isinstance(IntWeekday.MONDAY.value, int): True
```

We can see one difference: `isinstance(IntWeekday.MONDAY, int)` is
`True`. That means that we can use an `IntEnum` as if it were an 
integer without having to obtain the value first.

This will have an effect on some of the logical comparisons below.

---

### Checking Equivalency: `==`

Let's have a look at how our types affect equivalency checks:

```python
print("Weekday.MONDAY == IntWeekday.MONDAY:",
        Weekday.MONDAY == IntWeekday.MONDAY)
print("Weekday.MONDAY.value == IntWeekday.MONDAY.value:",
        Weekday.MONDAY.value == IntWeekday.MONDAY.value)
print("Weekday.MONDAY == 1:",
        Weekday.MONDAY == 1)
print("IntWeekday.MONDAY == 1:",
        IntWeekday.MONDAY == 1)
print("Weekday.MONDAY.value == 1:",
        Weekday.MONDAY.value == 1)
print("IntWeekday.MONDAY.value == 1:",
        IntWeekday.MONDAY.value == 1)
```

Output:

```
Weekday.MONDAY == IntWeekday.MONDAY: False
Weekday.MONDAY.value == IntWeekday.MONDAY.value: True
Weekday.MONDAY == 1: False
IntWeekday.MONDAY == 1: True
Weekday.MONDAY.value == 1: True
IntWeekday.MONDAY.value == 1: True
```

We can see that:

* We can't compare a `Weekday` against an `IntWeekday`, even if their
  values are the same.
* We can compare the `.value` attributes between the two enum types
* We cannot compare a `Weekday` against an integer
* We **can** compare an `IntWeekday` against an integer (important)
* We can compare the `.value` attribute of either type against an 
  integer.

---

### Checking Identity: `is`

Let's take a look at how our enum types behave when using `is` for
comparisons:

```python
print("Weekday.MONDAY is IntWeekday.MONDAY:",
        Weekday.MONDAY is IntWeekday.MONDAY)
print("Weekday.MONDAY.value is IntWeekday.MONDAY.value:",
        Weekday.MONDAY.value is IntWeekday.MONDAY.value)
print("Weekday.MONDAY is 1:",
        Weekday.MONDAY is 1)
print("IntWeekday.MONDAY is 1:",
        IntWeekday.MONDAY is 1)
print("Weekday.MONDAY.value is 1:",
        Weekday.MONDAY.value is 1)
print("IntWeekday.MONDAY.value is 1:",
        IntWeekday.MONDAY.value is 1)
```

Output:

```
Weekday.MONDAY is IntWeekday.MONDAY: False
Weekday.MONDAY.value is IntWeekday.MONDAY.value: True
Weekday.MONDAY is 1: False
IntWeekday.MONDAY is 1: False
Weekday.MONDAY.value is 1: True
IntWeekday.MONDAY.value is 1: True
```

The only notable item here is that where `IntEnum == int` was `True`,
`IntEnum is int` is `False`

---

### Checking Inequalities: `>`, `<`, `>=`, `<=`

Inequalities are where we see the most significant difference between
out `Enum` and `IntEnum` types.

#### Cannot Compare `Enum` Variants with Inequalities

This...

```python
print("Weekday.MONDAY < Weekday.TUESDAY:",
        Weekday.MONDAY < Weekday.TUESDAY)
```

... will result in a TypeError

Output:

```
Traceback (most recent call last):
  File "...\06_comparisons.py", line 111, in <module>
    main()
  File "...\06_comparisons.py", line 107, in main   
    check_inequalities()
  File "...\06_comparisons.py", line 77, in check_inequalities
    Weekday.MONDAY < Weekday.TUESDAY
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '<' not supported between instances of 'Weekday' and 'Weekday'
```

Remember that `Enum` types do not behave like integers.

---

#### Can Compare `.value` or `IntEnum` Variants with Inequalities

Since the values and/or any `IntEnum` types *do* behave like integers,
any of these will work:

```python
print("IntWeekday.MONDAY < IntWeekday.TUESDAY:",
    IntWeekday.MONDAY < IntWeekday.TUESDAY)
print("Weekday.MONDAY.value < Weekday.TUESDAY.value:",
        Weekday.MONDAY.value < Weekday.TUESDAY.value)
print("IntWeekday.MONDAY.value < IntWeekday.TUESDAY.value:",
    IntWeekday.MONDAY.value < IntWeekday.TUESDAY.value)
```

Output:

```
IntWeekday.MONDAY < IntWeekday.TUESDAY: True
Weekday.MONDAY.value < Weekday.TUESDAY.value: True
IntWeekday.MONDAY.value < IntWeekday.TUESDAY.value: True
```

---
