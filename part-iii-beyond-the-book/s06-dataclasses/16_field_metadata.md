## The `metadata` Field Attribute

The field attribute `metadata` provides a place to store additional 
information (in the form of a dictionary) about the field. Typically this is 
used to include some data that would be used separately from the field value.
The `metadata` value can be accessed from the `__dataclass_fields__` 
dictionary.

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
    city: str = field(default="Dallas", metadata={"gps": (32.78306, -96.80667)})

emp = Employee("Scott McLean", "smclean", 54)
print(emp)
print(emp.__dataclass_fields__["city"].metadata["gps"])
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas')
(32.78306, -96.80667)
```

---
