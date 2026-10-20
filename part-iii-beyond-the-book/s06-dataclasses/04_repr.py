"""Override the `__repr__()` Method"""

from dataclasses import dataclass

@dataclass(repr=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

    def __repr__(self) -> str:
        return f"Employee (name: {self.name}, id: {self.emp_id}, " + \
            f"age: {self.age}, city: {self.city})"

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 54, "Dallas")
    print(emp)

if __name__ == "__main__":
    main()
