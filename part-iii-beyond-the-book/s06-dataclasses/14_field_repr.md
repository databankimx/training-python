## The `repr` Field Attribute

The `repr` attribute is a boolean value that indicates whether or not the
field should be included in the `__repr__()` string. By default, the
value is `True` (as you've already seen, all fields are in the string 
representation by default), so this attribute should only be specified when 
it will be `False` (to remove the field from the output string).

---

### Example Code

Here's an example where we set the `init` value in our `Employee` class:

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int = field(repr=False)
    emp_id: str
    city: str = field(init=False, default="Dallas")

emp = Employee("Scott", "smclean", 53)
print(emp)
```

Output:

```
Employee(name='Scott', emp_id='smclean', city='Dallas')
```

---

### Effect on `__dataclass_fields__`

Like the other field settings, setting the `init` attribute on a field 
affects the `__dataclass_fields__`

```
...
Field(
    name='age',
    type=<class 'int'>,
    ...
    repr=False,
    ...
)
...
```

---
