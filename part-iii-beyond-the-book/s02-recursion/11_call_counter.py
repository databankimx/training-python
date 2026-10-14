"""Implementing recursion call counter"""

from time import sleep
from count_calls import CountCalls

@CountCalls
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
        print(f"\nrecursions complete after {countdown.call_count} calls...")
    else:
        print(f"\nrecursions failed after {countdown.call_count} calls...")

if __name__ == "__main__":
    main()
