## Detecting Palindromes

Palindromes are words or phrases that are spelled the same way backward and 
forward.

* Spaces and punctuation can be ignored
* Case can be ignored
* I will also ignore numeric character for simplicity

So, we have a couple of tasks in order to check if a string is a palindrome:

1. Sanitize the string:
    * Remove any characters other than letters
    * Standardize the case to all-upper or all-lower case
2. Check if the remaining characters are palindromic

> Full code example in [palindromes.py](./09_palindromes.py)

---

### Sanitizing the String

There are a number of ways we could approach this using loops, but most (if 
not all) would involve nesting loops and could get messy, so I have elected to
use a list comprehension to remove all the non-alphabetic characters and then
convert the result to all lower case:

```python
def clean_text(text: str) -> str:
    """Remove non-letters and standardize case"""
    return "".join([(text[i] if text[i].isalpha() else "")
                    for i in range(len(text))]).lower()
```

We can test this by just passing in a string with characters we don't want to
include:

```python
print(clean_text("Madam, I'm Adam."))
```

Output:

```
madamimadam
```

OK, that part is out of the way...

---

### Palindrome Checking (the Easy Way)

There is a clear and obvious way to test if a string is a palindrome in
Python: We just check if the string is equivalent to its reverse.

```python
text = clean_text("Madam, I'm Adam.")
if text == text[::-1]:
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is not a palindrome!")
```

Output:

```
'Madam, I'm Adam.' is a palindrome
```

---

### Palindrome Checking (Recursive)

Let's imagine, however, that the simple approach above doesn't exist or that
we just specifically want to accomplish the task recursively.

Here's an algorithm that we might implement:

* If the string is only one character long, it's a palindrome by definition
* If the first and last characters of the string are not the same, then the
  string is not a palindrome
* If the first and last characters of the string are the same, remove them and
  repeat the algorithm

We have two base cases: a single character or different characters at the
start and end of the string.

We have logic (the removal of the first and last characters) that progressively moves us toward the base case.

And we have a hint that recursion might be involved in the word "repeat."

So we can put together a recursive algorithm for palindrome checking:

```python
def is_palindrome(text: str) -> bool:
    """Checks if a word or phrase is a palindrome"""
    if len(text) < 2:
        return True
    return text[0] == text[-1] and is_palindrome(text[1:-1])
```

Which we can check like this:

```python
words = ["foo", "race car", "boot", "toot", "Madam, I'm Adam."]
for word in words:
    infix = "" if is_palindrome(clean_text(word)) else "not "
    print(f"- '{word}' is {infix}a palindrome")
```

Output:

```
- 'foo' is not a palindrome
- 'race car' is a palindrome
- 'boot' is not a palindrome
- 'toot' is a palindrome
- 'civic' is a palindrome
- 'Madam, I'm Adam.' is a palindrome
```

Great! It works!

---

### Palindrome Checking (Iterative)

Of course, we can pretty easily convert this to an iterative algorithm.

This approach is basically identical to the one we used in our recursive
function but uses a while loop instead.

```python
def is_palindrome(text: str) -> bool:
    """Checks if a word or phrase is a palindrome"""
    while len(text) > 1:
        if text[0] != text[-1]:
            return False
        text = text[1:-1]
    return True
```

Let's run the same tests:

```python
words = ["foo", "race car", "boot", "toot", "Madam, I'm Adam."]
for word in words:
    infix = "" if is_palindrome(clean_text(word)) else "not "
    print(f"- '{word}' is {infix}a palindrome")
```

Output:

```
- 'foo' is not a palindrome
- 'race car' is a palindrome
- 'boot' is not a palindrome
- 'toot' is a palindrome
- 'civic' is a palindrome
- 'Madam, I'm Adam.' is a palindrome
```

And we got the same output. So this one works too.

---
