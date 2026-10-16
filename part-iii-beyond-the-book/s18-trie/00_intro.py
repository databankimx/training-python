"""Shared prefixes in a trie"""

from trie import Trie

def main() -> None:
    """Main function"""
    t = Trie()
    for word in ["and", "ant", "dad", "do"]:
        t.insert(word)
    print(f"'an' is a prefix: {t.prefix_exists('an')}")
    print(f"'anbx' is a prefix: {t.prefix_exists('anbx')}")
    print(f"'do' is a word: {t.prefix_exists('do', True).word_end}")

if __name__ == "__main__":
    main()
