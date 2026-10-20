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

    def __post_init__(self):
        min_age = 30
        self.age_verified = self.age > min_age

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas', age_verified=True)
```

---
