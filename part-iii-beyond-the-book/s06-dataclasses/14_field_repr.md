## The `repr` Field Attribute

The `repr` attribute is a boolean value that indicates whether or not the
field should be included in the `__repr__()` string. By default, the
value is `True` (as you've already seen, all fields are in the string 
representation by default), so this attribute should only be specified when 
it will be `False` (to remove the field from the output string).

---

### Example Code

Here's an example where we set the `repr` value in our `Employee` class:

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int = field(repr=False)
    emp_id: str
    city: str = field(init=False, default="Dallas")

emp = Employee("Scott McLean", 53, "smclean")
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', city='Dallas')
```

The `age` field is left out of the string, but it's still stored. The `repr`
setting only affects the string output:

```python
print(emp.age)
```

Output:

```
53
```

---

### Effect on `__dataclass_fields__`

Like the other field settings, setting the `repr` attribute on a field affects
its entry in `__dataclass_fields__`. Printing the `age` entry:

```python
print(emp.__dataclass_fields__["age"])
```

Output (formatted across lines for readability, and the memory address will
vary):

```
Field(
    name='age',
    type=<class 'int'>,
    default=<dataclasses._MISSING_TYPE object at 0x0000013E2E2455D0>,
    default_factory=<dataclasses._MISSING_TYPE object at 0x0000013E2E2455D0>,
    init=True,
    repr=False,
    hash=None,
    compare=True,
    metadata=mappingproxy({}),
    kw_only=False,
    _field_type=_FIELD
)
```

> Note: the code file turns off a Pylint warning about `__dataclass_fields__`
> (no-member). That comment stays in the code file.

---
