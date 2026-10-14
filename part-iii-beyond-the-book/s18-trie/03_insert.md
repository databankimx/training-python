## Inserting a New Key

We have already reviewed the insert algorithm, but for review here is a
summary.

To insert a word (also called a *key*), starting from the *root* node:

1. Locate the child index for the first letter, and if it is not 
   populated, create a new node.
2. Move to the next node.
3. Repeat steps 1 and 2 until you reach the last letter
4. Mark the node for the final letter as a word end

```python
## -- SNIP --

    def insert(self, key: str) -> None:
        """Insert a string into the trie"""
        current_node = self.root
        for c in key.lower():
            index = ord(c) - self.offset # locate the child index
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(self.size)
            current_node = current_node.children[index]
        current_node.word_end = True
```

---
