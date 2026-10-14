## Bonus Lesson: Magic (Dunder) Methods and Properties

Python exposes a number of special methods and properties. These ***magic*** 
or ***dunder*** (short for double-underscore) methods are built into Python 
classes.

So far, we have worked with one "magic" method: `__init__`

### Identifying a Type's Available Magic Methods

You can get a list of the magic methods for a given class using the following code:  
`dir(class_name)`

For example, here are the dunder methods for `int`...

```python
print(dir(int))
```

Output:

```
['__abs__', '__add__', '__and__', ..., 'real', 'to_bytes']
```

And for `str`:

```python
print(dir(str))
```

Output:

```
['__add__', '__class__', '__contains__', ..., 'upper', 'zfill']
```

Of course, any of these can be overridden in your custom classes.

---

### Some of the Common Magic Methods

Some to pay attention to include:

|Common Magic Methods||
|---|---|
|**Initialization and Construction**||
|`__new__`|Called when a class is instantiated|
|`__init__`|Constructor: called by __new__ when a class is instantiated|
|`__del__`|Destructor|
|**Numeric Methods**||
|`__trunc__(self)`|Implements behavior for `math.trunc()`|
|`__ceil__(self)`|Implements behavior for `math.ceil()`|
|`__floor__(self)`|Implements behavior for `math.floor()`|
|`__round__(self, n)`|Implements behavior for the built-in `round()`|
|`__invert__(self)`|Implements behavior for inversion using the `~` operator.|
|`__abs__(self)`|Implements behavior for the built-in `abs()`|
|`__neg__(self)`|Implements behavior for negation|
|`__pos__(self)`|Implements behavior for unary positive |
|**Arithmetic Methods**||
|`__add__(self, other)`|Implements behavior for `+`|
|`__sub__(self, other)`|Implements behavior for `-`|
|`__mul__(self, other)`|Implements behavior for `*`|
|`__floordiv__(self, other)`|Implements behavior for `\\`|
|`__div__(self, other)`|Implements behavior for `\`|
|`__truediv__(self, other)`|Implements behavior for `float` division|
|`__mod__(self, other)`|Implements behavior for `%`|
|`__divmod__(self, other)`|Implements behavior for `math.divmod()` |
|`__pow__`|Implements behavior for exponents using the ** operator.|
|`__lshift__(self, other)`|Implements left bitwise shift using the << operator.|
|`__rshift__(self, other)`|Implements right bitwise shift using the >> operator.|
|`__and__(self, other)`|Implements bitwise and using the & operator.|
|`__or__(self, other)`|Implements bitwise or using the | operator.|
|`__xor__(self, other)`|Implements bitwise xor using the ^ operator.|
|**String Methods**||
|`__str__(self)`|Defines behavior for when str() is called on an instance of your class.|
|`__repr__(self)`|Called by built-int repr() method to return a machine readable representation of a type.|
|`__unicode__(self)`|This method to return an unicode string of a type.|
|`__format__(self, formatstr)`|Return a new style of string.|
|`__hash__(self)`|   Return an integer, used for quick key comparison in dictionaries.|
|`__nonzero__(self)`|Defines behavior for when bool() is called on an instance of your class.|
|`__dir__(self)`|This method to return a list of attributes of a class.|
|`__sizeof__(self)`|Returns the size (in bytes) of the object.|
|**Comparisons**||
|`__eq__(self, other)`|Defines behavior for the equality operator, `==`|
|`__ne__(self, other)`|Defines behavior for the inequality operator, `!=`|
|`__lt__(self, other)`|Defines behavior for the less-than operator, `<`|
|`__gt__(self, other)`|Defines behavior for the greater-than operator, `>`|
|`__le__(self, other)`|Defines behavior for the less-than-or-equal-to operator, `<=`|
|`__ge__(self, other)`|Defines behavior for the greater-than-or-equal-to operator, `>=`|

---

### Overriding Magic Methods

In a class that you develop, you can redefine any magic method.

Consider this class:

```python
class Person(object):
    """Class to define a person"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Create an instance of the person class"""
        self.first_name = first_name
        self.last_name = last_name
```

As, is, if we print the class instance, we see this:

```python
someone = Person("john", "doe")
print(someone)
```

Output:

```
<__main__.Person object at 0x000001F8E6528250>
```

---

If we add a custom `__str__` method to output a string representation of a 
class instance when it's used in a `print()` call (for example)...

```python
    def __str__(self) -> str:
        """Return a string representation of the person"""
        return f"{self.first_name.title()} {self.last_name.title()}"
```

... the custom `__str__` magic method lets us do this:

```python
someone = Person("john", "doe")
print(someone)
```

Output:

```
John Doe
```

---

### Using Magic Properties

There are also dunder properties that aren't methods.

|Common Magic Properties||
|---|---|
|**Classes**||
|`__name__`|Stores class name|
|`__dict__`|Stores class attributes (see where attributes are stored)|
|`__module__`|Stores the name of the module they were defined in within|
|`__bases__`|Stores class base classes (see inheritance)|
|`__mro__`|Stores class method resolution order|
|**Functions**||
|`__name__`|Function name|
|`__dict__`|Function attributes|
|`__module__`|Name of the module they were defined in within|
|`__defaults__`|Default argument values for positional args|
|`__kwdefaults__`|Default argument values for keyword args|
|**Modules**||
|`__name__`|Module name|
|`__dict__`|Module attributes|
|`__file__`|File this module was loaded from (though some modules are missing this)|
|**All Objects**||
|`__class__`|Class of the object attribute|
|`__dict__`|Object attributes|

---

### Using `__doc__`

For example, `__doc__` returns the doc string for a method or class.

Using our same `Person` class...

```python
class Person(object):
    """Class to define a person"""
    # -- SNIP --
```

We can output the doc string like this:

```python
print(Person.__doc__)
```

Output:

```
Class to define a person
```

---

### Using `__dict__`

Or we can use `__dict__` to output a dictionary of the object attributes.

```python
print(someone.__dict__)
```

Output:

```
{'first_name': 'john', 'last_name': 'doe'}
```

---
