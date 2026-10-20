"""The string .format() function"""

def main() -> None:
    """Main function"""
    template = "Hello, {}!"
    print(template.format("World"))

    print("{} {}".format("Hello", "World")) #pylint: disable=consider-using-f-string

    print("{} + {} = {}".format(2, 3, 2 + 3)) #pylint: disable=consider-using-f-string

    print("{1} {0}".format("world", "hello")) #pylint: disable=consider-using-f-string

    print("Name: {name}, Age: {age}".format(name="Scott", age=54)) #pylint: disable=consider-using-f-string

    try:
        print("{} {0}".format("Hello", "World")) #pylint: disable=format-combined-specification, consider-using-f-string #NOSONAR
    except ValueError as ex:
        print(f"ValueError: {ex}")

    print("Hello, %s!" % ("World",)) #pylint: disable=consider-using-f-string
    print("Hello, {}!".format("World")) #pylint: disable=consider-using-f-string

if __name__ == "__main__":
    main()
