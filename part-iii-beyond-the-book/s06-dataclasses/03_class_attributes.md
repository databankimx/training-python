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

---
