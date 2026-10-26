## Classes as Attributes

Where the object-oriented programming model really gets powerful is when we
use classes as attributes of other classes.

This design approach lets a developer build highly granular object models and
combine them, so there is minimal wasted data (unused attributes or functions)
in any object.

Breaking a large class into smaller classes that work together is called
*composition*. You'll see that word in other people's code, and it's a good
habit to reach for whenever one class starts doing too many jobs.

---

### Adding a Class as an Attribute

For this example, we'll continue using our existing `Car` class.

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
        self.fuel_level = 0.0

    def get_descriptive_name(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Get the odometer mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, mileage):
        """Set the odometer mileage"""
        # Let's prevent anyone from "rolling back" the odometer
        if mileage >= self.odometer_reading:
            print(f"Setting odometer to {mileage}")
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increment the odometer mileage"""
        if miles > 0:
            self.odometer_reading += miles
            print(f"Updated odometer to {self.odometer_reading}")
        else:
            print("You can't add negative miles!")

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        self.fuel_level = 1

    def check_fuel_level(self):
        """Check the fuel level"""
        fuel_state = "empty"
        if self.fuel_level == 1.0:
            fuel_state = "full"
        elif self.fuel_level >= 0.75:
            fuel_state = "three quarters full"
        elif self.fuel_level >= 0.5:
            fuel_state = "half full"
        elif self.fuel_level >= 0.25:
            fuel_state = "one quarter full"
        elif self.fuel_level > 0.0:
            fuel_state = "running on fumes"
        print(f"Fuel Status: {fuel_state}")
```

</details>

The code file marks the `== 1.0` comparison with a `#NOSONAR` comment, which
turns off a Sonar warning about comparing floats. That comment stays in the
code file.

We'll create a new class to model a `Battery`.

```python
class Battery:
    """Defines a battery"""

    def __init__(self, battery_size=75):
        """Initialize a new instance of the Battery class"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Get the range of the battery"""
        battery_range = "unknown"
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        else:
            print(f"Range unknown for battery size: {self.battery_size}-kWh.")
            return
        print(f"This car can go about {battery_range} miles on a full charge.")
```

The code file turns off a warning about the initial value of `battery_range`. Every path below it sets a new value, or returns early, so the
starting value never gets used.

This looks like a lot of extra work, but it means the battery details live in
one place. Now `ElectricCar` doesn't need to know how batteries work.

And we will modify the `ElectricCar` class `__init__()` method to create a new
instance attribute called `battery` that holds a `Battery` object, instead of
the plain `battery_size` attribute.

```python
class ElectricCar(Car):
    """Defines an Electric Car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        # A class as an attribute
        self.battery = Battery()

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Check the fuel level"""
        print("This car doesn't contain any fuel!")
```

Where does a method like `get_range()` belong? Is range a property of the
battery or of the car? If we're only describing one car, keeping `get_range()`
on `Battery` is fine. If we're describing a whole line of cars, it might make
more sense to move it up to `ElectricCar`. Either choice works, and there's no
single right answer. Pick the one that matches the model you're building.

---

### Using the Class as an Attribute

When an instance attribute is itself an instance of another class, we use the
same dot syntax we've been using to reach its attributes, one step at a time.

`main_class_object.attribute_that_is_a_class_object.attribute_of_attribute`

```python
my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
my_e_car.battery.describe_battery()
my_e_car.battery.get_range()
```

Output:

```
2024 Nissan Leaf
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

---
