## The Dataclass `order` Argument

When the `order` argument is `True` (default value is `False`), the dataclass 
generates the following methods automatically

* `__gt__()`
* `__ge__()`
* `__lt__()`
* `__le__()`

These compare all fields in the class, in the order they are declared, between
two objects. Two instances are compared field by field: the first field decides
the result unless the two values are equal, in which case the next field is
compared, and so on.

Be careful with using this. The results depend on the order the fields are
declared, so reordering the fields can change how instances sort.

---

### Added Comparison Methods

Consider this code:

```python
from dataclasses import dataclass

@dataclass(order=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp_1 = Employee("Scott McLean", "smclean", 54, "Dallas")
emp_2 = Employee("Saul Goodman", "sgoodman", 57, "Albuquerque")
emp_3 = Employee("Scott McLean", "smclean", 54, "Dallas")

print(f"emp_1 > emp_2: {emp_1 > emp_2}")
print(f"emp_1 < emp_3: {emp_1 < emp_3}")
print(f"emp_1 <= emp_3: {emp_1 <= emp_3}")
```

Output:

```
emp_1 > emp_2: True
emp_1 < emp_3: False
emp_1 <= emp_3: True
```

> Notice how `emp_1 > emp_2` returns true, even though `emp_2` has a larger
> value for `age`. This is because the first field, `name`, decides the result:
> `'Scott McLean'` is larger than `'Saul Goodman'` alphabetically, so `age` is
> never compared.

---

### Comparing With Other Types

The comparison methods only work with instances of the same class. Comparing an
`Employee` with a value of another type returns `NotImplemented`, and Python then
raises a `TypeError`:

```python
emp_1 < 54
```

Output:

```
TypeError: '<' not supported between instances of 'Employee' and 'int'
```

> Note: `order=True` requires `eq=True`. If you set `eq=False` and `order=True`
> together, the dataclass raises a `ValueError`. Since `eq` is `True` by default,
> you only run into this if you turn `eq` off.

---
