## Class Inheritance

One of the more powerful features of classes is inheritance. Inheritance works
in two basic ways:

* You can take an existing class and add functionality to it.
* You can create a generic class with attributes that apply to many more
  specific classes, and then inherit that common code in each of those classes.

When using inheritance, you have two class types:

* Parent Class (also called Superclass)
    * This is the class containing common attributes and methods
* Child Class (also called Subclass)
    * This class inherits all of the attributes and methods of the parent class,
      and adds attributes and methods purpose built for its more specific model

---

### The Parent Class

A parent class (or superclass) is a generic class that includes attributes
applicable to a group of classes.

For example, we might have our existing `Car` class:

<details>
<summary>The Car Class</summary>

```python
class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, mileage):
        """Set the odometer mileage"""
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles=1):
        """Increment the odometer mileage"""
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")
```

</details>

This class currently implements attributes that are applicable to any type of
car:

* make
* model
* year
* odometer_reading

---

### Creating a Child Class

However, there could be other, more specific types of cars. For example, an
electric car might have attributes related to its battery, which would not
be applicable to other subclasses of `Car`.

For this, we can use inheritance so that we don't have to re-code all of the
characteristics of the parent class.

When defining a child class, add the name of the parent class in parentheses
following the child class name:

```python
class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""
    # Implementation
```

The parent class has to be available when Python reads the child class. That
means the parent must either be defined earlier in the same file, or imported at
the top of the file. If both classes are in one file, put the parent first. If
the parent lives in another module, import it. You'll see how to do that later
in this chapter.

---

### Adding `__init__()` in a Child Class

The `__init__()` function behaves the same way in a child class as it did in
the parent.

And, while we could set each attribute individually, that would be redundant.
The parent class already has its own `__init__()` function where the common
attributes are set.

For this, Python provides the `super()` function. It gives the child class
access to the parent's methods, including its `__init__()`, so we can pass the
arguments along instead of repeating them.

```python
    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery_size = 75
```

We've added one attribute that only child class instances have: `battery_size`.

The names come from a convention. The parent is the *superclass*, and the child is
the *subclass*. `super()` is the way the subclass reaches up to its superclass.

---

### Adding Methods in a Child Class

Methods are added the same way they are in any class.

Let's add a method to interact with the `battery_size` attribute.

```python
    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
```

Now we have a complete (albeit simple) child class inheriting from `Car`.

<details>
<summary>The ElectricCar Class</summary>

```python
class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
```

</details>

---

### Where Shared Code Belongs

Any attribute or method that could apply to any car belongs in `Car`, not in
`ElectricCar`. Every child class gets it for free, and `ElectricCar` only
contains code that's specific to electric cars.

For example, `get_descriptive_name()` works for a gas car and an electric car,
so it stays in `Car`. `describe_battery()` only makes sense for an electric car,
so it goes in `ElectricCar`.

---

### Creating and Using a Child Class Object

Now we can create an instance of the child class. This object has all of
the attributes and methods of the parent class, as well as its own.

```python
my_e_car = ElectricCar("nissan", "leaf", 2024)
print()
print(my_e_car.get_descriptive_name())
my_e_car.describe_battery()
```

Output:

```

2024 Nissan Leaf
This car has a 75-kWh battery.
```

---

### Inheritance Is a One-Way Street

It's important to note that inheritance does not make child class attributes or
methods available to the parent class.

This code raises an `AttributeError`, because the `describe_battery()` method
is not available from the parent class `Car`.

```python
my_gas_car = Car("ford", "thunderbird", 1978)
my_gas_car.describe_battery()
```

Output:

```
Traceback (most recent call last):
  File "...\03_class_inheritance.py", line 67, in <module>
    my_gas_car.describe_battery()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Car' object has no attribute 'describe_battery'
```

The code file has this line commented out, so the rest of the file can run.
Uncomment it to see the error for yourself.

---
