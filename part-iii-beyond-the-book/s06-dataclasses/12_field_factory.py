"""Field Factory Functions"""

from dataclasses import dataclass, field
from itertools import count

_id_counter = count(1)

def get_emp_id() -> str:
    """Factory Function: returns the next employee ID"""
    return f"emp{next(_id_counter):04d}"

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="Dallas")

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott McLean", 54)
    emp_2 = Employee("Saul Goodman", 47, "sgoodman", "Albuquerque")
    emp_3 = Employee("Jane Doe", 30)

    print(emp_1.emp_id)

    # pylint: disable=no-member
    print(emp_1.__dataclass_fields__["emp_id"])

    print(emp_1)
    print(emp_2)
    print(emp_3)

if __name__ == "__main__":
    main()
