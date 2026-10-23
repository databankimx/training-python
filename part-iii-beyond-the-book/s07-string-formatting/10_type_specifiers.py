"""Type Specifiers"""

def data_types() -> None:
    """Demonstrates the use of format specifiers to control data types"""
    answer = 42
    print(f"d: {answer:d}")
    print(f"b: {answer:b}")
    print(f"e: {answer:e}")
    print(f"f: {answer:f}")
    print(f"g: {answer:g}")
    print(f"o: {answer:o}")
    print(f"X: {answer:X}")
    print(f"%: {answer / 100:.0%}")
    print(f"c: {answer:c}")
    print(f"s: {str(answer):s}\n")

def data_type_labels() -> None:
    """Demonstrates the use of format specifiers to label data types"""
    answer = 42
    print(f"b: {answer:#b}")
    print(f"o: {answer:#o}")
    print(f"X: {answer:#X}")
    print(f"g: {answer:#g}\n")

def main() -> None:
    """Main function"""
    data_types()
    data_type_labels()

if __name__ == "__main__":
    main()
