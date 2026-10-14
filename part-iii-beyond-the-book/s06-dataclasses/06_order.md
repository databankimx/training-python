## The DataClass `order` Argument

When the `order` argument is `True` (default value is `False`), the DataClass 
generates an the following methods automatically

* `__gt__()`
* `__ge__()`
* `__lt__()`
* `__le__()`

These compare all fields in the class (in the order declared) between two
objects.

Be careful with using this. Since the comparisons take place across all 
elements, the results may be difficult to predict.

---

### Added Comparison Methods

Consider this code:

```python
from dataclasses import dataclass

@dataclass(order=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp_1 = Employee("Scott McLean", "smclean", 54, "Dallas")
emp_2 = Employee("Saul Goodman", "sgoodman", 57, "Albuquerque")
emp_3 = Employee("Scott McLean", "smclean", 54, "Dallas")

print(f"emp_1 > emp_2: {emp_1 > emp_2}")
print(f"emp_1 < emp_3: {emp_1 < emp_3}")
print(f"emp_1 <= emp_3: {emp_1 <= emp_3}")
```

Output:

```
emp_1 > emp_2: True
emp_1 < emp_3: False
emp_1 <= emp_3: True
```

> Notice how `emp_1 > emp_2` returns true, even though `emp_2` has a larger
> value for `age`. This is because before it gets to `age`, `__gt__()` has
> already identified that `'Scott McLean'` is larger (alphabetically) than
> `'Saul Goodman'`.

---
