## Accessing `__dataclass_fields__`

An instance of a DataClass exposes a description of all of its member 
fields as `__dataclass_fields__`

---

### A First Look

Let's have a look at what it contains:

```python
from dataclasses import dataclass

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott", "McLean", 53, "Dallas")
print(emp.__dataclass_fields__)
```

> Note: When actually printed out, this won't be formatted. I added carriage
> returns and indentation to make the first field more readable.

<details>
<summary>Output:</summary>
<br>

```
{
    'name': Field(
        name='name',
        type=<class 'str'>,
        default=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        default_factory=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=mappingproxy({}),
        kw_only=False,
        _field_type=_FIELD
    ),
    'emp_id': Field(
        name='emp_id',type=<class 'str'>,
        default=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        default_factory=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=mappingproxy({}),
        kw_only=False,
        _field_type=_FIELD
    ),
    'age': Field(
        name='age',
        type=<class 'int'>,
        default=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        default_factory=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=mappingproxy({}),
        kw_only=False
        ,_field_type=_FIELD
    ),
    'city': Field(
        name='city',
        type=<class 'str'>,
        default=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        default_factory=<dataclasses._MISSING_TYPE object at 0x00000179393A5050>,
        init=True,
        repr=True,
        hash=None,
        compare=True,
        metadata=mappingproxy({}),
        kw_only=False,
        _field_type=_FIELD
    )
}
```

</details>

---

### What Does All That Mean?

In each field, you will see the following settings (we'll learn to control
these later in the lesson):

|Name|Meaning|
|-|-|
|`name`|Name of the field (declared in the class)|
|`type`|Data type of the field (per the type hint in the declaration)|
|`default`|Specifies the default value for the field|
|`default_factory`|Function that returns the default value for the field|
|`init`|If `True`, the field is included in the generated `__init__` method|
|`repr`|If `True`, the field is included in the generated `__repr__` method|
|`hash`|If `True`, the field is included in the generated `__hash__` method|
|`compare`|If `True`, field is included in `__eq__`  and `__gt__` methods|
|`metadata`|Dictionary (or None) defining additional data about the field|
|`kw_only`|If `True`, the field can only be a keyword argument in `__init__`|
|`_field_type`|The type of field implemented. In this lesson all are `_FIELD`|

We'll cover the usage of each of these (with the exception of `_field_type`) 
in separate lessons to follow.

---
