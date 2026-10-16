"""Delete words from a trie"""

from trie import Trie

def main() -> None:
    """Main function"""
    t = Trie()
    for word in ["any", "anyone"]:
        t.insert(word)

    print(t.delete("an"))
    print(t.delete("any"))
    print(t.search("anyone"))
    print(t.search("any"))

if __name__ == "__main__":
    main()
