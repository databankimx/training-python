## Inheritance with DataClasses

Inheritance with DataClasses is basically the same as class inheritance
anywhere else in Python:  
`class ClassName(ParentClass):`

The main difference is that there is no need to explicitly call the 
`super()` function and the parent class `__init__()` method when instantiating
a child class object. DataClasses take care of that for us in the generated
`__init__()` function.

---

Consider this example:

```python
from dataclasses import dataclass, field

@dataclass()
class Staff:
    """Metadata about a staff member"""
    name: str
    emp_id: str
    age: int
    city: str

@dataclass
class Employee(Staff):
    """Metadata about an employee"""
    salary: int

emp = Employee("Scott McLean", "smclean", 54, "Dallas", 50_000)
print(emp)
```

Output:

```
Employee(name='Scott McLean', emp_id='smclean', age=54, city='Dallas', salary=50000)
```

---
