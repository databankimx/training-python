"""Field Metadata"""

from dataclasses import dataclass, field

@dataclass()
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str = field(default="Dallas", metadata={"gps": (32.78306, -96.80667)})

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 54)
    print(emp)
    # pylint: disable=no-member
    print(emp.__dataclass_fields__["city"].metadata["gps"])

if __name__ == "__main__":
    main()
