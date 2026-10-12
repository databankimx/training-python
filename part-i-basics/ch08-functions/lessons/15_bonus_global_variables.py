"""Lesson 8.15"""

adj = "awesome"

def use_global(use_adv: bool=False):
    """Use a global variable"""
    infix = f"{adv} " if use_adv else ""
    print(f"Python is {infix}{adj}\n")

def try_to_modify_global() -> None:
    """Try (and fail) to modify a global variable"""
    # pylint: disable=redefined-outer-name
    adj = "fantastic"
    print(f"Python is {adj}")

def modify_global() -> None:
    """Modify a global variable"""
    # pylint: disable=global-statement
    global adj
    adj = "super"
    print(f"Python is {adj}")

def create_global() -> None:
    """Create a global variable"""
    # pylint: disable=global-variable-undefined
    global adv
    adv = "really"
    print(f"Python is {adv} {adj}")

def use_nonlocal(x: int=1, y: int=1) -> None:
    """Use a nonlocal variable"""
    print(f"Outer: x = {x}, y = {y}")
    def inner():
        nonlocal x
        x += 1
        y = 2
        print(f"Inner: x = {x}, y = {y}")
    inner()
    print(f"Outer: x = {x}, y = {y}\n")

def main() -> None:
    """Main function"""
    use_global()
    try_to_modify_global()
    use_global()
    modify_global()
    use_global()
    create_global()
    use_global(use_adv=True)
    use_nonlocal()

if __name__ == "__main__":
    main()
