"""String Modulo Operator"""

def hello(name: str) -> None:
    """Print a greeting using the string-modulo operator"""
    template = "Hello, %s!"
    values = (name,)
    print(template % values)

def compute_price(item: str, qty: int, price: float) -> None:
    """Calculate a total and print a description"""
    template = "%d %s cost $%.2f"
    values = (qty, item, price * qty)
    print(template % values)

def main() -> None:
    """Run the program"""
    hello("World")
    compute_price("bananas", 10, 0.39)

if __name__ == "__main__":
    main()
