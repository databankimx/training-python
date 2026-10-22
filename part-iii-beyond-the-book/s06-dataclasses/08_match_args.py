"""Dataclass with `match_args`"""

from dataclasses import dataclass

@dataclass(match_args=False)
class Employee:
    """Metadata about an employee"""
    name: str
    emp_id: str
    age: int
    city: str

@dataclass
class MatchEmployee:
    """Metadata about an employee, with the default match_args"""
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

    match_emp = MatchEmployee("Scott McLean", "smclean", 54, "Dallas")
    match match_emp:
        case MatchEmployee("Scott McLean", emp_id, age, city):
            print(f"Found Scott: {emp_id}, age {age}, {city}")

if __name__ == "__main__":
    main()
