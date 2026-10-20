"""Stopping recursion"""

from time import sleep

def countdown(n: int) -> bool:
    """Counts down to zero"""
    if n < 0:
        print("Cannot count down from a negative number!")
        return False
    if n == 0:
        print("Liftoff!")
        return True
    print(n)
    sleep(0.5)
    return countdown(n - 1)

def main() -> None:
    """Main program"""
    n = 3
    if countdown(n):
        print("\nrecursions complete...")
    else:
        print("\nrecursions failed!")

if __name__ == "__main__":
    main()
