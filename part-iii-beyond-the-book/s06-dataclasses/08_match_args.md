## The DataClass `match_args` Argument

When the `match_args` argument is `True` (which is the default), the class
will generate a tuple called `__match_args__` that contains the names of all
arguments in the generated `__init__()` method.

---

### With `match_args`

Consider this code:

```python
from dataclasses import dataclass

@dataclass()
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp.__match_args__)
```

Output:

```
('name', 'emp_id', 'age', 'city')
```

In the default state, the `__match_args__` tuple exists.

---

### No `__match_args__`
Consider this code:

```python
from dataclasses import dataclass

@dataclass(match_args=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
print(emp.__match_args__)
```

Output:

```
Traceback (most recent call last):
  File "...\08_match_args.py", line 16, in <module>
    main()
  File "...\08_match_args.py", line 13, in main
    print(emp.__match_args__)
          ^^^^^^^^^^^^^^^^^^
AttributeError: 'Employee' object has no attribute '__match_args__'
```

---
