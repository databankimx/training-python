## Review: A Traditional Class

Let's take a look at how we might create a class without using dataclasses.

---

### A Simple `Employee` Class

Let's imagine we are creating an `Employee` class, which will include the
following attributes:

* `name`
* `emp_id`
* `age`
* `city`

We might implement it like this:

```python
class Employee:
    """Metadata about an employee"""

    def __init__(self, name: str, emp_id: str, age: int, city: str) -> None:
        """Employee Constructor"""
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city
```

It's pretty clear that the primary function of the `Employee` class is to
carry data.

---

### Overriding Magic Methods

#### Override `__repr__()`

Without a `__repr__()` method, printing an instance shows only Python's default
form, which includes the class name and the object's memory address. So we
should implement `__repr__()` to show the data. (A `__str__()` method also works
for `print`, but if it's missing, `print` falls back to `__repr__()`.)

```python
# -- SNIP --

    def __repr__(self) -> str:
        """String representation of an employee"""
        return f"Employee (name: {self.name}, id: {self.emp_id}, " + \
            f"age: {self.age}, city: {self.city})"
```

We can then create and print an instance:

```python
emp = Employee("Scott McLean", "smclean", 53, "Dallas")
print(emp)
```

Output:

```
Employee (name: Scott McLean, id: smclean, age: 53, city: Dallas)
```

---

#### Override `__eq__()`

It's also really useful to override the `__eq__()` magic method so that we
can compare two instances based on their content as opposed to them being the
same object in memory.

```python
# -- SNIP --

    def __eq__(self, value: object) -> bool:
        """Check if two Employee objects contain the same data"""
        if not isinstance(value, Employee):
            return NotImplemented
        return (self.name, self.emp_id, self.age, self.city) == \
            (value.name, value.emp_id, value.age, value.city)
```

The `isinstance` check matters. Without it, comparing an `Employee` with a value
of another type would raise an `AttributeError`, because the method would try to
read `value.name`. Returning `NotImplemented` tells Python to try the comparison
from the other side, and if that also fails, the result is `False`.

Now we can compare two instances:

```python
# -- SNIP --

emp_1 = Employee("Scott McLean", "smclean", 53, "Dallas")
emp_2 = Employee("John Smith", "jsmith", 30, "Cleveland")
emp_3 = Employee("Scott McLean", "smclean", 53, "Dallas")

print(f"emp_1 == emp_2? {emp_1 == emp_2}")
print(f"emp_1 == emp_3? {emp_1 == emp_3}")
```

Output:

```
emp_1 == emp_2? False
emp_1 == emp_3? True
```

---

### What's Wrong with That?

The biggest problem is repetition. Each attribute has to be listed in
`__init__()`, `__repr__()`, and `__eq__()`. Adding a field means changing all
three places, and it's easy to miss one.

With four attributes, that's manageable. With twenty, the class becomes long,
and most of the code is the same pattern repeated.

As you'll soon see, dataclasses can be implemented to remove that repetition.

---
