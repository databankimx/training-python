## Enumerations

Sometimes when you want to use global variables with constant values, they may be related to one another meaningfully.

For example, you might be working with the days of the week and have
variables like:

```python
MONDAY = 1
TUESDAY = 2
...
```

In a case like this, it is useful to be able to group them together for
ease of use and maintenance.

To this end, the `enum` library in Python exposes the ability to create
enumerations, which are groups of related constant values.

In addition to meaningful grouping, an enumeration provides several
benefits:

* A more useful `__repr__()` that you would have with a standalone
  global variable.
* Type-safety (since the enum is a data type)
* Meaningful name/value relationships
* And other features depending on the type of enumeration

---

### Grouping Related Values

Enumerations are useful when the set of related values are

* Relatively few
* Constant

Let's expand the set of global variables we looked at above into an
`Enum`

To define a new enumeration, you declare a class ann inherit the `Enum`
type from the `enum` library.

The, within the class, you simply define values for each possible 
variant.

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
```

---

### Accessing `Enum` Variants

#### By Value

We can access a variant by the value that we assigned to it:

```python
print(Weekday(3))
```

Output:

```
Weekday.WEDNESDAY
```

---

#### `repr()` vs `str()`

The `repr()` method includes the value, while the `str()` method only
includes the variant name.

```python
print(repr(Weekday(2)))
print(str(Weekday(2)))
```

Output:

```
<Weekday.TUESDAY: 2>
Weekday.TUESDAY
```

---

#### By Name

We can also access a variant by its name

```python
print(Weekday.THURSDAY)
```

Output:

```
Weekday.THURSDAY
```

---

#### The `name` and `value` Attributes

Enums expose two useful properties: `name` and `value`:

```python
print(Weekday.FRIDAY.name)
print(Weekday.FRIDAY.value)
```

Output:

```
FRIDAY
5
```

---

### Type Safety

Because an enumeration is declared as a class, each of its variants are
of the data type of the class:

```python
print(type(Weekday.MONDAY))
print(isinstance(Weekday.MONDAY, Weekday))
```

Output:

```
<enum 'Weekday'>
True
```

---
