"""Bitwise OR"""

def bitwise_or_example() -> None:
    """Demonstrate bitwise OR"""
    a = 0b10011100 # 156
    b = 0b00110100 # 52
    print(f"{(a | b):>08b}") # --> 1011 1100 (188)

    x = 156
    y = 52
    print(x | y) # --> 188

def permissions_example() -> None:
    """Create permissions using bitwise OR"""
    read = 1
    write = 2
    read_write = 3
    need_to_write = True
    permissions = read
    if need_to_write:
        permissions |= write
    print(f"{permissions:04b} = {permissions}")
    if permissions == read_write:
        print("Success!")

def main() -> None:
    """Main program"""
    bitwise_or_example()
    print("\n---\n")
    permissions_example()

if __name__ == "__main__":
    main()
