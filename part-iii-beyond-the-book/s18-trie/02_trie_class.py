"""The Trie class and its members"""

from trie import Trie

def main() -> None:
    """Main function"""
    t = Trie()
    print(f"Size: {t.size}")
    print(f"Offset: {t.offset}")
    print(f"Root children: {len(t.root.children)}")
    print(f"Root is empty: {all(child is None for child in t.root.children)}")

if __name__ == "__main__":
    main()
