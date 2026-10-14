## The `default` Field Attribute

Using the `default` attribute on any field allows you to set the default value
for that field if it is omitted from the call to create a new class instance.

> Note: Just like regular functions, `default` (optional) attributes must
> occur at the end of the call.
>
> In a DataClass, this means they must be declared last in order in the class
> itself.

---

### Example Code

Here's an example of a default value for our `Employee` class:

Adding attributes uses the syntax `name: type = field(kw_attributes)`

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str = field(default="Dallas")

emp_1 = Employee("Scott", "smclean", 53)
emp_2 = Employee("Saul", "sgoodman", 47, "Albuquerque")

print(emp_1)
print(emp_2)
```

Output:

```
Employee(name='Scott', age=54, emp_id='smclean', city='Dallas')     
Employee(name='Saul', age=47, emp_id='sgoodman', city='Albuquerque')
```

As you can see, this behaves just like a default value in a function
definition.

---

### Effect on `__dataclass_fields__`

Having declared a default value for the `city` field will change the output 
of the `__dataclass_fields__` object as well...

```
...
Field(
    name='city',
    type=<class 'str'>,
    default='Dallas',
    ...
)
...
```

---
