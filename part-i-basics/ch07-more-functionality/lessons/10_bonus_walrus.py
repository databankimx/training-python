"""Lesson 7.10"""

def check_square_old(n: int, max_n: int=100) -> None:
    """Check if the square of a number is greater than the max allowed"""
    n_squared = n ** 2
    print(f"{n}² = {n_squared}")
    infix = "" if n_squared > max_n else "not "
    print(f"{n_squared} is {infix}greater than {max_n}\n")

def check_square(n: int, max_n: int=100) -> None:
    """Check if the square of a number is greater than the max allowed"""
    print(f"{n}² = {(n_squared := n ** 2)}")
    infix = "" if n_squared > max_n else "not "
    print(f"{n_squared} is {infix}greater than {max_n}\n")

def odd_squares(n: int) -> list[int]:
    """Return a list of odd squares from 1 to n"""
    if n < 1:
        return []
    return [y for x in range(1, n + 1) if (y := x ** 2) % 2]

def main():
    """Main function to execute the program"""
    n = 9
    check_square_old(n)
    check_square(n)
    print(odd_squares(n))

if __name__ == "__main__":
    main()
