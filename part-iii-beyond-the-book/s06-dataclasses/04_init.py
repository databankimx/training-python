"""Overriding the `__init__()` Method"""

from dataclasses import dataclass

@dataclass(init=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city
        self.emp_id = f"{name[0].lower()}{name.split()[-1].lower()}"

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", 54, "Dallas")
    print(emp)

if __name__ == "__main__":
    main()
