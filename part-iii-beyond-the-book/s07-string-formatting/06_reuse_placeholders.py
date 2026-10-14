"""Reusing placeholders in string formatting"""

def squares_reuse() -> None:
    """Use a placeholder index multiple times"""
    x, y = 2, 3
    squared = "²"

    # pylint: disable=consider-using-f-string
    print("{0}{1} = {2}\n{3}{1} = {4}\n".format(x, squared, x ** 2, y, y ** 2))

def imaginary_properties() -> None:
    """Access properties from a placeholder"""
    x = 3 + 5j

    # pylint: disable=consider-using-f-string
    print("Real = {0.real}\nImag = {0.imag}\n".format(x))

def main() -> None:
    """Main function"""
    squares_reuse()
    imaginary_properties()

if __name__ == "__main__":
    main()
