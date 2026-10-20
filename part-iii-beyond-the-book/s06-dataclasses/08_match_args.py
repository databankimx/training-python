"""DataClass with Match Arguments"""

from dataclasses import dataclass

@dataclass(match_args=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean", 54, "Dallas")
    print(emp)

    # Results in AttributeError unless match_args is True
    # for arg in emp.__match_args__:
    #     print(f"{arg} = {emp.__dict__[arg]}")

if __name__ == "__main__":
    main()
