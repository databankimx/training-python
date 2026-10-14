"""Inheritance with DataClasses"""

from dataclasses import dataclass

@dataclass()
class Staff:
    """Metadata about a staff member"""
    name: str
    emp_id: str
    age: int
    city: str

@dataclass
class Employee(Staff):
    """Metadata about an employee"""
    salary: int

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 54, "Dallas", 50_000)
    print(emp)

if __name__ == "__main__":
    main()
