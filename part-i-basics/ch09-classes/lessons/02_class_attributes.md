## Working with Class Attributes

As models for objects, classes' ability to carry related data is paramount in
their functionality.

Likewise, controlling that data is where developers can best take advantage of object-oriented programming.

---

### Default Class Attributes

Python supports initializing properties that are not included in the `__init__`
function's arguments to default values.

This is useful when there is a known starting value for a given property. For
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

Note that the `odometer_reading` property is not passed to the constructor. 
Instead it is automatically initialized to zero.

Additionally, we've created a function `read_odometer()` that accesses the
`odometer_reading` property for us.

---

### Interacting with Class Attributes

Even though we don't set the `odometer_reading` in the calling code, because it
is initialized as a property of `self` in the `__init__` function, it is 
accessible like any other property.

```python
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
# Access `odometer_reading` either directly or via the function that reads it
my_new_car.read_odometer()
print(my_new_car.odometer_reading)
```

Output:

```
2014 Dodge Challenger
This car has 0 miles on it.
0
```

---

### Modifying Class Attributes

All member attributes of a class instance are public (and therefore directly accessible).

However, it gives you greater control over your program's behavior if you
create dedicated functions that handle modifying the attributes rather than 
having developers manage that behavior on their own.

Here is an expanded version of our car class with functions added to modify 
the `odometer_reading` attribute:

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

We can create a new instance just like we did previously:

```python
my_new_car = Car("dodge", "challenger", 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
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

my_new_car.odometer_reading = 15_000
my_new_car.read_odometer()

my_new_car.odometer_reading = -1_000
my_new_car.read_odometer()

my_new_car.odometer_reading += 2_000
my_new_car.read_odometer()

my_new_car.odometer_reading -= 1_001
my_new_car.read_odometer()
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
    * This is a car, so it should not permit a negative odometer reading

---

### Using the Attribute-Modifying Functions

That's why it's considered a best practice to create functions that can be 
called to modify the attributes according to rules you establish when
creating the class.

---

#### The `set_odometer()` Method:

By creating a method to set the odometer, we prevent the issue we had
previously, where a negative value could be set.

```python
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()

my_new_car.set_odometer(14_000)
my_new_car.read_odometer()

my_new_car.set_odometer(-1_000)
my_new_car.read_odometer()
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

Having a method to increment the odometer either by `1` (default) or by
a specified amount again keeps control of the behavior.

```python
my_new_car = Car("dodge", "challenger", 2014)
my_new_car.read_odometer()

my_new_car.increment_odometer()
my_new_car.read_odometer()

my_new_car.increment_odometer(1_000)
my_new_car.read_odometer()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
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

### Everything is Still Public

Even though we have made these functions, another developer could still
manually modify the attributes.

However, by creating purpose-built methods and exposing them in the class, we
discourage this sort of risky use.

---
