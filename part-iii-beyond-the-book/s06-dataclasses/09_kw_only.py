"""DataClass with Keyword Only Arguments"""

from dataclasses import dataclass

@dataclass(kw_only=True)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

def main() -> None:
    """Main Function"""
    # Results in a TypeError
    # emp = Employee("Scott McLean", "smclean", 54, "Dallas")

    emp = Employee(name="Scott McLean", emp_id="smclean", age=54, city="Dallas")
    print(emp)

if __name__ == "__main__":
    main()
