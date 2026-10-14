"""Employee dataclass"""

from dataclasses import dataclass

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott", "smclean", 53, "Dallas")
    emp_2 = Employee("John", "Smith", 30, "Cleveland")

    emp_3 = Employee("Scott", "smclean", 53, "Dallas")

    print(emp_1)
    print(emp_2)

    print(f"emp_1 == emp_2? {emp_1 == emp_2}")
    print(f"emp_1 == emp_3? {emp_1 == emp_3}")

if __name__ == "__main__":
    main()
