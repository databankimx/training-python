"""The string .format() function"""

def main() -> None:
    """Main function"""
    template = "Hello, {}!"
    print(template.format("World"))

    print("{} {}".format("Hello", "World"))

    print("{} + {} = {}".format(2, 3, 2 + 3))

    print("{1} {0}".format("world", "hello"))

    print("Name: {name}, Age: {age}".format(name="Scott", age=54))

    try:
        print("{} {0}".format("Hello", "World"))
    except ValueError as ex:
        print(f"ValueError: {ex}")

    print("Hello, %s!" % ("World",))
    print("Hello, {}!".format("World"))

if __name__ == "__main__":
    main()
