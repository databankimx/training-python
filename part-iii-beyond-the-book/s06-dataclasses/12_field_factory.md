## The `default_factory` Field Attribute

Using the `default_factory` attribute on any field allows you to set a 
function that returns a default value for that field if it is omitted from 
the call to create a new class instance.

> Note: The default factory function cannot accept any arguments, so it can't
> see the other fields of the instance. It should be a module-level function, not
> defined inside the class.

---

### Example Code

Here's an example of a default factory function for our `Employee` class. The
factory can't receive any data, so it keeps its own state: a module-level counter
that hands out the next ID each time it's called.

```python
from dataclasses import dataclass, field
from itertools import count

_id_counter = count(1)

def get_emp_id() -> str:
    """Factory Function: returns the next employee ID"""
    return f"emp{next(_id_counter):04d}"

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="Dallas")

emp_1 = Employee("Scott McLean", 54)
emp_2 = Employee("Saul Goodman", 47, "sgoodman", "Albuquerque")
emp_3 = Employee("Jane Doe", 30)

print(emp_1.emp_id)
print(emp_1)
print(emp_2)
print(emp_3)
```

Output:

```
emp0001
Employee(name='Scott McLean', age=54, emp_id='emp0001', city='Dallas')
Employee(name='Saul Goodman', age=47, emp_id='sgoodman', city='Albuquerque')
Employee(name='Jane Doe', age=30, emp_id='emp0002', city='Dallas')
```

This shows three things:

* **Each instance gets its own value.** Scott and Jane get different IDs from the
  same factory.
* **The factory is skipped when a value is passed.** Saul's ID is supplied, so
  the counter doesn't advance, and Jane gets `emp0002`.
* **The state lives outside the function.** The factory takes no arguments, so
  the counter has to be module-level. That shared state is the trade-off.

If the ID needed to be built from the other fields, such as the name, a factory
couldn't do it, since it can't see them. That's the job of `__post_init__()`,
covered in the [post-init lesson](./17_post_init.md).

---

### Effect on `__dataclass_fields__`

Declaring a default factory for the `emp_id` field changes its entry in
`__dataclass_fields__`. Printing that entry shows `default_factory` set to the
function, and `default` set to the missing-value marker:

```python
print(emp_1.__dataclass_fields__["emp_id"])
```

Output (formatted across lines for readability, and the memory addresses will
vary):

```
Field(
    name='emp_id',
    type=<class 'str'>,
    default=<dataclasses._MISSING_TYPE object at 0x0000013E2E2455D0>,
    default_factory=<function get_emp_id at 0x0000013E2DDA04A0>,
    init=True,
    repr=True,
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

### A Mutable Default, Done Properly

Lesson 11 warned against a mutable default such as `field(default=[])`. A
default factory is the fix, because the factory runs once per instance:

```python
@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)
```

Each `Team` gets its own empty list, so adding a member to one team doesn't change
another.

---
