"""Lesson 11.1 (3rd Edition)"""

from name_function import formatted_name

def main() -> None:
    """User testing for formatted name function"""

    print("Enter 'q' at any time to quit.")

    while True:
        first = input("\nPlease give me a first name: ")
        if first and first.lower() == "quit":
            break
        middle = input("Please give me a middle name (optional): ")
        if middle and middle.lower() == "quit":
            break
        last = input("Please give me a last name: ")
        if last and last.lower() == "quit":
            break
        if not middle:
            middle = None
        print(f"\nName: {formatted_name(first, last, middle)}")

if __name__ == "__main__":
    main()
