## Importing Classes

Just like imports of modules and functions, we can import classes from a 
module.

For this lesson, the following classes have been created as separate module 
files:

* [car.py](./car.py)
    <details>
    <summary>Car Class</summary>

    ```python
    """A class module to define a car"""

    class Car:
        """Defines a car"""

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Initialize a new instance of the Car class

            Parameters:  
            * **make**: Manufacturer of the car
            * **model**: Model name of the car
            * **year**: Model year of the car
            """
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
            self.fuel_level = 0

        def get_descriptive_name(self) -> str:
            """
            Describe the car
            
            **Returns**:  
            Description of the car
            """
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self) -> None:
            """Get the odometer mileage"""
            print(f"This car has {self.odometer_reading} miles on it.\n")

        def set_odometer(self, mileage: int) -> None:
            """
            Set the odometer mileage
            
            Parameters:
            * **mileage**: Number of miles on the odometer
            """
            if mileage >= self.odometer_reading:
                print(f"Setting odometer to {mileage}")
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles: int=1) -> None:
            """
            Increment the odometer mileage
            
            Parameters:
            * **miles**: Number of miles to add to the odometer
            """
            if miles > 0:
                self.odometer_reading += miles
                print(f"Updated odometer to {self.odometer_reading}")
            else:
                print("You can't add negative miles!")

        def fill_gas_tank(self) -> None:
            """Fill the gas tank"""
            self.fuel_level = 1

        def check_fuel_level(self) -> None:
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

    </details><br>

* [electric_car.py](./electric_car.py)
    <details>
    <summary>ElectricCar and Battery Classes</summary>

    ```python
    """A class module to define an electric car"""

    # Because the superclass "Car" is defined in a separate module, we have to import it
    from car import Car

    class ElectricCar(Car):
        """ Define an electric car as a subclass of Car"""

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Initialize a new instance of the ElectricCar class

            Parameters:  
            * **make**: Manufacturer of the car
            * **model**: Model name of the car
            * **year**: Model year of the car
            """
            super().__init__(make, model, year)
            self.battery = Battery()

        def fill_gas_tank(self) -> None:
            """Set the fuel level to full"""
            print("This car doesn't have a gas tank!")

        def check_fuel_level(self) -> None:
            """Get the fuel level"""
            print("This car doesn't contain any fuel!\n")


    class Battery:
        """Define a battery"""

        def __init__(self, battery_size: int=75) -> None:
            """
            Initialize a new instance of the Battery class

            Parameters:  
            * **battery_size**: Battery size (in kWh)
            """
            self.battery_size = battery_size

        def describe_battery(self) -> None:
            """Describe the battery"""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self) -> None:
            """Get the battery range in miles"""
            range = "unknown"
            if self.battery_size == 75:
                range = 260
            elif self.battery_size == 100:
                range = 315
            print(f"This car can go about {range} miles on a full charge.\n")

        def upgrade_battery(self) -> None:
            """Upgrade the battery"""
            if self.battery_size < 100:
                self.battery_size = 100
                print("Upgraded battery.")
    ```

    </details><br>

* [full_car.py](./full_car.py)
    <details>
    <summary>Car, ElectricCar, and Battery Classes</summary>

    ```python
    """A set of classes used to represent gas and electric cars"""

    class Car:
        """Define a car"""

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Initialize a new instance of the Car class

            Parameters:  
            * **make**: Manufacturer of the car
            * **model**: Model name of the car
            * **year**: Model year of the car
            """
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0
            self.fuel_level = 0

        def get_descriptive_name(self) -> str:
            """
            Describe the car
            
            **Returns**:  
            Description of the car
            """
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self) -> None:
            """Get the odometer mileage"""
            print(f"This car has {self.odometer_reading} miles on it.\n")

        def set_odometer(self, mileage: int) -> None:
            """
            Set the odometer mileage
            
            Parameters:
            * **mileage**: Number of miles on the odometer
            """
            if mileage >= self.odometer_reading:
                print(f"Setting odometer to {mileage}")
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles: int=1) -> None:
            """
            Increment the odometer mileage
            
            Parameters:
            * **miles**: Number of miles to add to the odometer
            """
            if miles > 0:
                self.odometer_reading += miles
                print(f"Updated odometer to {self.odometer_reading}")
            else:
                print("You can't add negative miles!")

        def fill_gas_tank(self) -> None:
            """Set the fuel level to full"""
            self.fuel_level = 1

        def check_fuel_level(self) -> None:
            """Get the fuel level"""
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


    class ElectricCar(Car):
        """ Define an electric car as a subclass of Car"""

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Initialize a new instance of the ElectricCar class

            Parameters:  
            * **make**: Manufacturer of the car
            * **model**: Model name of the car
            * **year**: Model year of the car
            """
            super().__init__(make, model, year)
            self.battery = Battery()

        def fill_gas_tank(self) -> None:
            """Set the fuel level to full"""
            print("This car doesn't have a gas tank!")

        def check_fuel_level(self) -> None:
            """Get the fuel level"""
            print("This car doesn't contain any fuel!\n")


    class Battery:
        """Define a battery"""

        def __init__(self, battery_size: int=75) -> None:
            """
            Initialize a new instance of the Battery class

            Parameters:  
            * **battery_size**: Battery size (in kWh)
            """
            self.battery_size = battery_size

        def describe_battery(self) -> None:
            """Describe the battery"""
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self) -> None:
            """Get the battery range in miles"""
            range = "unknown"
            if self.battery_size == 75:
                range = 260
            elif self.battery_size == 100:
                range = 315
            print(f"This car can go about {range} miles on a full charge.\n")

        def upgrade_battery(self) -> None:
            """Upgrade the battery"""
            if self.battery_size < 100:
                self.battery_size = 100
                print("Upgraded battery.")
    ```

    </details>

> Note: The code samples for this lesson are split across several files in
> order to avoid conflicting imports.

---

### Importing a Class

To import a class we use the same syntax we used for a function:  
`from module import class`

So, we can create a python file that imports our `Car` class like this:

See sample code file:
[06a_importing_a_class.py](./06a_importing_a_class.py)

```python
from car import Car

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.set_odometer(23)
my_new_car.read_odometer()
```

Output:

```
2019 Audi A4
Setting odometer to 23
This car has 23 miles on it.
```

---

### Importing an Inherited Class

When we import a class that inherits from another class, we can access the
functionality of the parent class without explicitly importing it.

And when the imported class uses another class as an attribute, we gain that
class's functionality as well.

In this instance, we only import the `ElectricCar` class, but:

* Since it inherits from `Car`, we gain the functionality of the `Car` class
* Since its `battery` attribute is an instance of the `Battery` class, we gain
  the `Battery` functionality as well.

See sample code file:
[06b_importing_inherited_classes.py](./06b_importing_inherited_classes.py)

```python
from electric_car import ElectricCar

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

### Importing Multiple Classes

We can import multiple classes from a module the same way we import multiple
functions:  
`from module import Class1, Class2, ...`

Here, we'll import both the `Car` and `ElectricCar` classes

See sample code file:
[06c_importing_multiple_classes.py](./06c_importing_multiple_classes.py)

```python
from full_car import Car, ElectricCar

my_gas_car = Car("volkswagen", "beetle", 1967)
print(my_gas_car.get_descriptive_name())

my_e_car = ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
```

Output:

```
1967 Volkswagen Beetle
2024 Nissan Leaf
```

---

### Importing a Module with Classes

When you import a module, you gain access to the classes in it but not to
classes in modules from which it imports.

A class instance that inherits from a class in another module will still 
expose the parent class's functionality but not the class itself.

See sample code file:
[06d_import_module.py](./06d_import_module.py)

So we can perform this task:

```python
import electric_car

my_e_car = electric_car.ElectricCar("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
```

Output:

```
2024 Nissan Leaf
```

Our `ElectricCar` instance was able to run the `get_descriptive_name()` 
function from the `Car` class.

---

But, even though we had access to a `Car` function through inheritance,
because it is defined in a different module, we cannot access `Car` directly.

```python
import electric_car

my_car = Car("volkswagen", "beetle", 2019)
print(my_car.get_descriptive_name())
```

Output:

```
Traceback (most recent call last):
  File "...\06d_import_module_into_module.py", line 10, in <module>
    my_car = Car("volkswagen", "beetle", 2019)
             ^^^
NameError: name 'Car' is not defined. Did you mean: 'chr'?
```

---

### Using an Alias

Of course, just like a module or function, we can use an alias when importing
a class:  
`from module import class as alias`

See sample code file:
[06e_using_an_alias.py](./06e_using_an_alias.py)

```python
from electric_car import ElectricCar as EC

my_e_car = EC("nissan", "leaf", 2024)
print(my_e_car.get_descriptive_name())
```

Output:

```
2024 Nissan Leaf
```

---
