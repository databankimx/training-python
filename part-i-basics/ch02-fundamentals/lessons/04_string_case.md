## Ch 2 - Lesson 4: Manipulating String Case

It's often necessary to manipulate the case of characters within a string
for purposes of case-sensitive comparisons, storage standardization, or
just printing in a nicely formatted way.

Python provides several built-in methods for manipulating string case.

---

### Convert to Upper Case

You can convert a string to all-upper-case using the `upper()` function.

```python
name = "python crash course"
print(name.upper())
```

Output:

```
PYTHON CRASH COURSE
```

---

### Convert to Lower Case

You can convert a string to all-lower-case using the `lower()` function.

```python
name = "PYTHON CRASH COURSE"
print(name.lower())
```

Output:

```
python crash course
```

---

### Convert to Sentence Case

You can capitalize the first letter of the string using the `capitalize()` 
function.

```python
name = "python crash course"
print(name.capitalize())
```

Output:

```
Python crash course
```

---

### Convert to Title Case

You can capitalize the first letter of each word in the string using the 
`title()` function.

```python
name = "python crash course"
print(name.title())
```

Output:

```
Python Crash Course
```

---

### A Word of Caution about Title Case

Do not rely on title-case. While it's a useful function, there are some
significant limitations:

> #### The `title()` function does **not** know grammar!
> 
> In English titles, words like *and*, *the*, *in*, and so on are not
> capitalized in titles unless they occur as the first word.
> 
> Python's `title()` function does not include logic to identify words that
> should not be capitalized. It just capitalizes every word in the string.

> #### The `title()` function does **not** work for names!
>
> At first blush, it might seem like the `title()` function would be useful
> for properly capitalizing people's names.
>
> ---
>
> For example, if you have a database containing data in all uppercase,
> a scenario like this...
>
> ```python
> name = "JOHN SMITH"
> print(name.title()) # Outputs: `John Smith`
> ```
>
> ... functions as expected, because "JOHN SMITH" would be capitalized as 
> "John Smith" 
>
> ---
>
> But thinking this way is a trap!
>
> What happens to someone like "Scott McLean" or "Vincent van Gogh"
>
> ```python
> name = "Scott McLean"
> print(name.title()) # Outputs: `Scott Mclean` *WRONG!
> ```
>
> In a proper name failing to capitalize a letter is a misspelling of
> the name.
>
> ```python
> name = "Vincent van Gogh"
> print(name.title()) # Outputs: `Vincent Van Gogh` *WRONG!
> ```
>
> So is capitalizing a letter that shouldn't be capitalized
>
> ---
>
> Failing to consider the issue of names not always containing exactly one
> capital letter is one of the most ubiquitous errors in programming.
>
> Don't be the next developer to fall prey to this trap.
>
> ---
