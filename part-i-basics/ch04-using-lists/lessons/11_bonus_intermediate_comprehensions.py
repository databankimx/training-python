"""Examples of more complicated comprehensions"""

from sm_utils import timer, pause, clear_terminal

def basic_loop(n: int) -> None:
    """List values from 1 to n using basic loop"""
    clear_terminal()
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Basic loop: numbers from 1 to {n}")
    result = []
    for i in range(1, n + 1):
        result.append(i)
    print(result, "\n")

def basic_comprehension(n: int) -> None:
    """List values from 1 to n using basic comprehension"""
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Basic list comprehension: numbers from 1 to {n}")
    result = [i for i in range(1, n + 1)]
    print(result, "\n")
    pause()

def computed_loop(n: int) -> None:
    """Calculate squares from 1 to n using basic loop"""
    clear_terminal()
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Computed loop: squares from 1 to {n}")
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    print(result, "\n")

def computed_comprehension(n: int) -> None:
    """Calculate squares from 1 to n using basic comprehension"""
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Computed list comprehension: squares from 1 to {n}")
    result = [i ** 2 for i in range(1, n + 1)]
    print(result, "\n")
    pause()

def conditional_loop(n: int) -> None:
    """Calculate even squares from 1 to n using basic loop"""
    clear_terminal()
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Conditional loop: even squares from 1 to {n}")
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i ** 2)
    print(result, "\n")

def conditional_comprehension(n: int) -> None:
    """Calculate even squares from 1 to n using conditional comprehension"""
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Conditional list comprehension: even squares from 1 to {n}")
    result = [i ** 2 for i in range(1, n + 1) if i % 2 == 0]
    print(result, "\n")
    pause()

@timer
def timed_for_loop(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using a for loop"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

@timer
def timed_list_comprehension(n: int) -> list[int]:
    """Calculate the square of numbers from 0 to n using list comprehension"""
    return [i ** 2 for i in range(n)]

def matrix_loop(n: int) -> None:
    """Print a matrix of size n x n using basic loop"""
    clear_terminal()
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Matrix/nested loop: size {n} x {n}")
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        result.append(row)
    for row in result:
        print(row)
    print()

def matrix_comprehension(n: int) -> None:
    """Print a matrix of size n x n using list comprehension"""
    if n < 1:
        print("`n` must be a positive integer!\n")
        return
    print(f"Matrix/nested list comprehension: size {n} x {n}")
    result = [[i * j for j in range(n)] for i in range(n)]
    for row in result:
        print(row)
    print()
    pause()

def main() -> None:
    """Main function"""
    n = 10
    basic_loop(n)
    basic_comprehension(n)
    computed_loop(n)
    computed_comprehension(n)
    conditional_loop(n)
    conditional_comprehension(n)
    clear_terminal()
    n = 10 ** 6
    print("First million squares:\n")
    print("Using for_loop...")
    timed_for_loop(n)
    print("\nUsing list_comprehension...")
    timed_list_comprehension(n)
    print()
    pause()
    n = 3
    matrix_loop(n)
    matrix_comprehension(n)

if __name__ == "__main__":
    main()
