## The `default_factory` Field Attribute

Using the `default_factory` attribute on any field allows you to set a 
function that returns a default value for that field if it is omitted from 
the call to create a new class instance.

> Note: The default factory function cannot accept any arguments and should
> be created outside the class.

---

### Example Code

Here's an example of a default factory function for our `Employee` class:

```python
from dataclasses import dataclass, field

def get_emp_id():
    """Factory Function"""
    id = "smclean"
    return id

@dataclass
class Employee:
    name: str
    age: int
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="Dallas")

emp_1 = Employee("Scott", 54)
emp_2 = Employee("Saul", 47, "sgoodman", "Albuquerque")

print(emp_1)
print(emp_2)
```

Output:

```
Employee(name='Scott', age=54, emp_id='smclean', city='Dallas')     
Employee(name='Saul', age=47, emp_id='sgoodman', city='Albuquerque')
```

---

### Effect on `__dataclass_fields__`

Having declared a default factory for the `emp_id` field will change the 
output of the `__dataclass_fields__` object as well...

```
...
Field(
    name='emp_id',
    type=<class 'str'>,
    default=<dataclasses._MISSING_TYPE object at 0x0000013E2E2455D0>,
    default_factory=<function get_emp_id at 0x0000013E2DDA04A0>
    ...
)
...
```

---
