"""String `.format()` Using Keywords"""

def hello_keywords() -> None:
    """Using `string.format()` with a Keyword"""
    print("\nUsing `string.format()` with a Keyword")
    # template = "Hello, {name}!"
    # keywords = {"name": "World"}
    # print(template.format(**keywords))

    # pylint: disable=consider-using-f-string
    print("Hello, {name}!".format(name="World"))

def price_keywords(item: str, qty: int, price: float) -> None:
    """Using `string.format()` with Multiple Keywords"""
    total = round(price * qty, 2)

    # template = "{num} {name} cost ${price}"
    # keywords = {"num": qty, "name": item, "price": total}
    # print(template.format(**keywords))

    # pylint: disable=consider-using-f-string
    print("{num} {name} cost ${price}".format(num=qty, name=item, price=total))

def main() -> None:
    """Main Program"""
    hello_keywords()
    price_keywords("bananas", 5, 0.39)

if __name__ == "__main__":
    main()
