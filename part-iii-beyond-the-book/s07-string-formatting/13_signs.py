"""Demonstrates controlling signs on numbers"""

def format_signs(nums: list[int]) -> None:
    """Demonstrates controlling signs on numbers"""
    for n in nums:
        print(f"[+5d]  '{n:+5d}'")
    print()
    for n in nums:
        print(f"[=+5d] '{n:=+5d}'")
    print()
    for n in nums:
        print(f"[-5d]  '{n:-5d}'")
    print()
    for n in nums:
        print(f"[=-5d]  '{n:=-5d}'")
    print()
    for n in nums:
        print(f"[ 5d]  '{n: 5d}'")
    print()
    for n in nums:
        print(f"[= 5d]  '{n:= 5d}'")

def main() -> None:
    """Main function"""
    nums = [1, -7, 42]
    format_signs(nums)

if __name__ == "__main__":
    main()
