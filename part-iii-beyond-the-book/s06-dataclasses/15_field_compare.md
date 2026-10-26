## The `compare` Field Attribute

When the `compare` attribute is `True` (which is the default value), the field
will be included in the equality and comparison methods generated based on the
class-level values of `eq` and `order`:

* `__eq__()`
* `__gt__()`
* `__ge__()`
* `__lt__()`
* `__le__()`

---

### By Default All Attributes Are Included

Recall that when we added the `order` attribute to the class-level settings,
we saw these results:

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

print(f"emp_1 > emp_2: {emp_1 > emp_2}")
```

Output:

```
emp_1 > emp_2: True
```

This is `True` because `name` is the first field, and `'Scott McLean' > 'Saul Goodman'`
decides the result before `age` is ever compared.

---

### Controlling Field Inclusion

But consider this modified code:

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Employee:
    """Metadata about an employee"""
    name: str = field(compare=False)
    emp_id: str = field(compare=False)
    age: int
    city: str = field(compare=False)

emp_1 = Employee("Scott McLean", "smclean", 54, "Dallas")
emp_2 = Employee("Saul Goodman", "sgoodman", 57, "Albuquerque")

print(f"emp_1 > emp_2: {emp_1 > emp_2}")
```

Output:

```
emp_1 > emp_2: False
```

Now the same comparison yields `False`, because we are only allowing `age` to 
be evaluated.

The code file has this modified version. The first example above comes from the
ordering lesson, where the class is unmodified.

`compare` also applies to `__eq__()`. With `compare=False` on `name`, `emp_id`,
and `city`, two employees with the same age compare equal, even if their names
differ:

```python
emp_3 = Employee("Jane Doe", "jdoe", 54, "Austin")
print(f"emp_1 == emp_3: {emp_1 == emp_3}")
```

Output:

```
emp_1 == emp_3: True
```

---
