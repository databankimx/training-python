## Creating and Using a Class

In programming, there are three different overall design philosophies:

* **Procedural Programming**:
    * In the *procedural* design pattern, data is decoupled from the
      functions that operate on it.
    * Functions are agnostic to the source of the data and are not modeled for
      specific use cases.
    * Functions are typically implemented using iterative patterns like loops.
* **Functional Programming**:
    * In the *functional* design pattern, data and its structure is taken into
      account when the functions are designed.
    * But the data itself remains separate from the functions.
    * Functions are often designed using recursion and/or composition patterns
* **Object-Oriented Programming**:
    * In *object-oriented* programming, data is modeled into logically
      constructed objects that group related data and functionality together.
    * Functions are developed within the data model and exist as part of the
      object.
    * So the actual data is coupled directly to the functions that perform
      work on it.

While each of these has advantages and limitations, many programmers find
object-oriented code easier to read and maintain, because the models for things
you are working with contain both the data and the functions.

Models like this are called *classes* in Python. A class represents a
conceptual thing and encapsulates its attributes and functions.

---

### Class Declaration

Classes in Python are declared with the `class` keyword and differ from
variables and functions in naming. Instead of `snake_case`, classes should be
named in `PascalCase`.

```python
class MyClass:
    # Implementation
```

By convention, a capitalized name refers to a class, and a lowercase name refers
to an instance of a class. You'll see both in this chapter, so keep an eye on
which is which.

---

### Class Initializers

In many languages, classes include a concept of a *constructor*, which is a
function built to allow the developer to create an instance of the class and
populate its member properties.

In Python, we have a special function named `__init__` that should be implemented
in order to create and initialize class instances. The name has two underscores
on each side. That's not decoration. Python looks for exactly that name to know
which method to run when an instance is created. If you use only one underscore on
each side, the method won't be called automatically, and the resulting error can
be hard to track down.

The `__init__` function must take a special parameter `self` (which references
the instance itself) as its first argument and can accept any other parameters
the developer wishes to include. You don't pass `self` yourself. Python passes it
for you every time a method is called on an instance.

Within the `__init__` function, any attributes usable in class functions or
accessible in the calling code should be populated in the form
`self.var_name = value`. The `self.var` format means that the variable is a
member of the class, not just of the `__init__` function. Variables that are
accessible through an instance like this are called *attributes*.

### A Simple Class

With that preamble, we can now create a simple class modeling a dog.

```python
class Dog:
    """This is a simple model for a dog"""

    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        self.name = name.title()
        self.age = age
```

We now have a simple class `Dog` that has two attributes: `name` and `age`.

---

### Creating a Class Instance

To create an instance of a class, we call the class name as though it were a
function. Python knows to run `__init__` when this happens, and we pass the
values the `__init__` function expects, minus `self`.

Making an object from a class is called *instantiation*, and the object itself is
an *instance* of the class. Think of the class as a set of instructions for
building instances. The `Dog` class tells Python how to build a dog, and each
instance is one specific dog.

```python
my_dog = Dog("fido", 6)
```

---

### Accessing Object Attributes

Then, to access any of the attributes of the new object, we use
`object_name.attribute_name`.

```python
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

Output:

```
My dog's name is Fido.
My dog is 6 years old.
```

---

### Adding Methods to a Class

While grouping related attributes together is useful, if that is the only
reason for creating a class, we have to ask if we're really accomplishing
something for which we couldn't have just used a dictionary.

But classes have another capability. We can create functions that are part of
the class and are designed specifically to work with the data model in the
class.

Functions in a class that act on class instances are called methods. They work
just like regular functions, with one difference: they require `self` as the
first parameter, so they can reach the instance's attributes.

Here's what our class looks like with a couple of instance methods added.

```python
class Dog:
    """This is a simple model for a dog"""

    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Tell the Dog to sit"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Tell the Dog to roll over"""
        print(f"{self.name} has rolled over.")
```

---

### Calling Instance Methods

Instance methods are called in the form `object_name.method_name()`

```python
my_dog = Dog("fido", 6)
my_dog.sit()
my_dog.roll_over()
```

Output:

```
Fido is now sitting.
Fido has rolled over.
```

---

### Class Methods

Sometimes you want a method that works on the class itself, not on one
instance. Those are *class methods*. They take `cls` instead of `self`, and you
mark them with the `@classmethod` decorator. Python will pass the class in as
the first argument, the same way it passes the instance for `self`.

```python
class Dog:
    """This is a simple model for a dog"""

    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        self.name = name.title()
        self.age = age

    @classmethod
    def from_string(cls, text):
        """Create a Dog from a 'name,age' string"""
        name, age = text.split(",")
        return cls(name, int(age))
```

Class methods are useful when you need to create an instance in a different way.
Here, `from_string()` takes a string, splits it apart, and passes the pieces to
the constructor through `cls`. Since `cls` refers to `Dog`, the method calls the
same `__init__()` you'd call yourself.

```python
my_dog = Dog.from_string("fido,6")
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

Output:

```
My dog's name is Fido.
My dog is 6 years old.
```

Notice that we called the method on the class, not on an instance. That's the
big difference from instance methods. You can't call `from_string()` on a dog you
already have, because you're using it to make the dog in the first place. You'll
see the `cls` and `@classmethod` pattern in other people's code, so it's worth
recognizing them now.

---

### Working With Multiple Instances

Of course, it's possible to have multiple instances of a class at the same
time. This is a fundamental characteristic of object-oriented programming,
since each instance carries its own data.

Each instance is separate, even if two of them have the same values. Two dogs
of the same age are still two dogs. To keep track of them, give each instance
its own variable name, or put it in a list or dictionary.

```python
my_dog = Dog("rover", 6)
your_dog = Dog("lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
```

Output:

```
My dog's name is Rover.
My dog is 6 years old.
Rover is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy has rolled over.
```

---
