"""The collections module: Counter, defaultdict, deque, and namedtuple"""

from collections import Counter, defaultdict, deque, namedtuple


def counter_example() -> None:
    """Count how often each item appears with Counter"""
    letters = Counter("mississippi")
    print(letters)
    print(letters.most_common(2))
    print()


def defaultdict_example() -> None:
    """Supply a default value for missing keys with defaultdict"""
    groups = defaultdict(list)
    for name, dept in [("Ana", "sales"), ("Ben", "tech"), ("Cy", "sales")]:
        groups[dept].append(name)
    print(dict(groups))
    print()


def deque_example() -> None:
    """Add and remove items at both ends with deque"""
    queue = deque(["first", "second"])
    queue.append("third")
    queue.appendleft("zero")
    print(queue.popleft())
    print(queue)
    print()


def namedtuple_example() -> None:
    """Create a tuple whose fields have names with namedtuple"""
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print(p.x, p.y)
    print(p)
    print()


def main() -> None:
    """Run each collections example"""
    counter_example()
    defaultdict_example()
    deque_example()
    namedtuple_example()


if __name__ == "__main__":
    main()
