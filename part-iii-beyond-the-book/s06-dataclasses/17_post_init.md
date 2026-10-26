## The `__post_init__()` Function

When creating a class instance, the `__init__()` function automatically
calls `__post_init__()` after populating attribute data. Typically, this
does nothing, but you can implement additional functionality by defining the
function.

---

### Implementation

Consider this example:

```python
from dataclasses import dataclass, field

@dataclass()
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str
    age_verified: bool = field(init=False)

    def __post_init__(self) -> None:
        min_age = 30
        self.age_verified = self.age > min_age

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas', age_verified=True)
```

The `age_verified` field has no default, and it's marked `init=False`, so it isn't
passed to the constructor. The `__post_init__()` method computes its value instead.
Without that method, the field would never be set, and printing the instance would
fail.

---

### Validating Input

Since `__post_init__()` runs for every new instance, it's also the usual place to
check values and reject bad input. This version raises a `ValueError` when the
age is negative:

```python
@dataclass
class Employee:
    name: str
    emp_id: str
    age: int

    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValueError(f"age cannot be negative: {self.age}")

emp = Employee("Scott McLean", "smclean", -5)
```

Output (the full traceback is omitted here):

```
ValueError: age cannot be negative: -5
```

---
