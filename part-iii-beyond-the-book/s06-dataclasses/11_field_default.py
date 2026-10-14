"""Field Default Values"""

from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str = field(default="Dallas")

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott", "smclean", 53)
    emp_2 = Employee("Saul", 47, "sgoodman", "Albuquerque")

    # pylint: disable=no-member
    print(emp_1.__dataclass_fields__["city"])

    print(emp_1)
    print(emp_2)

if __name__ == "__main__":
    main()
