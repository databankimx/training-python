## Testing Functions

> There are two kinds of programmers: ones who write bad code and liars.  
> &emsp;&emsp;~me

Let's face it. When you write code, you're going to write bugs. Everyone does.
Yes, even ChatGPT.

You can perform extensive manual testing of your code to make sure it's 
bug-free before you release it to the public, and sometimes you will need to
test manually.

But it's more efficient to create automated tests that you can run every time
you make an update to the code. Programming is all about automation after all.

This may not completely replace human QA, but
it certainly reduces the time spent, especially if automated testing reveals
an issue before it gets into human testing.

---

### Planning For an Automated Test

Let's take a look at the example of a function to return a formatted name.

We know that we want the function to:

* Accept a first and last name (plus an optional middle name)  
  and
* Return a full name where the names are capitalized.

So, the function (without the actual code) will look something like this:

```python
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    ...
```

We also know how we'd like the function results to look:

If I include a value for `middle`, I expect the result to be formatted like this:

```
First Middle Last
```

But if I omit the `middle` argument, I want the result to look like this:

```
First Last
```

This gives me the information to set up tests for two possible cases.

---

### Test-Driven Development with `unittest`

One especially good approach to unit testing is test-driven development, where
we create the tests for a list of cases (preferably exhaustive) before we even
start writing the code.

Remember our two possible cases are:

* The call includes a middle name
* The call omits the middle name

Python provides a library `unittest` that allows you to create tests for parts 
of your software that validate that your code produces the expected results.

> Note: `unittest` is an older testing method, and many developers now use
> `pytest` instead (see the 3rd edition lessons in this chapter), but it's
> still useful to learn, as you may be asked to maintain older code where the
> unit testing is still written using `unittest`.

To use `unittest`, we create a class that inherits from `unittest.TestCase`
and in that function, we create functions that execute the desired test cases.

Each function is what we call a *unit test*, and the collection of unit tests
is called a *test case*.

We use one of the `assert...()` functions to state our assumed result, which 
will be compared against the computed result. If they match, the test is 
passed. Otherwise it is failed.

|Assert Function|Tests|
|-|-|
|`assertEqual(x, y)`|`x == y`|
|`assertNotEqual(x, y)`|`x != y`|
|`assertTrue(x)`|`x == True`|
|`assertFalse(x)`|`x == False`|
|`assertIn(item, list)`|`item is in list`|
|`assertNotIn(item, list)`|`item is not in list`|
<br>

```python
import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for the `formatted_name()` function"""

    def test_with_middle(self) -> None:
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        result = formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(result, "Wolfgang Amadeus Mozart")

    def test_without_middle(self) -> None:
        """Do names like 'Janis Joplin' work?"""
        result = formatted_name("janis", "joplin")
        self.assertEqual(result, "Janis Joplin")
```

We can also add a `main()` function to call `unittest.main()`, which will
execute the tests in the class that inherited `unittest.TestCase`

```python
def main():
    unittest.main()

if __name__ == "__main__":
    main()
```

---

### The First Run

Right now, having written no functional code in `formatted_name()`, both of our
tests should fail, because the function will only return `None`.

> Note: the code file keeps two earlier versions of `formatted_name()` as
> comments. To see each output below, uncomment one version and comment out the
> active version. The line numbers stay the same either way.

Output:

```
FF
======================================================================
FAIL: test_with_middle (__main__.NamesTestCase.test_with_middle)
Do names like 'Wolfgang Amadeus Mozart' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\01_testing_functions.py", line 31, in test_with_middle
    self.assertEqual(result, "Wolfgang Amadeus Mozart")
AssertionError: None != 'Wolfgang Amadeus Mozart'

======================================================================
FAIL: test_without_middle (__main__.NamesTestCase.test_without_middle)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\01_testing_functions.py", line 36, in test_without_middle
    self.assertEqual(result, "Janis Joplin")
AssertionError: None != 'Janis Joplin'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=2)
```

The first line will contain a dot `.` for each passed test and an `F` for each 
failed test. We see `FF`, so both tests failed.

---

### Writing Some Code and Retesting

Let's have a first go at the function code:

```python
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

Output:

```
.F
======================================================================
FAIL: test_without_middle (__main__.NamesTestCase.test_without_middle)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "...\01_testing_functions.py", line 36, in test_without_middle
    self.assertEqual(result, "Janis Joplin")
AssertionError: 'Janis  Joplin' != 'Janis Joplin'
- Janis  Joplin
?      -
+ Janis Joplin


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

---

### Evaluating the Failures and Debugging

Now we see `.F`, so we know we passed the first test and failed the second 
(where we omitted the middle name).

Let's have a look at why.

We can review an explanation of the failed assertion:

```
AssertionError: 'Janis  Joplin' != 'Janis Joplin'
- Janis  Joplin
?      -
+ Janis Joplin
```

It looks like the problem is that there are two spaces between the names.

That makes sense, since we included a space after the middle name even if it
didn't have a value.

So, to fix our bug, we need to modify the function to only add the second space
if there is a value for the middle name.

---

### Fixing the Bug and Retesting

There are a number of approaches we could take to fix this, but for our
example, let's just use a simple conditional, even though it's not the most
efficient solution.

```python
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

Output:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

At last, we see `..`, so our tests passed, and our function is debugged.

---
