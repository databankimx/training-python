## Review: A Traditional Class

Let's take a look at how we might create a class without using DaatClasses.

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

Since there is no way to print a class instance meaningfully, we should probably implement either a `__str__()` or `__repr__()` method.

```python
# -- SNIP --

    def __repr__(self) -> str:
        """String representation of an employee"""
        return f"Employee (name: {self.name}, id: {self.emp_id}, " + \
            f"age: {self.age}, city: {self.city})"
```

We can then create and print an instance:

```python
emp = Employee("Scott", "smclean", 53, "Dallas")
print(emp)
```

Output:

```
Employee (name: Scott, id: smclean, age: 53, city: Dallas)
```

---

#### Override `__eq__()`

It's also really useful to override the `__eq__()` magic method so that we
can compare two instances based on their content as opposed to them being the
same object in memory.

```python
# -- SNIP --

    def __eq__(self, value: object) -> bool:
        return (self.name, self.emp_id, self.age, self.city) == \
            (value.name, value.emp_id, value.age, value.city)
```

Now we can compare two instances:

```python
# -- SNIP --

emp_1 = Employee("Scott", "smclean", 53, "Dallas")
emp_2 = Employee("John", "Smith", 30, "Cleveland")
emp_3 = Employee("Scott", "smclean", 53, "Dallas")

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

In the above code, the biggest problem lies in passing the argument in 
`__init__`, `__repr__`, and `__eq__`.

Each time it has to copy its properties and return the object. It is a good 
way of dealing with a small amounts of data, but suppose we have work with 
large data. It makes your code more complicated.

As you'll soon see, DataClasses can be implemented to simplify coding.

---
