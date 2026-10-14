"""Field Initialization"""

from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int
    emp_id: str
    city: str = field(init=False, default="Dallas")

def main() -> None:
    """Main Function"""
    emp = Employee("Scott", "smclean", 53)
    print(emp)
    # pylint: disable=no-member
    print(emp.__dataclass_fields__["city"])

    # This would produce a TypeError, because the `city` attribute is not
    #     permitted to appear in the constructor
    # emp_2 = Employee("Saul", "sgoodman", 47, "Albuquerque")

    emp_2 = Employee("Saul", "sgoodman", 47)
    emp_2.city = "Albuquerque"
    print(emp_2)

if __name__ == "__main__":
    main()
