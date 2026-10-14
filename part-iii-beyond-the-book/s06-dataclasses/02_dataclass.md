## Using a DataClass

Let's build the same `Employee` class as a DataClass.

---

### A Simple `Employee` DataClass

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

---

### What About the Missing Stuff?

With a DataClass, the `__init__()`, `__repr__()` and `__eq__()` methods are
automatically generated. We don't need to code them at all.

Let's test this code:

```python
# -- SNIP --

emp_1 = Employee("Scott", "smclean", 53, "Dallas")
emp_2 = Employee("John", "Smith", 30, "Cleveland")

emp_3 = Employee("Scott", "smclean", 53, "Dallas")

print(emp_1)
print(emp_2)

print(f"emp_1 == emp_2? {emp_1 == emp_2}")
print(f"emp_1 == emp_3? {emp_1 == emp_3}")
```

Output:

```
Employee(name='Scott', emp_id='smclean', age=53, city='Dallas')
Employee(name='John', emp_id='Smith', age=30, city='Cleveland')
emp_1 == emp_2? False
emp_1 == emp_3? True
```

Those results are nearly identical to our results from the traditional class,
but we wrote a whole lot less code to get there.

---
