"""Inserting words into a trie"""

from trie import Trie

def main() -> None:
    """Main function"""
    t = Trie()
    t.insert("and")
    print(f"Node for 'a' exists: {t.root.children[0] is not None}")
    print(f"Node for 'an' exists: {t.prefix_exists('an')}")
    print(f"'and' is a word end: {t.prefix_exists('and', True).word_end}")
    t.insert("ant")
    print(f"'ant' is a word end: {t.prefix_exists('ant', True).word_end}")
    print(f"'an' is a word end: {t.prefix_exists('an', True).word_end}")

if __name__ == "__main__":
    main()
