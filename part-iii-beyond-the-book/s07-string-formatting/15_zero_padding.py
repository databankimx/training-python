"""Zero Padding"""

def pad_zeros() -> None:
    """Pad numbers with zeros"""
    nums = [1, -7, 123]
    for n in nums:
        print(f"{n:>05d}, {n:>06.1f}")

def pad_zeros_str() -> None:
    """Pad a string with zeros"""
    s = "abc"
    print(f"{s:>05}")

def drown_zeros() -> None:
    """Pad with other character"""
    nums = [1, -7, 123]
    for n in nums:
        print(f"{n:•>05d}, {n:•>06.1f}")

def main() -> None:
    """Main function"""
    pad_zeros()
    print()
    pad_zeros_str()
    print()
    drown_zeros()

if __name__ == "__main__":
    main()
