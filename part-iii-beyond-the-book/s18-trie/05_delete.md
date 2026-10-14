## Deleting a Word

Removing a word from a trie is a bit trickier than insertion or search.

We cannot necessarily remove the nodes for the letters in the word, since
those nodes might be used by other words in the trie.

For example, if both "any" and "anyone" are in the trie, deleting "any"
should not remove "any" as a prefix, only as a word end.

---

### The Delete Algorithm

Walking down the trie from the root, we need to know two things:

1. Whether the word is in the trie at all. If the final letter's node is not
   marked as a word end, the word is not there, so we return `False`.
2. How much of the word can be removed. Nodes are only safe to remove after
   the last point where the path *branches*, meaning a node that has more than
   one child. Everything below that branch belongs only to our word.

So the algorithm keeps track of the last branch node it passes, and then:

* If the final node has children, other words continue past it. We only clear
  its word-end flag.
* Otherwise, we remove the child link from the last branch node, which deletes
  the whole chain of letters that only this word used.
* If there was no branch at all, the word is the only one that starts with its
  first letter, so we remove that link from the root.

---

### The Delete Function

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
        for i in range(self.size):
            if current_node.children[i] is not None:
                count += 1
        if count > 1:
            last_branch_node = current_node
            last_branch_char = c
        current_node = current_node.children[ord(c) - self.offset]
    if not current_node.word_end:
        return False
    count = 0
    for i in range(self.size):
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

The `if not current_node.word_end` check is what stops a prefix from being
deleted by mistake. Without it, deleting "an" from a trie that only holds
"anyone" would remove the "anyone" branch.

---

### Trying It

Build a small trie, then delete words and check the results:

```python
from trie import Trie

t = Trie()
for word in ["any", "anyone"]:
    t.insert(word)

print(t.delete("an"))      # False: "an" was never inserted
print(t.delete("any"))     # True: removes "any" as a word
print(t.search("anyone"))  # True: "anyone" still exists
print(t.search("any"))     # False: "any" is no longer a word
```

Output:

```
False
True
True
False
```

> Note: `search()` is wrapped in the `@timer` decorator, so each call to it also
> prints an execution time line before its result. Those lines are left out of
> the output above.

---
