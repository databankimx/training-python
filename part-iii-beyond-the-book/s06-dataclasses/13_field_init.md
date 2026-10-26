## The `init` Field Attribute

The `init` attribute is a boolean value that indicates whether or not the
field should be included in the `__init__()` constructor. By default, the
value is `True` (as you've already seen, all fields are in the constructor by 
default), so this attribute should only be specified when it will be `False` 
(to remove the field from the constructor).

---

### Example Code

Here's an example where we set the `init` value in our `Employee` class:

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    emp_id: str
    city: str = field(init=False, default="Dallas")

def main() -> None:
    emp = Employee("Scott McLean", 53, "smclean")
    print(emp)

if __name__ == "__main__":
    main()
```

Output:

```
Employee(name='Scott McLean', age=53, emp_id='smclean', city='Dallas')
```

---

### We Can't Override This Setting

Unlike what we saw previously with the defaults, we cannot specify a value
for `city` in the constructor now.

This code would result in an error:

```python
# -- SNIP --

emp_2 = Employee("Saul Goodman", 47, "sgoodman", "Albuquerque")
```

Output:

```
Traceback (most recent call last):
  File "...\13_field_init.py", line 29, in <module>
    main()
  File "...\13_field_init.py", line 22, in main
    emp_2 = Employee("Saul Goodman", 47, "sgoodman", "Albuquerque")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee.__init__() takes 4 positional arguments but 5 were given
```

> Note: this call is commented out in the code file. Uncomment it to see the
> error above.

---

### We Can Still Change the Value Though

Of course, just because we can't include the value in the constructor does not
mean that we're stuck with the default value.

We can still do something like this:

```python
# -- SNIP --

emp_2 = Employee("Saul Goodman", 47, "sgoodman")
emp_2.city = "Albuquerque"
print(emp_2)
```

Output:

```
Employee(name='Saul Goodman', age=47, emp_id='sgoodman', city='Albuquerque')
```

---

### Effect on `__dataclass_fields__`

Like the other field settings, setting the `init` attribute on a field affects
the `__dataclass_fields__` entry for that field. Printing it:

```python
print(emp.__dataclass_fields__["city"])
```

Output (formatted across lines for readability, and the memory address will
vary):

```
Field(
    name='city',
    type=<class 'str'>,
    default='Dallas',
    default_factory=<dataclasses._MISSING_TYPE object at 0x0000013E2E2455D0>,
    init=False,
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
