## The Dataclass `frozen` Argument

When the `frozen` argument is set to `True` (default is `False`), code cannot 
assign values to instance fields.

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
  File "...\07_frozen.py", line 23, in <module>
    main()
  File "...\07_frozen.py", line 19, in main
    emp.age = 54
    ^^^^^^^
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'age'
```

> Note: the assignment is commented out in the code file, so the traceback only
> appears if you uncomment it.

---

### Frozen Is Shallow

`frozen` only blocks assigning to the fields themselves. If a field holds a
mutable object, such as a list, the object's contents can still change:

```python
@dataclass(frozen=True)
class Team:
    name: str
    members: list[str]

team = Team("Support", ["Scott"])
team.members.append("John")
```

`team.name = "Sales"` would raise a `FrozenInstanceError`, but the append
succeeds, because the list object itself was never reassigned.

---

### Frozen Instances Can Be Hashed

With `frozen=True` and the default `eq=True`, the dataclass also generates a
`__hash__()` method, so its instances can be used as dictionary keys and in sets.

This is the case that `unsafe_hash` covered in the attributes lesson. A frozen
instance can't change, so its hash can't go out of date, which is why no
`unsafe_hash` is needed. The dataclass lesson on `eq` explains what happens to
the hash when `eq` is set to `False`.

---
