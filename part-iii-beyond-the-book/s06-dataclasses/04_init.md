## The Dataclass `init` Argument

When the `init` argument is `True` (which is the default value), the dataclass generates an `__init__()` method automatically, which includes (in
the order declared) all fields in the class.

Setting this to `False` will prevent that method from being generated.

---

### No `__init__()` Method

Observe this code, which results in a TypeError:

```python
@dataclass(init=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

emp = Employee("Scott", "smclean", 54, "Dallas")
```

Output:

```
Traceback (most recent call last):
  File "...\04_init.py", line 17, in <module>
    main()
  File "...\04_init.py", line 12, in main
    emp = Employee("Scott", "smclean", 54, "Dallas")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee() takes no arguments
```

> Note: this traceback comes from an earlier version of the file, without an
> `__init__()` method. The code file in this lesson has the fixed version below.

---

### Create the `__init__()` Method

To fix this problem, we must explicitly implement the `__init__()` constructor
in the class.

This can be useful in a scenario where you want to set a field's value based on other values rather than a function argument.

```python
# -- SNIP --

    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city
        self.emp_id = f"{name[0].lower()}{name.split()[-1].lower()}"

emp = Employee("Scott McLean", 54, "Dallas")
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas')
```

---

Another way to get a field's value from other values is to leave `init` set to
`True` on the class, mark the field with `field(init=False)`, and compute the
value in a `__post_init__()` method. The [post-init lesson](./17_post_init.md)
covers that approach.

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int
    city: str
    emp_id: str = field(init=False)

    def __post_init__(self) -> None:
        self.emp_id = f"{self.name[0].lower()}{self.name.split()[-1].lower()}"

emp = Employee("Scott McLean", 54, "Dallas")
print(emp)
```

Output:

```
Employee(name='Scott McLean', age=54, city='Dallas', emp_id='smclean')
```

The `init=False` field is left out of the generated `__init__()`, so it isn't passed
in. The `__post_init__()` method runs after `__init__()` and sets the field. The
field is still included in `__repr__()`, in the order it was declared.

---
