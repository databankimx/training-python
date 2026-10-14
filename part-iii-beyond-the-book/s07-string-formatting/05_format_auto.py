"""Using `string.format()` with Auto-Matching"""

def hello_auto() -> None:
    """Using `string.format()` with Auto-Matching"""
    print("\nUsing Auto-Matching `string.format()`")
    # template = "Hello, {}!"
    # values = ("World",)
    # print(template.format(*values))

    # pylint: disable=consider-using-f-string
    print("Hello, {}!".format("World"))

def price_keywords(item: str, qty: int, price: float) -> None:
    """Using `string.format()` with Multiple Keywords"""
    total = round(price * qty, 2)

    # template = "{} {} cost ${}"
    # values = (qty, item, total)
    # print(template.format(*values))

    # pylint: disable=consider-using-f-string
    print("{} {} cost ${}".format(qty, item, total))

def main() -> None:
    """Main Program"""
    hello_auto()
    price_keywords("bananas", 5, 0.39)

if __name__ == "__main__":
    main()
