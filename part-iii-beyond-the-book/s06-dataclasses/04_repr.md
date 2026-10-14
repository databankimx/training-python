## The DataClass `repr` Argument

When the `repr` argument is `True` (which is the default value), the DataClass generates a `__repr__()` method automatically, which includes (in
the order declared) all fields in the class.

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

Lacking a `__repr__()` method, we cannot print a meaningful string
representation.

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

---
