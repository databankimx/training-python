"""Dataclass attributes (decorator arguments)"""

from dataclasses import dataclass

@dataclass(slots=True)
class Employee:
    """Employee with a fixed set of attributes (slots)"""
    name: str
    emp_id: str

@dataclass(unsafe_hash=True)
class Point:
    """Point that can be hashed because unsafe_hash is True"""
    x: int
    y: int

def main() -> None:
    """Main Function"""
    emp = Employee("Scott McLean", "smclean")
    print(emp)

    try:
        emp.nickname = "Scott" #pylint: disable=attribute-defined-outside-init #NOSONAR
    except AttributeError:
        print("Cannot add a new attribute to a slotted class")

    point = Point(1, 2)
    print(f"Point hash is an integer? {isinstance(hash(point), int)}")

if __name__ == "__main__":
    main()
