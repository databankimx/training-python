"""Field Factory Functions"""

from dataclasses import dataclass, field

def get_emp_id():
    """Factory Function"""
    new_id = "smclean"
    return new_id

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="Dallas")

def main() -> None:
    """Main Function"""
    emp_1 = Employee("Scott", 54)
    emp_2 = Employee("Saul", 47, "sgoodman", "Albuquerque")

    print(emp_1.emp_id)

    # pylint: disable=no-member
    print(emp_1.__dataclass_fields__["emp_id"])

    print(emp_1)
    print(emp_2)

if __name__ == "__main__":
    main()
