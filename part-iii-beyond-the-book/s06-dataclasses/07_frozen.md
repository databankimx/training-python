## The DataClass `frozen` Argument

When the `frozen` argument is set to `True` (default is `False`), code cannot 
assign values to instance members.

---

### Blocked From Setting Values

Consider this code:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott McLean", "smclean", 53, "Dallas")
emp.age = 54
```

Output:

```
Traceback (most recent call last):
  File "...\07_frozen.py", line 18, in <module>
    main()
  File "...\07_frozen.py", line 14, in main
    emp.age = 54
    ^^^^^^^
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'age'
```

---
