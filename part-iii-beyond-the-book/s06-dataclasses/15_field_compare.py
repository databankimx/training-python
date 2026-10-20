"""Field Compare"""

from dataclasses import dataclass, field

@dataclass(order=True)
class Employee:
    """Metadata about an employee"""
    name: str = field(compare=False)
    emp_id: str = field(compare=False)
    age: int
    city: str = field(compare=False)

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott McLean", "smclean", 54, "Dallas")
    emp_2 = Employee("Saul Goodman", "sgoodman", 57, "Albuquerque")

    print(f"emp_1 > emp_2: {emp_1 > emp_2}")

if __name__ == "__main__":
    main()
