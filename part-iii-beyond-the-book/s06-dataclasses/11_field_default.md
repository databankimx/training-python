## The `default` Field Attribute

Using the `default` attribute on any field allows you to set the default value
for that field if it is omitted from the call to create a new class instance.

> Note: Just like regular functions, fields with defaults must occur at the end
> of the call.
>
> In a dataclass, this means they must be declared last in order in the class
> itself. The exception is keyword-only fields, covered in the `kw_only` lesson.

---

### Example Code

Here's an example of a default value for our `Employee` class:

Adding a default uses the syntax `name: type = field(keyword arguments)`

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str = field(default="Dallas")

emp_1 = Employee("Scott McLean", "smclean", 53)
emp_2 = Employee("Saul Goodman", "sgoodman", 47, "Albuquerque")

print(emp_1)
print(emp_2)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=53, city='Dallas')
Employee(name='Saul Goodman', emp_id='sgoodman', age=47, city='Albuquerque')
```

As you can see, this behaves just like a default value in a function
definition.

> Warning: the default must be an immutable value, such as a string or a number.
> A mutable default, such as `field(default=[])`, raises a `ValueError`, because
> one list would be shared by every instance. Use `default_factory` instead, which
> the [field factory lesson](./12_field_factory.md) covers.

---

### Effect on `__dataclass_fields__`

Declaring a default value for the `city` field changes the field's entry in
`__dataclass_fields__`. Printing that entry shows `default='Dallas'`:

```python
print(emp_1.__dataclass_fields__["city"])
```

Output (formatted across lines for readability, and the memory address will
vary):

```
Field(
    name='city',
    type=<class 'str'>,
    default='Dallas',
    default_factory=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
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
