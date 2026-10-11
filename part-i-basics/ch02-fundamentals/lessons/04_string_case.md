## Ch 2 - Lesson 4: Manipulating String Case

It is often necessary to manipulate the case of characters within a string
for case-sensitive comparisons, storage standardization, or display purposes.

Python provides several built-in methods for manipulating string case.

---

### Convert to Upper Case

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

Do not rely on `title()` blindly. It has significant limitations:

> #### The `title()` function does **not** know grammar
>
> In English, words like *and*, *the*, *in* are not capitalized in titles
> unless they are the first word. Python's `title()` does not include any
> logic to identify these words - it capitalizes every word in the string.

> #### The `title()` function does **not** work for names
>
> At first glance it might seem useful for capitalizing names, and for a
> simple case like `"JOHN SMITH"` it produces `"John Smith"` correctly.
>
> But consider names with unusual capitalization:
>
> ```python
> name = "Scott McLean"
> print(name.title())  # Outputs: Scott Mclean  <-- WRONG
>
> name = "Vincent van Gogh"
> print(name.title())  # Outputs: Vincent Van Gogh  <-- WRONG
> ```
>
> Failing to handle names correctly is one of the most common mistakes in
> programming. Do not fall into this trap.

---
