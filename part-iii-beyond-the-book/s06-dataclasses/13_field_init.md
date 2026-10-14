## The `init` Field Attribute

The `init` attribute is a boolean value that indicates whether or not the
field should be included in the `__init__()` constructor. By default, the
value is `True` (as you've already seen, all fields are in the constructor by 
default), so this attribute should only be specified when it will be `False` 
(to remove the field from the constructor).

---

### Example Code

Here's an example where we set the `init` value in our `Employee` class:

```python
from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    emp_id: str
    city: str = field(init=False, default="Dallas")

def main() -> None:
    emp = Employee("Scott", "smclean", 53)
    print(emp)

if __name__ == "__main__":
    main()
```

Output:

```
Employee(name='Scott', age='smclean', emp_id=53, city='Dallas')
```

---

### We Can't Override This Setting

Unlike what we saw previously with the defaults, we cannot specify a value
for `city` in the constructor now.

This code would result in an error:

```python
# -- SNIP --

emp_2 = Employee("Saul", "sgoodman", 47, "Albuquerque")
```

Output:

```
Traceback (most recent call last):
  File "...\06_init.py", line 19, in <module>
    main()
  File "...\06_init.py", line 16, in main
    emp_2 = Employee("Saul", "sgoodman", 47, "Albuquerque")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Employee.__init__() takes 4 positional arguments but 5 were given
```

---

### We Can Still Change the Value Though

Of course, just because we can't include the value in the constructor does not mean that we're stuck with the default value.

We can still do something like this:

```python
# -- SNIP --

emp_2 = Employee("Saul", "sgoodman", 47)
emp_2.city = "Albuquerque"
print(emp_2)
```

Output:

```
Employee(name='Saul', age='sgoodman', emp_id=47, city='Albuquerque')
```

---

### Effect on `__dataclass_fields__`

Like the other field settings, setting the `init` attribute on a field 
affects the `__dataclass_fields__`

```
...
Field(
    name='city',
    type=<class 'str'>,
    default='Dallas',
    ...
    init=False,
    ...
)
...
```

---
