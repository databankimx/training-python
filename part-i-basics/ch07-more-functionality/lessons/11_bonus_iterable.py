"""Lesson 7.11"""

from typing import Iterable

def is_iterable(obj: any) -> Iterable|None:
    """Check if the given object is iterable"""
    try:
        return iter(obj)
    except TypeError:
        return None

def show_iteration(coll: Iterable, level: int=0) -> None:
    """Show the elements of an iterable in a formatted manner"""
    if not (iter_obj := is_iterable(coll)):
        print(f"`{type(coll).__name__}` is not iterable.\n")
        return
    while True:
        try:
            item = next(iter_obj)
            print(f"{' ' * level * 2}• {item}")
            if is_iterable(item) and len(item) > 1:
                show_iteration(item, level + 1)
        except StopIteration:
            if not level:
                print()
            break

def main() -> None:
    """Main program"""
    try:
        iter(None)
    except TypeError as e:
        print(f"TypeError: {str(e)}\n")
    stuff = [34, [4, 5], (4, 5), {"a":4}, "abcd", 4.5]
    for item in stuff:
        print(f"{str(item):9}", end="")
        print(f"{f'({type(item).__name__})':8}", end="")
        print(f"iterable: {bool(is_iterable(item))}")
    print()
    arr = [1, 2, 3]
    show_iteration(arr)
    show_iteration(42)
    show_iteration(stuff)

if __name__ == "__main__":
    main()
