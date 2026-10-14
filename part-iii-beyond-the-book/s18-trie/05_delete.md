## Deleting a Word

Removing a word from a trie is a bit trickier than insertion or search.

We cannot necessarily remove the nodes for the letters in the word, since
those nodes might be used by other words in the trie.

For example, if both "any" and "anyone" are in the trie, deleting "any"
should not remove "any" as a prefix, only as a word end.

---

### The Delete Function

For a delete function, the algorithm works as follows:

In addition to the current node, we'll need to keep track of the current 
*branch* (parent node)

#### TODO: Describe the algorithm

```python
    def delete(self, key: str) -> bool:
        """Remove word from trie"""
        current_node = self.root
        last_branch_node = None
        last_branch_char = "a"
        for c in key.lower():
            if current_node.children[ord(c) - self.offset] is None:
                return False
            count = 0
            for i in range(26):
                if current_node.children[i] is not None:
                    count += 1
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c
            current_node = current_node.children[ord(c) - self.offset]
        count = 0
        for i in range(26):
            if current_node.children[i] is not None:
                count += 1
        if count > 0:
            current_node.word_end = False
            return True
        if last_branch_node is not None:
            last_branch_node.children[ord(last_branch_char) - self.offset] = None
            return True
        self.root.children[ord(key[0]) - self.offset] = None
        return True
```

---
