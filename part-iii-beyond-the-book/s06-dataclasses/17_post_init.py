"""Post-Init Hook"""

from dataclasses import dataclass, field

@dataclass()
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str
    age_verified: bool = field(init=False)

    def __post_init__(self):
        min_age = 30
        self.age_verified = self.age > min_age

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 54, "Dallas")
    print(emp)

if __name__ == "__main__":
    main()
