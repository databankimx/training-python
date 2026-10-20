"""Format Specifiers"""

def formatted_pi() -> None:
    """ `pi` to 2 places, zero-padded to 6 characters"""
    pi = 3.14159
    # pylint: disable=consider-using-f-string
    print("%06.2f" % pi)
    print("{:06.2f}".format(pi))
    print(f"{pi:06.2f}")

def main() -> None:
    """Main Function"""
    formatted_pi()

if __name__ == "__main__":
    main()
