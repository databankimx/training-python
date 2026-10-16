"""A single node in a trie"""

from trie_node import TrieNode

def main() -> None:
    """Main function"""
    node = TrieNode()
    print(f"Children: {len(node.children)}")
    print(f"First child: {node.children[0]}")
    print(f"Word end: {node.word_end}")

if __name__ == "__main__":
    main()
