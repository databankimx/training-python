## Manipulating String Case

Case matters more than it looks. You might need to compare two strings without
caring about capitals, store everything in one consistent format, or simply
print something that doesn't look like it was typed during a caps-lock
accident.

Python gives you several built-in methods for changing case.

---

### Convert to Upper Case

Use `upper()` to turn every letter in a string into a capital.

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

Use `lower()` to turn every letter into a lowercase one.

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

Use `capitalize()` to make the first letter a capital.

```python
name = "python crash course"
print(name.capitalize())
```

Output:

```
Python crash course
```

Be careful with this one. `capitalize()` also lowercases everything after the
first letter, so a string that's already in capitals gets quieter:

```python
print("NASA".capitalize())
```

Output:

```
Nasa
```

If you wanted NASA to stay NASA, `capitalize()` isn't the method you want.

---

### Convert to Title Case

Use `title()` to capitalize the first letter of each word.

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

Don't rely on title case. It's useful for quick formatting, but it has real
limitations.

> #### The `title()` function does **not** know grammar!
>
> In English titles, words like *and*, *the*, and *in* usually aren't
> capitalized, unless they're the first word.
>
> Python's `title()` doesn't know that. It capitalizes every word, so you get
> results like this:
>
> ```python
> print("the lord of the rings".title())
> ```
>
> Output:
>
> ```
> The Lord Of The Rings
> ```
>
> Nobody writes a book title like that. Well, almost nobody.

> #### The `title()` function does **not** work for names!
>
> It might seem like `title()` would be handy for fixing people's names,
> especially when they arrive in all capitals from a database.
>
> ```python
> name = "JOHN SMITH"
> print(name.title())
> ```
>
> Output:
>
> ```
> John Smith
> ```
>
> That looks right, and it's a trap.
>
> Try a name that doesn't follow the one-capital-per-name pattern:
>
> ```python
> name = "Scott McLean"
> print(name.title())
> ```
>
> Output:
>
> ```
> Scott Mclean
> ```
>
> That's wrong. The name is McLean, with a capital L, and `title()` lowercased
> it. Names are spelled the way their owners spell them, so a misspelled name is
> a misspelled name, even if the capitals look tidy.
>
> ```python
> name = "Vincent van Gogh"
> print(name.title())
> ```
>
> Output:
>
> ```
> Vincent Van Gogh
> ```
>
> Also wrong. The name is van Gogh, with a lowercase *van*, and `title()` added a
> capital that doesn't belong there.
>
> Failing to account for names that don't have exactly one capital letter is one
> of the most common mistakes in programming. Don't be the next developer to fall
> into that trap.

---

### The Original String Doesn't Change

The case methods don't change the string you call them on. They return a new
string, and the original stays the same:

```python
name = "python crash course"
print(name.upper())
print(name)
```

Output:

```
PYTHON CRASH COURSE
python crash course
```

If you want to keep the uppercase version, store it in a variable:

```python
shouting = name.upper()
print(shouting)
```

Output:

```
PYTHON CRASH COURSE
```

This is true of every string method you'll meet in this chapter. Get into the
habit of asking, "Did I save the result, or did I just print it and walk away?"

---
