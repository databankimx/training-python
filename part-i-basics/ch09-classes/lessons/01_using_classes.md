## Creating and Using a Class

In development, there are three different overall design philosophies:

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

While each of these has advantages and limitations, object-oriented code is
often easier to read and maintain, because the models for things you are 
working with contain both the data and the functions.

Objects like this are called *classes* in Python

A class represents a conceptual thing and encapsulates its attributes and 
functions.

---

### Class Declaration

Classes in Python are declared with the `class` keyword and differ from
variables and functions in naming. Instead of `snake_case`, classes should be
named in `PascalCase`

```python
class MyClass:
    # Implementation
```

---

### Class Initializers

In many languages, classes include a concept of a *constructor*, which is a
function built to allow the developer to create an instance of the class and
populate its member properties.

In Python, we have a special function name `__init__` that must be implemented 
in order to create and initialize class instance objects.

The `__init__` function must take a special parameter `self` (which references
the instance itself) as its first argument and can accept any other parameters
the developer wishes to include.

Within the `__init__` function, any properties usable in class functions or
accessible in the calling code must be populated in the form
`self.var_name = value`. The `self.var` format means that the variable is a 
member of the class, not just of the `__init__` function.

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

We now have a simple class `Dog` that has two properties: `name` and `age`.

---

### Creating a Class Instance

To create an instance of a class, we call the class name as though it were a
function (Python knows to execute `__init__` when this occurs) and pass 
whatever properties are available in the `__init__` function.

```python
my_dog = Dog("fido", 6)
```

---

### Accessing Object Properties

Then, to access any of the properties of the new object, we use
`object_name.property_name`

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

While grouping related properties together is useful, if that is the only
reason for creating a class, we have to ask if we're really accomplishing
something for which we couldn't have just used a dictionary.

But classes have another capability. We can create functions that are part of 
the class and are designed specifically to work with the data model in the 
class.

Functions in a class that act on class instance objects are called methods.
These are implemented just like regular classes, except that in order to act on the object, they also require `self` as the first parameter.

There are also *class methods* that act on the class instead of an instance.
These methods will be covered later, but it's useful to point out that the 
main difference between instance methods and class methods is that class 
methods do not use the `self` parameter.

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

### Working With Multiple Instances

Of course, it's possible to have multiple instances of a class at the same
time. This is a fundamental characteristic of object-oriented programming,
since each instance carries its own data.

```python
my_dog = Dog("rover", 6)
your_dog = Dog("lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
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


---
