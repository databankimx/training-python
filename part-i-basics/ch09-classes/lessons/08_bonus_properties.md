## Bonus Lesson: Properties

Python provides a mechanism to create properties.

Properties differ from attributes in that a property is a method that returns a
value to the developer, and it's used like a simple variable.

---

### The `@property` Decorator

In this class, we are defining two attributes: `first_name` and `last_name`.

Additionally, we're implementing a method to return the full name.

When we mark the method with the `@property` decorator, we no longer need to
include the parentheses after the method name. As a property, it behaves like
an attribute, and it's called like this:  
`object.property`

```python
class Person:
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

So, we can now treat `full_name` as though it were an attribute.

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

The code file clears the terminal and pauses between the two examples, so you
can read the first output before the second one starts.

---

### Hiding Attributes with Name Mangling

Often, we don't want another developer to access attributes directly.

To make it more difficult to interact with attributes directly, we can use a
technique called *name mangling*.

To mangle an attribute name, precede it with two underscores, like `__first_name`.
When Python sees one of these names inside a class, it renames the attribute
internally by adding the class name in front. So `__first_name` inside `Human`
becomes `_Human__first_name`.

Then you can create properties using the non-mangled name, which nudges the
next developer toward the property instead of the raw attribute.

```python
class Human:
    """Class to define a human"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the human class"""
        # first_name and last_name are attributes of the class
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        """Return the first name of the person"""
        return self.__first_name.title()

    @property
    def last_name(self) -> str:
        """Return the last name of the person"""
        return self.__last_name.title()

    @property
    def full_name(self) -> str:
        """Return the full name of the person"""
        return f"{self.first_name} {self.last_name}"
```

So, with the properties in place and the attributes hidden, we do this:

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

Name mangling is not security. Python renamed the attribute, but it didn't lock
it. Anyone who knows the mangled name can still reach the raw value:

```python
print(someone_else._Human__first_name)
```

Output:

```
john
```

Hiding data like this, and offering controlled access through methods or
properties, is called *encapsulation*. It's one of the core ideas of
object-oriented programming, and you'll see it in a lot of code.

The code file turns off Pylint's `too-few-public-methods` warning for `Person`,
since that class has only a constructor and one property. That comment stays in
the code file.

---
