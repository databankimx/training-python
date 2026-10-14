## The DataClass `init` Argument

When the `init` argument is `True` (which is the default value), the DataClass generates an `__init__()` method automatically, which includes (in
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
  File "...\04_init.py", line 17, in <module>    main()
  File "...\04_init.py", line 12, in main    
    emp = Employee("Scott", "smclean", 53, "Dallas")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee() takes no arguments
```

---

### Create the `__init__()` Method

To fix this problem, we must explicitly implement the `__init__()` constructor
in the class.

This can be useful in a scenario where you want to specify a fields value based on other values rather than a function argument.

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

As you'll see when we review the [Field-Level `init`](./13_field_init.md)
setting, we could accomplish the same by leaving `init` set to `True` on the
class and controlling it at the field level.

---
