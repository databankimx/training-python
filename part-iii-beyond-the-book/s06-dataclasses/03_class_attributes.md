## DataClass Attributes

You can specify attributes of the class as arguments to the decorator:
`@dataclass(kw_arguments)`

The following attributes are supported:

|Name|Meaning|
|-|-|
|`init`|If `True` (default), generates `__init__()`|
|`repr`|If `True` (default), generates `__repr__()`|
|`eq`|If `True` (default), generates `__eq__()`|
|`order`|If `True` generates `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`, |
|`unsafe_hash`|If `False`, generates `__hash__()` based on `eq` and `frozen`|
|`frozen`|If `True` assigning to fields raises an exception|
|`match_args`|If `True` generates `__match_args__` tuple from `__init__()`|
|`kw_only`|If `True` all fields will be `kw_only` in `__init__()`|
|`slots`|If `True`, generates `__slots__` attribute|
|`weakref_slot`|If it and `slots` are `True`, adds a slot named `__weakref__`|

> Note: For the settings that determine if magic methods are auto-generated
> (`init`, `repr`, etc.), If you implement the associated magic method in the 
> class explicitly, the class attribute will be ignored.

I will cover most of these settings in following lessons

### Trying Three of the Settings

The script [03_class_attributes.py](./03_class_attributes.py) uses `slots`,
`unsafe_hash`, and the default `repr` in a short example:

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Employee:
    name: str
    emp_id: str

@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int
```

* `slots=True` stores the attributes in a fixed set of slots instead of a
  per-object dictionary. This means that a new attribute cannot be added to
  the instance.
* `unsafe_hash=True` generates `__hash__()`, so the instance can be used as a
  dictionary key or in a set, even though it is mutable.

Output:

```
Employee(name='Scott McLean', emp_id='smclean')
Cannot add a new attribute to a slotted class
Point hash is an integer? True
```

---
