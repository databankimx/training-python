## Chapter 9 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 9 try-it-yourself exercises.

---

### Assignment 9.1 - Restaurant

Make a class called `Restaurant`. The `__init__()` method for `Restaurant` 
should store two attributes: a `restaurant_name` and a `cuisine_type`. 
Make a method called `describe_restaurant()` that prints these two pieces 
of information, and a method called `open_restaurant()` that prints a 
message indicating that the restaurant is open. Make an instance called 
`restaurant` from your class. Print the two attributes individually,
and then call both methods.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant = Restaurant("the mad greek", "greek & indian food")
print(restaurant.name.title())
print(restaurant.cuisine.title())
restaurant.describe()
restaurant.open()
```

</details>
<br>

<details>
<summary>Output</summary>

```
The Mad Greek
Greek & Indian Food
The Mad Greek proudly serves Greek & Indian Food
The Mad Greek is open for business!
```

</details>

---

### Assignment 9.2 - Three Restaurants

Start with your class from Exercise 9.1. Create three different instances 
from the class, and call `describe_restaurant()` for each instance.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""
    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Print a description of the restaurant"""
        print(f"{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

restaurant_1 = Restaurant("The Mad Greek", "Greek & Indian food")
restaurant_2 = Restaurant("Charlie's Crab", "seafood")
restaurant_3 = Restaurant("The Brown Derby", "steak")

restaurant_1.describe()
restaurant_2.describe()
restaurant_3.describe()
```

</details>
<br>

<details>
<summary>Output</summary>

```
The Mad Greek proudly serves Greek & Indian Food!
Charlie'S Crab proudly serves Seafood!
The Brown Derby proudly serves Steak!
```

</details>

---

### Assignment 9.3 - Users

