"""Using f-strings"""

from datetime import datetime

def hello_f_string() -> None:
    """Using a simple f-string with one interpolation"""
    name = "World"
    f_string = f"Hello, {name}!\n"
    print(f_string)

def price_f_string(item: str, qty: int, price: float) -> None:
    """Using an f-string with multiple interpolations"""
    total = round(price * qty, 2)
    f_string = f"{qty} {item} cost ${total}\n"
    print(f_string)

def convert_f_string() -> None:
    """Using an f-string with conversion"""
    now = datetime.now()
    print(f"{now!s}")
    print(f"{now!r}\n")

def replace_invalid_f_string(invalid_string: str) -> str:
    """Remove invalid characters from a string"""
    return f"{invalid_string!a}"

def main() -> None:
    """Main function"""
    hello_f_string()
    price_f_string("bananas", 5, 0.39)
    convert_f_string()
    invalid_string = "Thisö stringö hadö invalidö charactersö."
    print(replace_invalid_f_string(invalid_string))

if __name__ == "__main__":
    main()
