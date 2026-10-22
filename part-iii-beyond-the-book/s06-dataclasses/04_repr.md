## The Dataclass `repr` Argument

When the `repr` argument is `True` (which is the default value), the dataclass
generates a `__repr__()` method automatically, which includes (in the order
declared) all fields in the class.

Setting this to `False` will prevent that method from being generated.

---

### No `__repr__()` Method

Observe this code:

```python
from dataclasses import dataclass

@dataclass(repr=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp)
```

Output:

```
<__main__.Employee object at 0x000001DE68E3FAD0>
```

Without a `__repr__()` method, Python falls back to its default form, which shows
the class name and memory address, but not the field values.

---

### Create the `__repr__()` Method

To fix this problem, we must explicitly implement the `__repr__()` method
in the class.

```python
# -- SNIP --

    def __repr__(self) -> str:
        return f"Employee (name: {self.name}, id: {self.emp_id}, " + \
            f"age: {self.age}, city: {self.city})"

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp)
```

Output:

```
Employee (name: Scott McLean, id: smclean, age: 54, city: Dallas)
```

> Note: you can also leave `repr` set to `True` and write `__repr__()` yourself.
> The generated method isn't added to a class that already defines one, so your
> version is the one that runs.

---
