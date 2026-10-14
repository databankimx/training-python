"""Computing factorials without recursion"""

def iterative_factorial(n: int) -> int | None:
    """Calculate the factorial of n"""
    if not isinstance(n, int) or n < 0:
        print("n must be a non-negative integer!")
        return None
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def main() -> None:
    """Main program"""
    # print(iterative_factorial(1001))
    for n in range(10):
        print(f"{n}! = {iterative_factorial(n)}")

if __name__ == "__main__":
    main()
