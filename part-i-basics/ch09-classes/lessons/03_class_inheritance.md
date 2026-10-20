## Class Inheritance

One of the more powerful features of classes is inheritance.

The basic concept of inheritance is that

* You can take an existing class and add additional functionality to it  
  or
* You can create a generic class with attributes that apply to many more 
  specific classes and then inherit that common code in each of the classes.

When using inheritance, you have two class types:

* Parent Class (also called Superclass)
    * This is the class containing common attributes and methods
* Child Class (also called Subclass)
    * This class inherits all of the properties of the parent class and adds
      attributes and methods purpose built for its more specific model

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
        print(f"This car has {self.odometer_reading} miles on it.\n")

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

However, there could be other, more specific types of cars. For example, ane
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

---

### Adding `__init__()` in a Child Class

The `__init__()` function behaves the same way in a child class as it did in
the parent.

And, while we could set each attribute individually, that would be redundant.
The parent class already has its own `__init__()` function where the common
attributes are set.

For this, Python provides the `super()` function, which returns the parent
class and allows us to call its initializer with the arguments passed to the
child class.

```python
    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery_size = 75
```

We've added one attribute only accessible in the child class: `battery_size`

---

### Adding Methods in a Child Class

Methods are added identically to the structure for any class.

Let's add a method to interact with the `battery_size` attribute.

```python
    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
```

Now, we have a complete (albeit simple) child class inheriting from `Car`

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

### Creating and Using a Child Class Object

Now we can create an instance of the child class. This object will have all of
the attributes and functionality of the parent class as well as its own.

```python
my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
my_e_car.describe_battery()
```

Output:

```
2024 Nissan Leaf
This car has a 75-kWh battery.
```

---

### Inheritance is a One-Way Street

It's important to note that inheritance does not make child class attributes or
functions available to the parent class.

This code will result in an AttributeError, because the `describe_battery()`
method is not available from the parent class `Car`.

```python
my_gas_car = Car("ford", "thunderbird", 1978)
my_gas_car.describe_battery()
```

Output:

```
Traceback (most recent call last):
  File "...\03_class_inheritance.py", line 62, in <module>
    my_gas_car.describe_battery()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Car' object has no attribute 'describe_battery'
```

---
