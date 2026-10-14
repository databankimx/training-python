<style>
    span.indent {
        display: inline-block;
        width: 25px;
    }
</style>

## The Trie Data Structure

A `trie` (pronounced like "try") is a tree-like data structure used in 
computer science to efficiently store and retrieve strings.

The word "trie" is derived from "tree" (the data structure it is built
upon) and "reTRIEval" (the function for which is improves efficiency).

Sometimes called a *digital tree* or *prefix tree*, the trie is made up of 
nodes, where each node represents a single character step when building a 
word.

This means that if any two words share the same prefix (for example: "and"
and "ant" share the prefix "an"), then they share the same ancestor in the
trie.

---

### Very Efficient for String Searches

Because we are traversing the trie letter by letter until we either find
the complete string or reach a dead end, the worst-case complexity for a
search is O(*k*) where *k* is the number of letters in the word.

In the image above, searching from the root, it requires three steps to locate
the word "and" and only three steps to identify that "anbx" is not
in the trie.

This may seem trivial when searching for a single word, but consider this
use case:

* You have a dictionary (of some number *n* words)
* For any given word in the dictionary, you need to determine if its 
  reverse is also a word.

#### Poor Efficiency Using a List

Let's assume that we're using a `list` to contain the words.

* If we make no assumptions about whether or not the list is sorted, we'll
  have to perform *n* checks for each of the *n* words to identify which
  have their reverses in the dictionary
    * That's *n* * *n* operations: O(*n*²)
* Assuming the list is fully sorted, we can implement a more efficient
  algorithm using an O(log *n*) binary search:
    * For *n* words, that's O(*n* log *n*) complexity, and while there are
      some incremental improvements we could make, that's nearly the best we can do

#### Improved Efficiency Using a Trie

On the other hand, we know that with a trie, each search requires only *k*
operations, so to check our *n* words, we have *n* * *ꝁ* (*ꝁ* is the 
average of all word lengths *k*) operations, which is O(*n*), since *ꝁ* 
is a constant.

That means that if the average length of the words in the dictionary is 
smaller than the log (base 2) of the number of words, the trie will always 
be a faster search mechanism, even if the list is sorted.

In the [example dictionary](./data/words.txt) included in this lesson, 
there are: 370,105 words (note: Log₂(370,105) = 18.05) with an average 
length of 9 characters.

* O(*n*²) = 136,977,711,025 operations
* O(*n* log *n*) = 6,846,943 operations
* O(*n*) (*n* * *k*) = 3,330,945 operations

So, the trie is at least twice as fast as a sorted list (and 40,000 times 
faster that the unsorted list).

Once we take into account the cost of sorting the list (at least another 
O(*n* log *n*)), the trie is definitely the clear winner.

---

### What About a Hash Table?

Using a hash table is another common option for storing and retrieving 
string data. However, the Trie has advantages over it as well.

* Efficient prefix search (or auto-complete - think Google)
* Easily traverse all words in alphabetical order which is not easily 
  possible with hashing.
* No overhead of Hash functions in a Trie data structure.
* Searching for a String even in the large collection of strings in a Trie 
  data structure can be done in O(L) Time complexity, Where L is the 
  number of words in the query string. This searching time could be even 
  less than O(L) if the query string does not exist in the trie.

---

### Trie Properties

OK - I'm sold! What are the properties of a trie?

* Contains an empty root node, with links (or references) to other nodes.
* Each node represents a string, and each edge represents a character.
* Every node consists of hashmaps or an array of pointers
    * with each index representing a character
    * and a flag to indicate if any string ends at the current node.
* Trie data structure can contain any number of characters including 
  alphabets, numbers, and special characters.
    * For the examples in this lesson, we'll focus solely on the English
      alphabet, so each node will contain:
        * Array of 26 character pointers
        * A character will only be populated if children exist
* Each path from the root to any node represents a word or string.

---

### How Does a Trie Work?

Here is an image of a simple trie containing paths to the words "and,"
"ant," "dad," and "do".

<img src="./images/trie_1.png" style="width:260px">

The *root node* (like any node in the trie) contains pointers for each
possible child. When initialized, all child nodes in the root node array
will contain some default value: `null`, `None`, `0`, etc.

When we store the word "and" into a new trie, we do the following:

1. Inserting "and," we first check if the "a" child exists.
    * Since it does not, we mark it as filled with a new node
        * `root_node[0] = TrieNode()`
    * ...and traverse to the new node.
    * Although in reality "a" is a word, it is not in our insert set, so
      we do not mark the "a" node as a word end.
2. Now, in the "a" node, we check its array to see if "n" is populated
    * We know that it is not, since this is a new node
    * So we create the new node and traverse to it.
3. From the "a -> n" node, we repeat the process to populate its "d" node
    * This node is a word end (so we flag it)
    * And since we've reached the end of the word, we don't populate any 
      of its children.

After this insertion the trie looks like this:

```
root_node
    ↓ (children)
  [a_node|...|0]
      ↓ (children)
    [0|...|(a)n_node|...|0]
            ↓ (children)
        [0|...|(an)d_node*|...|0]
```

Now, if we insert "ant", starting from the root:

1. We find "a" already populated
2. We find "a → n" already populated
3. Node "a → n → t" is not populated, so we create it and mark it as a
   word end, and so on.

Now the trie looks like this:

```
root_node
    ↓ (children)
  [a_node|...|0]
      ↓ (children)
    [0|...|(a)n_node|...|0]
            ↓ (children)
        [0|...|(an)d_node*|...|(an)t_node*|...|0]
```

You can see that each word's parent is a prefix up to the last letter of 
the word, and their parents are their prefixes, and so on.

---

### Other Functionality

We'll need to implement search, retrieve, delete, and other typical data
structure functions, but for now, understanding how data is inserted is
enough to get the basic gist of the trie.

In the following lessons, we'll implement the trie in Python and add the
necessary functions.

---
