"""Identifying palindromes"""

def clean_text(text: str) -> str:
    """Remove non-letters and standardize case"""
    return "".join([(text[i] if text[i].isalpha() else "")
                    for i in range(len(text))]).lower()

def is_palindrome_simple(text: str) -> bool:
    """Checks if a word or phrase is a palindrome"""
    clean = clean_text(text)
    return clean == clean[::-1]

def is_palindrome_recursive(text: str) -> bool:
    """Checks if a word or phrase is a palindrome"""
    if len(text) < 2:
        return True
    return text[0] == text[-1] and is_palindrome_recursive(text[1:-1])

def is_palindrome_iterative(text: str) -> bool:
    """Checks if a word or phrase is a palindrome"""
    while len(text) > 1:
        if text[0] != text[-1]:
            return False
        text = text[1:-1]
    return True

def main() -> None:
    """Main function"""
    words = ["foo", "race car", "boot", "toot", "Madam, I'm Adam."]

    algorithms = {
        "simple": is_palindrome_simple,
        "recursive": is_palindrome_recursive,
        "iterative": is_palindrome_iterative
    }

    for name, algorithm in algorithms.items():
        print(f"\nTest with {name} algorithm:")
        for word in words:
            infix = "" if algorithm(clean_text(word)) else "not "
            print(f"- '{word}' is {infix}a palindrome")

if __name__ == "__main__":
    main()
