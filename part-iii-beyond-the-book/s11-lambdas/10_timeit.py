"""Using Lambdas with `timeit`"""

from timeit import timeit
from math import factorial

def timeit_normal() -> float:
    """Using normal code with `timeit`"""
    return timeit("factorial(999)", "from math import factorial", 
                  number=10)

def timeit_with_lambda() -> float:
    """Using a lambda with `timeit`"""
    return timeit(lambda: factorial(999), number=10)

def main() -> None:
    """Main function"""
    print(timeit_normal(), "\n")
    print(timeit_with_lambda())

if __name__ == "__main__":
    main()
