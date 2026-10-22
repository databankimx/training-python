## The Dataclass `kw_only` Argument

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
  File "...\09_kw_only.py", line 22, in <module>
    main()
  File "...\09_kw_only.py", line 16, in main
    emp = Employee("Scott McLean", "smclean", 54, "Dallas")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee.__init__() takes 1 positional argument but 5 were given
```

The only positional argument that `__init__()` accepts is `self`, so the five
arguments given (including `self`) are one too many.

> Note: the call is commented out in the code file, so the traceback only appears
> if you uncomment it.

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

### Defaults Can Come in Any Order

Normally, a field without a default can't come after a field with one, because
positional arguments would then be ambiguous. Keyword-only fields don't have that
restriction, since they can't be passed by position, so a field with a default can
be followed by one without:

```python
@dataclass(kw_only=True)
class Employee:
    city: str = "Dallas"
    name: str
```

---
