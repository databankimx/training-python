"""Nested formatters"""

from random import randint

def get_random_numbers(min_n: int=1, max_n: int=1000, length: int=5) -> list[int]:
    """Get a list of random integers"""
    return [randint(min_n, max_n) for _ in range(length)]

def align_numbers(numbers: list[int]) -> None:
    """Right-justify numbers for proper alignment"""
    total = sum(numbers)
    width = max(len(str(n)) for n in numbers + [total]) + 1
    for i, n in enumerate(numbers):
        lead = "+" if i == len(numbers) - 1 else " "
        print(f"{lead}{n:>{width}}")
    print("-" * (width + 1))
    print(f" {total:>{width}}")

def main() -> None:
    """Main function"""
    numbers = get_random_numbers()
    align_numbers(numbers)

if __name__ == "__main__":
    main()
