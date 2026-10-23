## Working with Attributes

Classes are good at carrying related data. Controlling that data is where they
really earn their keep.

---

### Default Attributes

Python lets you set attributes that aren't passed into the `__init__` function.
Give them a default value, and every instance starts out with it.

This is useful when there is a known starting value for a given attribute. For
example, a new automobile has zero miles on the odometer.

Here is a simple class modeling a car:

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
```

Note that the `odometer_reading` attribute is not passed to the constructor.
Instead, it is automatically initialized to zero.

We've also added a method, `read_odometer()`, that accesses the
`odometer_reading` attribute for us.

---

### Interacting with Attributes

Even though we don't set `odometer_reading` in the calling code, it is
initialized as an attribute of `self` in the `__init__` method, so it is
accessible like any other attribute.

```python
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
# Access `odometer_reading` either directly or via the method that reads it
my_new_car.read_odometer()
print()
print(my_new_car.odometer_reading)
```

Output:

```
2014 Dodge Challenger
This car has 0 miles on it.

0
```

---

### Modifying Attributes

Python doesn't hide attributes, so anyone can reach them directly. However, you
get more control over your program's behavior if you create dedicated methods
that handle changes to an attribute, rather than leaving every developer to
manage those changes on their own.

Here is an expanded version of our car class with methods added to modify the
`odometer_reading` attribute:

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

We can create a new instance just like we did previously:

```python
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()
```

Output:

```
2014 Dodge Challenger
This car has 0 miles on it.

```

---

### Modifying Attributes Directly

Of course, you can modify the attributes of a class instance directly.

```python
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.odometer_reading = 15_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading = -1_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading += 2_000
my_new_car.read_odometer()
print()

my_new_car.odometer_reading -= 1_001
my_new_car.read_odometer()
print()
```

Output:

```
This car has 0 miles on it.

This car has 15000 miles on it.

This car has -1000 miles on it.

This car has 1000 miles on it.

This car has -1 miles on it.

```

That worked exactly as expected, but:

* This technique forces the developer to keep track of the value in the
  calling code.
* And it requires the developer to understand the rules of the model.
    * This is a car, so it should not permit a negative odometer reading.

---

### Using the Attribute-Modifying Methods

That's why it's considered a best practice to create methods that modify the
attributes according to rules you establish when creating the class.

---

#### The `set_odometer()` Method

By creating a method to set the odometer, we prevent the issue we had
previously, where a negative value could be set.

```python
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.set_odometer(14_000)
my_new_car.read_odometer()
print()

my_new_car.set_odometer(-1_000)
my_new_car.read_odometer()
print()
```

Output:

```
This car has 0 miles on it.

Setting odometer to 14000
This car has 14000 miles on it.

You can't roll back an odometer!
This car has 14000 miles on it.

```

Attempting to set `-1_000` on the odometer was not permitted.

---

#### The `increment_odometer()` Method

Having a method to increment the odometer, either by `1` (the default) or by a
specified amount, again keeps control of the behavior.

```python
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()
print()

my_new_car.increment_odometer()
my_new_car.read_odometer()
print()

my_new_car.increment_odometer(1_000)
my_new_car.read_odometer()
print()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
print()
```

Output:

```
This car has 0 miles on it.

Updated odometer to 1
This car has 1 miles on it.

Updated odometer to 1001
This car has 1001 miles on it.

You can't add negative miles!
This car has 1001 miles on it.

```

---

### Everything Is Still Accessible

Even though we've written these methods, another developer could still modify
the attributes directly. The methods aren't security. They're a convention that
discourages risky use, and they only work if everyone follows it. Anyone with
access to the code can still set the odometer to any value. Real security takes
more care than the checks shown here.

---
