"""Example using a function to filter a list"""

def even(n: int) -> bool:
    """Check if a number is even"""
    return not n % 2

def even_loop(numbers: list[int]) -> list[int]:
    """Get even numbers using a loop"""
    even_numbers = []
    for n in numbers:
        if even(n):
            even_numbers.append(n)
    return even_numbers

def even_comprehension(numbers: list[int]) -> list[int]:
    """Get even numbers using a list comprehension"""    
    return [n for n in numbers if even(n)]

def even_filter(numbers: list[int]) -> list[int]:
    """Get even numbers using the filter function"""
    return list(filter(even, numbers))

def main() -> None:
    """Main function"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(even_loop(numbers))
    print(even_comprehension(numbers))
    print(even_filter(numbers))

if __name__ == "__main__":
    main()
