"""Frozen DataClasses"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 53, "Dallas")
    print(emp)

    # This will result in a FrozenInstanceError
    # emp.age = 54
    # print(emp)

if __name__ == "__main__":
    main()
