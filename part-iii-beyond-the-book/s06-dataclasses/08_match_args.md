## The Dataclass `match_args` Argument

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

This tuple is what lets a `match` statement use positional patterns with the
class. The example below uses a second class, `MatchEmployee`, with the default
setting, so the code file has both. The patterns match on the first argument, the
name, and then bind the remaining fields to variables:

```python
match_emp = MatchEmployee("Scott McLean", "smclean", 54, "Dallas")

match match_emp:
    case MatchEmployee("Scott McLean", emp_id, age, city):
        print(f"Found Scott: {emp_id}, age {age}, {city}")
```

Output:

```
Found Scott: smclean, age 54, Dallas
```

The class name in the pattern checks the type, and each position in the pattern
is matched against the field listed at the same position in `__match_args__`.

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
  File "...\08_match_args.py", line 12, in <module>
    print(emp.__match_args__)
          ^^^^^^^^^^^^^^^^^^
AttributeError: 'Employee' object has no attribute '__match_args__'
```

> Note: this traceback comes from a standalone version of the file. The code file
> has the `match_args=False` class, with its loop commented out, and the `match`
> example uses a second class with the default setting.

---
