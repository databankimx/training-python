"""Field Representation"""

from dataclasses import dataclass, field

@dataclass
class Employee:
    """Metadata about an employee"""
    name: str
    age: int = field(repr=False)
    emp_id: str
    city: str = field(init=False, default="Dallas")

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", 53, "smclean")
    print(emp)
    # pylint: disable=no-member
    print(emp.__dataclass_fields__["age"])

if __name__ == "__main__":
    main()
