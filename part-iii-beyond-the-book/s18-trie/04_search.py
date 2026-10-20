"""Searching a trie for words and prefixes"""

from trie import Trie

def main() -> None:
    """Main function"""
    t = Trie()
    for word in ["and", "ant"]:
        t.insert(word)
    print(t.search("and"))
    print(t.search("an"))
    print(t.prefix_exists("an"))
    print(t.prefix_exists("anbx"))

if __name__ == "__main__":
    main()
