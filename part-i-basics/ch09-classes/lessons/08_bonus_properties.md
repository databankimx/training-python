## Bonus Lesson: Properties

Python provides a mechanism to create properties.

Properties differ from attributes in that properties are functions that return
a value to the developer rather than simple variables.

---

### The `@property` Decorator

In this class, we are defining two attributes: `first_name` and `last_name`

Additionally, we're implementing a method to return the full name.

When we mark the method with the `@property` decorator, we no longer need to
include the parentheses after the method name. As a property, it behaves like
an attribute and it called like this:  
`object.property`

```python
class Person(object):
    """Class to define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"
```

So, we can now treat `full_name` as though it was an attribute.

```python
someone = Person("john", "doe")
print(someone.first_name)
print(someone.last_name)
print(someone.full_name)
```

Output:

```
john
doe
John Doe
```

---

### Name Mangling to Obfuscate Attributes

Often, we don't want another developer to access attributes directly.

To make it more difficult to directly interact with attributes, we can use a
technique called *name mangling*.

To mangle an attribute name, precede it with two underscores `__attrib_name`

Then you can create properties using the non-mangled name, which encourages 
the next developer to use the property options.

```python
class Human(object):
    """Class to define a human"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the human class"""
        # first_name and last_name are attributes of the class
        self.__first_name = first_name
        self.__last_name = last_name
    
    @property
    def first_name(self):
        """Return the first name of the person"""
        return self.__first_name.title()
    
    @property
    def last_name(self):
        """Return the last name of the person"""
        return self.__last_name.title()

    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return f"{self.first_name} {self.last_name}"
```

So, with the properties in place and obfuscating the attributes, we do this:

```python
someone_else = Human("john", "doe")
print(someone_else.first_name)
print(someone_else.last_name)
print(someone_else.full_name)
```

Output:

```
John
Doe
John Doe
```

---
