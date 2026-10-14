## The DataClass `kw_only` Argument

When `kw_only` is `True` (default is `False`), all arguments in the 
`__init__()` method can only be passed as keyword arguments.

---

### No Positional Arguments in Constructor

Consider this code:

```python
from dataclasses import dataclass

@dataclass(kw_only=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott McLean", "smclean", 54, "Dallas")
```

Output:

```
Traceback (most recent call last):
  File "...\09_kw_only.py", line 19, in <module>
    main()
  File "...\09_kw_only.py", line 13, in main
    emp = Employee("Scott McLean", "smclean", 54, "Dallas")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee.__init__() takes 1 positional argument but 5 were given
```

Obviously, the one expected positional argument is `self`.

---

### Passing Keyword Arguments Instead

We must pass our constructor arguments as keywords:

```python
from dataclasses import dataclass

@dataclass(kw_only=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee(name="Scott McLean", emp_id="smclean", age=54, city="Dallas")
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas')
```

---
