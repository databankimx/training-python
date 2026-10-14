## Searching for a Word

The whole point of a trie is to provide quick retrieval, so it's vital to
include search functionality.

---

### The Search Function

The algorithm for a search function is very similar to the insert 
algorithm.

To check if a word exists in the trie, starting from the root, at each 
node:

1. Locate the child index of the current letter
    * If no node exists, we're done: return `False`
    * Otherwise traverse to the child node
2. Repeat until the last letter is found
3. Check if the last node is a word end
    * If it is, return `True`
    * Otherwise return `False`

```python
# -- SNIP --

    def search(self, key: str) -> bool:
        """Check if word exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            current_node = current_node.children[ord(c) - self.offset]
        return current_node.word_end
```

---

### The Check Prefix Function

Sometimes, you only want to check if any word starts with a sequence of
letters as opposed to finding a specific word.

For example, if you need to search for both "anyone" and "anybody," it 
could be useful to first check to see if the prefix "any" occurs, since 
it's  a shorter search that, if false, would negate the need to check 
either of the full words.

The algorithm for a check prefix function is identical to the search except
that there is no need to check if the final letter occurs at the end of a 
word.

```python
# -- SNIP --

    def prefix_exists(self, key: str) -> bool:
        """Check if prefix exists in the trie"""
        current_node = self.root
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            current_node = current_node.children[ord(c) - self.offset]
        return True
```

---
