## Inheritance with Dataclasses

Inheritance with dataclasses is basically the same as class inheritance
anywhere else in Python:  
`class ClassName(ParentClass):`

The main difference is that there is no need to explicitly call the 
`super()` function and the parent class `__init__()` method when instantiating
a child class object. Dataclasses take care of that for us in the generated
`__init__()` function.

Only dataclass parents contribute fields. A parent class that isn't a dataclass
doesn't pass its annotated attributes on to the child.

---

Consider this example:

```python
from dataclasses import dataclass

@dataclass()
class Staff:
    """Metadata about a staff member"""
    name: str
    emp_id: str
    age: int
    city: str

@dataclass
class Employee(Staff):
    """Metadata about an employee"""
    salary: int

emp = Employee("Scott McLean", "smclean", 54, "Dallas", 50_000)
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas', salary=50000)
```

The parent's fields come first in the generated `__init__()` and in the repr,
followed by the child's fields. That's why `salary` is last in the output.

The default-ordering rule from the `default` lesson applies across the parent and
child as well. If the parent has a field with a default, a child field without one
raises a `TypeError`, because a field without a default can't follow one with a
default. See the [default lesson](./11_field_default.md) for that rule.

---
