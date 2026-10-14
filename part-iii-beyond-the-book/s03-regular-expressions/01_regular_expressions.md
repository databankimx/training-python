## Regular Expressions

Nothing strikes fear into the heart of a developer like the phrase "regular
expressions."

Regular expressions (sometimes called "regex") aren't nearly as horrible as many people think.

Yes, they can get complicated, and sometimes they're very difficult to read, 
but they adhere to a strict set of rules, so you absolutely ***can*** learn 
them.

Regardless what your peers tell you, regular expressions are just a skill,
not a dive into dark and arcane magic.

All hail Cthulhu... er... let's take a look.

---

### What is a Regular Expression?

A regular expression is just a string that represents a pattern instead of a
specific set of characters.

When we create a regular expression, we're designing it to match any string 
that follows the pattern. Patterns occur everywhere, and being able to match
them when they appear is a crucial skill in making your code better.

Here are a few examples of patterns in real-world data:

|Example|Pattern|
|-|-|
|Zip Code|Five digits optionally followed by a hyphen and four more digits|
|SSN|Three digits, an optional hyphen, two digits, an optional hyphen, four digits|
|Sentence|Unknown number of characters terminated with a punctuation mark|
|Email Address|Some characters, an @ sign, some characters, dot, some characters|

For our experiment, we'll try to come up with a pattern to match a phone
number. This can be tricky, since there are many ways a phone number could be
structured.

* `1111111111`
* `111-111-1111`
* `111.111.1111`
* `111,111,1111`
* `(111) 111-1111`
* `(111) 111-1111 ext: 11`
* and so on...

Using regular expressions, we can match them all with one pattern.

---

### What Can We Match in a Regular Expression?

We can match a lot of things:

* A specific letter, like `A`
* A range of letters, like `A-z`
* A specific number, like `0`
* A range of numbers, like `0-9`
* A set of characters, like `[-.,]`
* Any character escape, `\a  \b  \f  \n  \N  \r  \t  \u  \U  \v  \x  \\`

---

### Special Characters

In a regular expression, you can also match any of these special characters:

|Character|Meaning|
|:-:|-|
|.|Any character except newline (If DOTALL flag is on, matches newline as well)|
|^|Start of string|
|$|End of string|
|*|Zero or more of the immediately preceding item|
|+|One or more of the immediately preceding item|
|?|Zero or one of the immediately preceding item|
|*?|Zero or more of the immediately preceding item (non-greedy match)|
|+?|One or more of the immediately preceding item (non-greedy match)|
|??|Zero or one of the immediately preceding item (non-greedy match)|
|{n}|Matches exactly n instances of the preceding item|
|{m, n}|Matches m to n instances of the preceding item|
|{m, n}?|Matches m to n instances of the preceding item (non-greedy match)|
|\\ |Escapes special characters or signals special sequence|
|[]|Set: matches any character in the contained set|
|a\|b|Matches regex a or regex b|
|(regex)|Matches entire contained regex|
|\A|Matches only at beginning of string|
|\b|Matches empty string at beginning or end of a word (boundary between `\w` and `\W`)|
|\B|Matches empty string EXCEPT at beginning or end of a word|
|\d|Any digit (equivalent to `[0-9]`)|
|\D|Any non-digit (equivalent to `[^0-9]`)|
|\s|Any whitespace character (`[ \t\n\r\f\v]` and potentially others)|
|\S|Any non-whitespace character (`[^ \t\n\r\f\v]`)|
|\w|Any word character (`[a-zA-Z0-9_]`)|
|\W|Any non-word character (`[^a-zA-Z0-9_]`)|
|\Z|Matches only at end of string|

Inside a set `[...]`, these special characters may be used:

|Character|Meaning|
|:-:|-|
|^|If the first character in the set, negates is (match anything EXCEPT what is in the remaining set)|
|-|Indicates range, e.g.:   a-z 0-9|
|all others|Special characters lose their meaning in a set (except square-brackets)|

---

### Storing Regular Expressions in Code

We've previously learned about f-strings (formatted strings). Now we'll learn 
about r-strings (raw strings). In an r-string, the backslash character `\` is
treated as a literal instead of being used to escape characters in the string
itself, which allows it to be used to create the special character matches we
use in regular expressions.

Syntax: `r"literal (raw) string"`

```python
string = r"Not a carriage return -> \n"
print(string)
```

Output:

```
Not a carriage return -> \n
```

---

### Pattern Matching with Regular Expressions

In order to take advantage of regular expressions, we need to import the `re`
library.

We then use two functions from that library to create and use the regular 
expression.

* `re.compile(raw_string)` converts the string into a regular expression
* `re.search(regex)` reviews a string to determine if the pattern is found

```python
import re

pattern = r"^\d{3}$" # Match string made up of exactly three digits
regex = re.compile(pattern)
for string in ["123", "4567", "098"]:
    if regex.search(string):
        print(f"{string} is a match")
