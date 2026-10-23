## The `metadata` Field Attribute

The field attribute `metadata` provides a place to store additional 
information (in the form of a dictionary) about the field. The dataclass itself
ignores this information. It's there for your own code, such as a validator, a
serializer, or a form builder, to read when it works with the fields. The
`metadata` value can be accessed from the `__dataclass_fields__` dictionary.

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

> Note: the code file turns off a Pylint warning about `__dataclass_fields__`
> (no-member). That comment stays in the code file.

---

### The Metadata Is Read-Only

Python wraps the metadata in a read-only `mappingproxy`, so you can't change it
through the field. This assignment fails:

```python
emp.__dataclass_fields__["city"].metadata["gps"] = (0, 0)
```

Output:

```
TypeError: 'mappingproxy' object does not support item assignment
```

If the metadata needs to change, change the field declaration in the class.

---
