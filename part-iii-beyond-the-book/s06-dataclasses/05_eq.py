"""Overriding the equality operator"""

from dataclasses import dataclass

@dataclass(eq=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

    def __eq__(self, value: object) -> bool:
        return self.name == value.name \
           and self.emp_id == value.emp_id \
           and self.age == value.age \
           and self.city == value.city

def main() -> None:
    """Main function"""
    emp_1 = Employee("Scott McLean", "smclean", 54, "Dallas")
    emp_2 = Employee("Saul Goodman", "sgoodman", 47, "Albuquerque")
    emp_3 = Employee("Scott McLean", "smclean", 54, "Dallas")

    print(f"emp_1 = emp_2: {emp_1 == emp_2}")
    print(f"emp_1 = emp_3: {emp_1 == emp_3}")

if __name__ == "__main__":
    main()
