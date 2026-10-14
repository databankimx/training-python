## Overriding Parent Class Methods

Sometimes you will have a parent class that implements functions that do not
make sense in a child class. This breakdown in the "common functionality"
concept can be the result of bad design, changing requirements, or even a 
change in the over all environment.

Perhaps we implemented our `Car` class in an era before there was widespread
adoption of electric vehicles. It might have made sense to implement methods
in that version of the car class for filling the gas tank and reading the fuel
gauge, neither of which makes sense for the child `ElectricCar` class:

```python
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
        print(f"Fuel Status: {fuel_state}\n")
```

<details>
<summary>The Car Class with Fuel Functions</summary>

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
        print(f"Fuel Status: {fuel_state}\n")
```

</details>

<br>One option to address this would be to remove those functions from the `Car`
class and create another child class, perhaps `InternalCombustionCar` and
implement them there.

Unfortunately, in the real world, there may be several prior versions of the
software in production, and changing the model might make them incompatible.

For situations like this, we can override an existing function with different behavior in the child class.

---

### Creating an Override Function

To override a parent class function, we simply add a function with an 
identical signature (`def check_fuel_level(self)`, e.g.) to the child class.

When the class contains a method matching a function call, it will be executed
rather than looking to the parent class. It *overrides* the parent function.

In this case, we'll override the two fuel-related functions

```python
    def fill_gas_tank(self):
        """Set the gas tank to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Check the fuel level"""
        print("This car doesn't contain any fuel!\n")
```

<details>
<summary>The ElectricCar Class with Fuel Function Overrides</summary>

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

    def fill_gas_tank(self):
        """Set the gas tank to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
```

</details>

---

### Using Parent Class Functions and Overrides Interchangeably

Now, in our code, we don't have to worry about keeping track of whether or not 
the method makes sense. Instead there is behavior specific to the child class to prevent confusion.

```python
my_car = Car("dodge", "challenger", 2014)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
my_car.check_fuel_level()

my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
my_e_car.describe_battery()
my_e_car.fill_gas_tank()
my_e_car.check_fuel_level()
```

Output:

```
2014 Dodge Challenger
Fuel Status: full

2024 Nissan Leaf
This car has a 75-kWh battery.
This car doesn't have a gas tank!
This car doesn't contain any fuel!
```

---