Make a class called `User`. Create two attributes called `first_name` and 
`last_name`, and then create several other attributes that are typically 
stored in a user profile. Make a method called `describe_user()` that prints 
a summary of the user's information. Make another method called
`greet_user()` that prints a personalized greeting to the user. Create 
several instances representing different users, and call both methods for 
each user.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class User:
    """Defines a user"""

    def __init__(self, first_name, last_name, location, profession):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.profession = profession

    def greet(self):
        """Greet the user"""
        print(
            f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(
            f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Location:   {self.location.title()}")
        print(f"Profession: {self.profession.title()}\n")


user_1 = User("scott", "mclean", location="dallas", profession="programmer")
user_1.greet()
user_1.describe()

user_2 = User("hillary", "taylor", location="twinsburg", profession="lawyer")
user_2.greet()
user_2.describe()

user_3 = User("jeremy", "mclean", location="columbus",
              profession="restaurant manager")
user_3.greet()
user_3.describe()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hello there, Scott Mclean
Name:       Scott Mclean
Location:   Dallas
Profession: Programmer

Hello there, Hillary Taylor
Name:       Hillary Taylor
Location:   Twinsburg
Profession: Lawyer

Hello there, Jeremy Mclean
Name:       Jeremy Mclean
Location:   Columbus
Profession: Restaurant Manager
```

</details>

---

### Assignment 9.4 - Number Served

Start with your program from Exercise 9.1. Add an attribute called 
`number_served` with a default value of 0. Create an instance called 
restaurant from this class. Print the number of customers the restaurant has 
served, and then change this value and print it again.

Add a method called `set_number_served()` that lets you set the number of 
customers that have been served. Call this method with a new number and print 
the value again.

Add a method called `increment_number_served()` that lets you increment the 
number of customers who've been served. Call this method with any number you 
like that could represent how many customers were served in, say, a day of 
business.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()} food!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")

    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")


restaurant = Restaurant("burger heaven", "american")
restaurant.describe()
restaurant.get_number_served()
restaurant.number_served = 10
restaurant.get_number_served()

restaurant.set_number_served(20)
restaurant.get_number_served()

restaurant.increment_number_served(5)
restaurant.get_number_served()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Burger Heaven proudly serves American food!
We have served 0 people today.

We have served 10 people today.

Set number served to 20
We have served 20 people today.

Incremented number served to 25
We have served 25 people today.
```

</details>

---

### Assignment 9.5 - Login Attempts

Add an attribute called `login_attempts` to your `User` class from
Exercise 9.3. Write a method called `increment_login_attempts()`
that increments the value of `login_attempts` by `1`. Write another
method called `reset_login_attempts()` that resets the value of
`login_attempts` to `0`.

Make an instance of the `User` class and call
`increment_login_attempts()` several times. Print the value of
`login_attempts` to make sure it was incremented properly, and
then call `reset_login_attempts()`. Print `login_attempts` again
to make sure it was reset to `0`.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
class User:
    """Defines a user"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"Name:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the number of login attempts"""
        print(f"Login Attempts: {self.login_attempts}")

user = User("john", "doe")
user.describe()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()
```

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       John Doe
Username:   JDOE
Login Attempts: 0
Login Attempts: 1
Login Attempts: 2
Login Attempts: 0
```

</details>

---

### Assignment 9.6 - Ice Cream Stand

An ice cream stand is a specific kind of restaurant. Write a class called
`IceCreamStand` that inherits from the `Restaurant` class you wrote in
Exercise 9.1 or Exercise 9.4. Either version of the class will work; just
pick the one you like better. Add an attribute called `flavors` that
stores a list of ice cream flavors. Write a method that displays these
flavors. Create an instance of `IceCreamStand`, and call this method.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Restaurant Class</summary>

```python
class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")
        
    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")
```

</details>
<br>

<details>
<summary>IceCreamStand Class</summary>

```python
class IceCreamStand(Restaurant):
    """Defines an Ice Cream Stand as a subclass of Restaurant"""

    def __init__(self, name, cuisine, flavors=["chocolate", "vanilla", "strawberry"]):
        """Initialize a new instance of the IceCreamStand class"""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def list_flavors(self):
        """Print out a list of the available flavors"""
        print(f"\n{self.name.title()} has the following flavors available:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}")

    def add_flavor(self, flavor):
        """Add an item to the list of the available flavors"""
        if flavor not in self.flavors:
            self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        """Remove an item from the list of the available flavors"""
        if flavor in self.flavors:
            self.flavors.remove(flavor)
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_stand = IceCreamStand("Frosty Freeze", "ice cream", ["chocolate", "vanilla", "strawberry", "pistachio"])
my_stand.list_flavors()

my_stand.add_flavor("rocky road")
my_stand.list_flavors()

my_stand.remove_flavor("pistachio")
my_stand.list_flavors()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Pistachio

Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Pistachio
 - Rocky Road

Frosty Freeze has the following flavors available:
 - Chocolate
 - Vanilla
 - Strawberry
 - Rocky Road
```

</details>

---

### Assignment 9.7 - Admin

An administrator is a special kind of user. Write a class called `Admin`
that inherits from the `User` class you wrote in Exercise 9.3 or
Exercise 9.5. Add an attribute, `privileges`, that stores a list of
strings like "can add post", "can delete post", "can ban user", and
so on. Write a method called `show_privileges()` that lists the
administrator's set of privileges. Create an instance of `Admin`, and
call your method.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User Class</summary>

```python
class User:
    """Defines a User"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(
            f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(
            f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempts counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the login attempts counter"""
        print(f"Login Attempts: {self.login_attempts}\n")
```

</details>
<br>

<details>
<summary>Admin Class</summary>

```python
class Admin(User):
    """Define an Admin as a subclass of User"""

    def __init__(self, first_name, last_name, privileges=None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the user's privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_admin = Admin("jane", "smith")
my_admin.describe()
my_admin.show_privileges()

my_admin = Admin("bob", "jones", ["create", "delete"])
my_admin.describe()
my_admin.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Jane Smith
Username:   JSMITH

Privileges:
 - create
 - delete
 - modify
 - ban

Name:       Bob Jones
Username:   BJONES

Privileges:
 - create
 - delete
```

</details>

---

### Assignment 9.8 - Privileges

Write a separate `Privileges` class. The class should have one attribute,
`privileges`, that stores a list of strings as described in Exercise 9.7.
Move the `show_privileges()` method to this class.

Make a `Privileges` instance as an attribute in the `Admin` class. Create
a new instance of `Admin` and use your method to show its privileges.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User Class</summary>

```python
class User:
    """Defines a User"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempts counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Get the login attempts counter"""
        print(f"Login Attempts: {self.login_attempts}\n")
```

</details>
<br>

<details>
<summary>Admin Class</summary>

```python
class Admin(User):
    """Define an Admin as a subclass of User"""

    def __init__(self, first_name, last_name, privileges = None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
```

</details>
<br>

<details>
<summary>Privileges Class</summary>

```python
class Privileges:
    """Defines a set of privileges"""

    def __init__(self, privileges = None):
        """Initialize a new instance of the Privileges class"""
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the user's privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_admin = Admin("jane", "smith")
my_admin.describe()
my_admin.privileges.show_privileges()

my_admin = Admin("bob", "jones", ["create", "delete"])
my_admin.describe()
my_admin.privileges.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Jane Smith
Username:   JSMITH

Privileges:
 - create
 - delete
 - modify
 - ban

Name:       Bob Jones
Username:   BJONES

Privileges:
 - create
 - delete
```

</details>

---

### Assignment 9.9 - Battery Upgrade

Use the final version of electric_car.py from this section. Add a method
to the `Battery` class called `upgrade_battery()`. This method should check
the battery size and set the capacity to 100 if it isn't already. Make an
electric car with a default battery size, call `get_range()` once, and then
call `get_range()` a second time after upgrading the battery. You should
see an increase in the car's range.

Solution:

<details>
<summary>Spoiler Code</summary>
</br>

<details>
<summary>Car Class</summary>

```python
class Car:
    """Defines a car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_level = 0

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
        """Set the fuel level to full"""
        self.fuel_level = 1

    def check_fuel_level(self):
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
```

</details>
<br>

<details>
<summary>ElectricCar Class</summary>

```python
class ElectricCar(Car):
    """Define an electric car as a subclass of Car"""

    def __init__(self, make, model, year):
        """Initialize a new instance of the ElectricCar class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Set the fuel level to full"""
        print("This car doesn't have a gas tank!")

    def check_fuel_level(self):
        """Get the fuel level"""
        print("This car doesn't contain any fuel!\n")
```

</details>
<br>

<details>
<summary>Battery Class</summary>

```python
class Battery:
    """Define a battery"""

    def __init__(self, battery_size=75):
        """Initialize a new instance of the Battery class"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Get the battery range"""
        range = "unknown"
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.\n")

    def upgrade_battery(self):
        """Upgrade the battery"""
        if self.battery_size < 100:
            self.battery_size = 100
            print("Upgraded battery.")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
my_nissan = ElectricCar("nissan", "leaf", 2024)
print(my_nissan.get_descriptive_name())

my_nissan.battery.describe_battery()
my_nissan.battery.get_range()

my_nissan.battery.upgrade_battery()
my_nissan.battery.describe_battery()
my_nissan.battery.get_range()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
2024 Nissan Leaf
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.

Upgraded battery.
This car has a 100-kWh battery.
This car can go about 315 miles on a full charge.
```

</details>

---

### Assignment 9.10 - Imported Restaurant

Using your latest Restaurant class, store it in a module. Make a separate 
file that imports Restaurant. Make a Restaurant instance, and call one of 
Restaurant's methods to show that the import statement is working properly.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Restaurant Class</summary>

In [restaurant.py](./restaurant.py)

```python
class Restaurant:
    """Defines a restaurant object"""

    def __init__(self, name, cuisine):
        """Initialize a new instance of the Restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Print a description of the restaurant"""
        print(f"\n{self.name.title()} proudly serves {self.cuisine.title()}!")

    def open(self):
        """Open the restaurant"""
        print(f"{self.name.title()} is open for business!")

    def get_number_served(self):
        """Get the number of people served by the restaurant"""
        print(f"We have served {self.number_served} people today.\n")
        
    def set_number_served(self, num):
        """Set the number of people served by the restaurant"""
        if num >= self.number_served:
            self.number_served = num
            print(f"Set number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

    def increment_number_served(self, num=1):
        """Increment the number of people served by the restaurant"""
        if num >= 0:
            self.number_served += num
            print(f"Incremented number served to {self.number_served}")
        else:
            print("Cannot reduce the number served!")

```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
from restaurant import Restaurant

my_restaurant = Restaurant("my place", "scottish food")
my_restaurant.describe()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
My Place proudly serves Scottish Food!
```

</details>

---

### Assignment 9.11 - Imported Admin

Start with your work from Exercise 9.8. Store the classes `User`, 
`Privileges`, and `Admin` in one module. Create a separate file, make an 
`Admin` instance, and call `show_privileges()` to show that everything is 
working correctly.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User, Privileges, and Admin Classes</summary>

In [full_user.py](./full_user.py)

```python
"""A class module to allow modeling users and admins"""

class User:
    """Defines a user"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempt counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempt counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Read the login attempt counter"""
        print(f"Login Attempts: {self.login_attempts}\n")


class Admin(User):
    """Define an admin ad a subclass of User"""

    def __init__(self, first_name, last_name, privileges = None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


class Privileges:
    """Define a collection of user privileges"""

    def __init__(self, privileges = None):
        """Initialize a new instance of the Privileges class"""
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the list of user privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
from full_user import Admin

my_admin = Admin("Sue", "Smith")
my_admin.describe()
my_admin.privileges.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Sue Smith
Username:   SSMITH

Privileges:
 - create
 - delete
 - modify
 - ban
```

</details>

---

### Assignment 9.12 - Multiple Modules

Store the `User` class in one module, and store the `Privileges` and `Admin` 
classes in a separate module. In a separate file, create an `Admin` instance 
and call `show_privileges()` to show that everything is still working 
correctly.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>User Class</summary>

In [user.py](./user.py)

```python
"""A class module to allow modeling users"""

class User:
    """Defines a user"""

    def __init__(self, first_name, last_name):
        """Initialize a new instance of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = f"{self.first_name[0]}{self.last_name}"
        self.login_attempts = 0

    def greet(self):
        """Greet the user"""
        print(f"Hello there, {self.first_name.title()} {self.last_name.title()}")

    def describe(self):
        """Describe the user"""
        print(f"\nName:       {self.first_name.title()} {self.last_name.title()}")
        print(f"Username:   {self.username.upper()}")

    def increment_login_attempts(self):
        """Increment the login attempt counter"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempt counter"""
        self.login_attempts = 0

    def get_login_attempts(self):
        """Read the login attempt counter"""
        print(f"Login Attempts: {self.login_attempts}\n")
```

</details>
<br>

<details>
<summary>Admin and Privileges Classes</summary>

In [admin.py](./admin.py)

```python
"""A class module allowing modeling of admins"""

from user import User

class Admin(User):
    """Define an admin ad a subclass of User"""

    def __init__(self, first_name, last_name, privileges = None):
        """Initialize a new instance of the Admin class"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


class Privileges:
    """Define a collection of user privileges"""

    def __init__(self, privileges = None):
        """Initialize a new instance of the Privileges class"""
        if privileges == None:
            self.privileges = ["create", "delete", "modify", "ban"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print out the list of user privileges"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
from admin import Admin

my_admin = Admin("Sue", "Smith")
my_admin.describe()
my_admin.privileges.show_privileges()
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
Name:       Sue Smith
Username:   SSMITH

Privileges:
 - create
 - delete
 - modify
 - ban
```

</details>

---

### Assignment 9.13 - Dice

Make a class `Die` with one attribute called `sides`, which has a default
value of 6. Write a method called `roll_die()` that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

Solution:

<details>
<summary>Spoiler Code</summary>
<br>

<details>
<summary>Die Class</summary>

In [die.py](./die.py)

```python
"""A class module for modeling a fair die"""

from random import randint

class Die:
    """Defines an n-sided die"""

    def __init__(self, sides = 6):
        """Initialize a new instance of the Die class"""
        self.sides = sides

    def roll(self):
        """Roll the die"""
        return randint(1, self.sides)
```

</details>
<br>

<details>
<summary>Calling Code</summary>

```python
from die import Die

die = Die()
for i in range(1, 11):
    print(f"[{die.sides}-sided die] Roll {i}: {die.roll()}")
print("-----")

dice = [Die(10), Die(20)]
for die in dice:
    for i in range(1, 11):
        print(f"[{die.sides}-sided die] Roll {i}: {die.roll()}")
    print("-----")
```

</details>

</details>
<br>

<details>
<summary>Output</summary>

```
[6-sided die] Roll 1: 2
[6-sided die] Roll 2: 3
[6-sided die] Roll 3: 2
[6-sided die] Roll 4: 5
[6-sided die] Roll 5: 1
[6-sided die] Roll 6: 3
[6-sided die] Roll 7: 1
[6-sided die] Roll 8: 5
[6-sided die] Roll 9: 3
[6-sided die] Roll 10: 3
-----
[10-sided die] Roll 1: 1
[10-sided die] Roll 2: 1
[10-sided die] Roll 3: 6
[10-sided die] Roll 4: 8
[10-sided die] Roll 5: 4
[10-sided die] Roll 6: 7
[10-sided die] Roll 7: 2
[10-sided die] Roll 8: 7
[10-sided die] Roll 9: 6
[10-sided die] Roll 10: 10
-----
[20-sided die] Roll 1: 4
[20-sided die] Roll 2: 9
[20-sided die] Roll 3: 4
[20-sided die] Roll 4: 20
[20-sided die] Roll 5: 10
[20-sided die] Roll 6: 17
[20-sided die] Roll 7: 18
[20-sided die] Roll 8: 2
[20-sided die] Roll 9: 17
[20-sided die] Roll 10: 4
-----
```

</details>

---

### Assignment 9.14 - Lottery

Make a list or tuple containing a series of 10 numbers and five letters. 
Randomly select four numbers or letters from the list and print a message 
saying that any ticket matching these four numbers or letters wins a prize.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]
selected = []

while len(selected) < 4:
    val = choice(numbers)
    if val not in selected:
        selected.append(val)

print(f"The winning numbers are: {selected}\n")
```

</details>
<br>

<details>
<summary>Output</summary>

```
The winning numbers are: [9, 'D', 'B', 0]
```

</details>

---

### Assignment 9.15 - Lottery Analysis

You can use a loop to see how hard it might be to win the kind of lottery 
you just modeled. Make a list or tuple called my_ticket. Write a loop that 
keeps pulling numbers until your ticket wins. Print a message reporting how 
many times the loop had to run to give you a winning ticket.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
my_ticket = ["1", "2", "3", "4"]
i_won = False
attempts = 0

while not i_won:
    attempts += 1
    selected = []
    while len(selected) < 4:
        val = choice(numbers)
        if val not in selected:
            selected.append(val)
    print(selected)
    if sorted(selected) == sorted(my_ticket):
        i_won = True

print(f"\nMy ticket {my_ticket} won after {attempts} attempts!\n")
```

</details>
<br>

<details>
<summary>Output</summary>

```
My ticket ['1', '2', '3', '4'] won after 646 attempts!
```

</details>

---

### Assignment 9.16 - Python Module of the Week

One excellent resource for exploring the Python standard library is a site
called Python Module of the Week. Go to
[https://pymotw.com/](https://pymotw.com/) and look at the table of
contents. Find a module that looks interesting to you and read about it,
perhaps starting with the random module.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
print("Complete this task as independent study.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Complete this task as independent study.
```

</details>

---

