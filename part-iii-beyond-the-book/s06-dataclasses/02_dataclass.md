## Using a Dataclass

Let's build the same `Employee` class as a dataclass.

---

### A Simple `Employee` Dataclass

Here is the implementation using the same four attributes:

* `name`
* `emp_id`
* `age`
* `city`

```python
from dataclasses import dataclass

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str
```

Note that we have done the following:

1. Decorated the class with `@dataclass`
2. Declared our attributes in the form: `name: type_hint`

The type hints document the intended types, and tools such as type checkers use
them. Python doesn't check them at runtime, so `Employee(53, 42, "x", "Dallas")`
would still be accepted without an error.

---

### What About the Missing Stuff?

With a dataclass, the `__init__()`, `__repr__()` and `__eq__()` methods are
automatically generated. We don't need to code them at all.

Because `__eq__()` is generated without a `__hash__()` method, Python sets
`__hash__` to `None` for the class. That makes its instances unhashable, so they
can't be used as dictionary keys or stored in a set. Later lessons cover how to
change that.

Let's test this code:

```python
# -- SNIP --

emp_1 = Employee("Scott McLean", "smclean", 53, "Dallas")
emp_2 = Employee("John Smith", "jsmith", 30, "Cleveland")

emp_3 = Employee("Scott McLean", "smclean", 53, "Dallas")

print(emp_1)
print(emp_2)

print(f"emp_1 == emp_2? {emp_1 == emp_2}")
print(f"emp_1 == emp_3? {emp_1 == emp_3}")
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=53, city='Dallas')
Employee(name='John Smith', emp_id='jsmith', age=30, city='Cleveland')
emp_1 == emp_2? False
emp_1 == emp_3? True
```

The comparison results match the traditional class. The printed form differs,
because the traditional class has its own `__repr__()`, and the dataclass uses the
generated one. But we wrote a whole lot less code to get there.

---