```

Output:

```
123 is a match
098 is a match
```

---

### Matching Phone Numbers with a Regular Expression

For all of these tests, we'll use this collection of phone numbers:

```python
phone_numbers = [
    "7134833111",
    "713-483-3111",
    "713.483.3111",
    "713,483,3111",
    "(713) 483-3111",
    "(713) 483-3111 ext: 42",
    "Don't match this one: (713) 483-3111 - BAD"
]
```

The goal will be to match all except the last one with one regular expression.

---

### A First, Naive Attempt

Right away, we can see that every one of these phone numbers includes an area
code, so we know we'll have to match ten numeric digits.

Let's give that a try.

We'll use:

* `\d` - special character to match a digit
* `{10}` - match exactly ten of the preceding item

```python
import re

phone_numbers = # -- SNIP (see above) --

pattern = r"\d{10}"
print(f"Using pattern: `{pattern}`\nMatches:")
regex = re.compile(pattern)
for phone in phone_numbers:
    if regex.search(phone):
        print(f"• {phone}")
```

Output:

```
Using pattern: `\d{10}`
Matches:
• 7134833111
```

We only matched the phone number with ten consecutive digits. This tells us 
that matching has to be done in smaller units. The rule of thumb is to use 
units as large as you can without allowing an errant character to break the 
match.

> Note: From this point forward, only the patterns change, so I won't keep
> including the entire code snippet.

---

### A Better (but Still Bad) Attempt

This time, we'll break up the digit matches into groups of three, three, and
four, like we normally do with a phone number in our heads. And we'll insert
hyphens to match the separators:

```python
# -- SNIP --
pattern = r"\d{3}-\d{3}-\d{4}"
# -- SNIP --
```

Output:

```
Using pattern: `\d{3}-\d{3}-\d{4}`
Matches:
• 713-483-3111
```

We only matched the number that exactly follows the pattern of three digits,
dash, three digits, dash, four digits

---

### An Improved (but Mediocre) Attempt

We saw in the special characters section that we can include a set of
characters in square brackets in order to match any one of the included
characters.

We can try replacing the dashes in our pattern with a set that allows us to
also match periods and commas, like this: `[-.,]`.

> Note: Normally, we would have to escape the period `\.`, since it is a 
> special character that matches literally anything. But we should remember
> that inside a set, special characters lose their functions, so here we can
> use it without an escape.

```python
# -- SNIP --
pattern = r"\d{3}[-.,]\d{3}[-.,]\d{4}"
# -- SNIP --
```

Output:

```
Using pattern: `\d{3}[-.,]\d{3}[-.,]\d{4}`
Matches:
• 713-483-3111
• 713.483.3111
• 713,483,3111
```

Well, that worked the way we planned. We still aren't matching the ones that
don't follow this intermediate pattern, but we're matching multiple values
now, and that's a good start.

---

### A Not-Bad Attempt

We know that we can use the `?` special character to match either zero or one
of the preceding item. Using this, we can:

* Make our sets optional `[-.,]?`
* Add optional parentheses around the area code `\(?\d{3}\)?`
* Add an optional space character after the area code `\s?`

```python
# -- SNIP --
pattern = r"\(?\d{3}\)?\s?[-.,]?\d{3}[-.,]?\d{4}"
# -- SNIP --
```

Output:

```
Using pattern: `\(?\d{3}\)?\s?[-.,]?\d{3}[-.,]?\d{4}`
Matches:
• 7134833111
• 713-483-3111
• 713.483.3111
• 713,483,3111
• (713) 483-3111
• (713) 483-3111 ext: 42
• Don't match this one: (713) 483-3111 - BAD
```

Hey! We matched all the phone numbers!

Unfortunately, we also matched the one we don't want to match.

---

### An OK Attempt

We want to not match text occurring before the phone number or bad text
following it.

To accomplish this, we can add two items to our pattern:

* `^` means the first match must occur at the beginning of the string
* `$` means the last match must occur at the end of the string

```python
# -- SNIP --
pattern = r"^\(?\d{3}\)?\s?[-.,]?\d{3}[-.,]?\d{4}$"
# -- SNIP --
```

Output:

```
Using pattern: `^\(?\d{3}\)?\s?[-.,]?\d{3}[-.,]?\d{4}$`
Matches:
• 7134833111
• 713-483-3111
• 713.483.3111
• 713,483,3111
• (713) 483-3111
```

We're not matching the bad one any more, but we're also not matching the one
with an extension. Let's see if we can fix that:

---

### A Good (if not Great) Solution

We need to match the remainder of the one number that includes an extension:
` ext: 42`

This includes:

* One optional space `\s?`
* A Label `e?x?t?`, which could be any of these:
    * `ext`
    * `ex`
    * `e`
    * `x`
* Another optional space `\s?`
* One or more additional digits `\d+`
    * Note: We'll use `\d*` (zero or more), since the whole extension part
      might not appear

```python
pattern = r"^\(?\d{3}\)?[-.,]?\s?\d{3}[-.,]?\d{4}\s?e?x?t?:?\s?\d*$"
```

Output:

```
• 7134833111
• 713-483-3111
• 713.483.3111
• 713,483,3111
• (713) 483-3111
• (713) 483-3111 ext: 42
```

We've done it! We matched all of our patterns ans managed to avoid matching
the bad pattern.

---

### So We're Done?

Not really...

This isn't a comprehensive regular expression for all possible phone number 
patterns. For example, we haven't dealt with country codes, short code
cell numbers, etc.

In the real world, you might have to modify a RegEx many times during its 
lifetime to match changing patterns.

---
