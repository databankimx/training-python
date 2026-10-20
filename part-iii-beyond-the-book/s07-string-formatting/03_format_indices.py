"""Using `string.format()` with Indices"""

def hello_index() -> None:
    """Using `string.format()` with an Index"""
    print("\nUsing `string.format()` with an Index")
    # template = "Hello, {0}!"
    # values = ("World",)
    # print(template.format(*values))

    # pylint: disable=consider-using-f-string
    print("Hello, {0}!".format("World"))

def price_index(item: str, qty: int, price: float) -> None:
    """Using `string.format()` with Multiple Indices"""
    print("\nUsing `string.format()` with Multiple Indices")
    total = round(price * qty, 2)

    # template = "{0} {1} cost ${2}"
    # values = (qty, item, total)
    # print(template.format(*values))

    # template = "{2} {0} cost ${1}"
    # values = (item, total, qty)
    # print(template.format(*values))

    # pylint: disable=consider-using-f-string
    print("{0} {1} cost ${2}".format(qty, item, total))

def main() -> None:
    """The main function"""
    hello_index()
    price_index("bananas", 5, 0.39)

if __name__ == "__main__":
    main()
