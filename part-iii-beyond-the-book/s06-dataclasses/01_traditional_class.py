"""Employee Class (Traditional)"""

class Employee:
    """Metadata about an employee"""

    def __init__(self, name: str, emp_id: str, age: int, city: str) -> None:
        """Employee Constructor"""
        self.name = name
        self.emp_id = emp_id
        self.age = age
        self.city = city

    def __repr__(self) -> str:
        """String representation of an employee"""
        return f"Employee (name: {self.name}, id: {self.emp_id}, " + \
            f"age: {self.age}, city: {self.city})"
    
    def __eq__(self, value: object) -> bool:
        """Check if two Employee objects contain the same data"""
        return (self.name, self.emp_id, self.age, self.city) == \
            (value.name, value.emp_id, value.age, value.city)

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott", "smclean", 53, "Dallas")
    emp_2 = Employee("John", "Smith", 30, "Cleveland")

    print(emp_1)
    print(emp_2)

    emp_3 = Employee("Scott", "smclean", 53, "Dallas")

    print(f"emp_1 == emp_2? {emp_1 == emp_2}")
    print(f"emp_1 == emp_3? {emp_1 == emp_3}")

if __name__ == "__main__":
    main()
