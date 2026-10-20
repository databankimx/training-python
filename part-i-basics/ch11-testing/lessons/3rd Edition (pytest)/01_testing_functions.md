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

### Test-Driven Development with `pytest`

One especially good approach to unit testing is test-driven development, where
we create the tests for a list of cases (preferably exhaustive) before we even
start writing the code.

Remember our two possible cases are:

* The call includes a middle name
* The call omits the middle name

Python provides a library `pytest` that allows you to create tests for parts 
of your software that validate that your code produces the expected results.

> Note: Unlike `unittest`, `pytest` is not part of the standard library.   
> Follow the steps below to install the library
>
> In the terminal run the following commands:
> * Create a virtual environment: [12_bonus_virtual_environments.md](../../../ch08-functions/lessons/12_bonus_virtual_environments.md)   
>   ```pwsh
>   python.exe -m venv .venv
>   ```
> * Activate the virtual environment:  
>   ```pwsh
>   .venv\Scripts\activate
>   ```
> * Install `pytest`:  
>   ```pwsh
>   python.exe -m pip install pytest
>   ```

To use `pytest`, we create a file whose name starts with `test_...`, and in 
that file, we create functions that execute the desired test cases.

Each function is what we call a *unit test*, and the collection of unit tests
is called a *test case*.

We use the `assert` statement to state a condition representing our assumed 
result. The test passes if the condition asserted is true. Otherwise the test
fails.

In [`test_name_function.py`](./test_name_function.py)

```python
from name_function import formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    name = formatted_name("janis", "joplin")
    assert name == "Janis Joplin"

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    name = formatted_name("wolfgang", "mozart", "amadeus")
    assert name == "Wolfgang Amadeus Mozart"
```

---

### The First Run

Right now, having written no functional code in `formatted_name()`, both of our
tests should fail, because the function will only return `None`.

To perform testing:

1. Navigate to the folder where this script is located in your terminal
2. Run the following command in the terminal  
   `pytest`
3. Verify your results
   - Green dots `.` following the filename indicate passed tests
   - Failed tests are indicated by a red `F` and are followed by an error 
     description

Output:

```
===================== test session starts =====================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_name_function.py FF                                 [100%]

=========================== FAILURES ==========================
_____________________ test_first_last_name ____________________

    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
        name = formatted_name("janis", "joplin")
>       assert name == "Janis Joplin"
E       AssertionError: assert None == 'Janis Joplin'
test_name_function.py:6: AssertionError
_________________ test_first_last_middle_name _________________

    def test_first_last_middle_name():
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        name = formatted_name("wolfgang", "mozart", "amadeus")
>       assert name == "Wolfgang Amadeus Mozart"
E       AssertionError: assert None == 'Wolfgang Amadeus Mozart'

test_name_function.py:11: AssertionError
=================== short test summary info ===================
FAILED test_name_function.py::test_first_last_name - AssertionError: assert None == 'Janis Joplin'
FAILED test_name_function.py::test_first_last_middle_name - AssertionError: assert None == 'Wolfgang Amadeus Mozart'
====================== 2 failed in 0.07s ======================
```

As expected, both tests fail with an `AssertionError`, because the function
returns `None`, which doesn't match our expected result.

---

### Writing Some Code and Retesting

Let's have a first go at the function code:

```python
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    full_name =  f"{first} {middle} {last}"
    return full_name.title()
```

Output:

```
====================== test session starts ======================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_name_function.py F.                                       [100%]

============================ FAILURES ===========================
_____________________ test_first_last_name ______________________

    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
        name = formatted_name("janis", "joplin")
>       assert name == "Janis Joplin"
E       AssertionError: assert 'Janis  Joplin' == 'Janis Joplin'
E
E         - Janis Joplin
E         + Janis  Joplin
E         ?      +

test_name_function.py:6: AssertionError
==================== short test summary info ====================
FAILED test_name_function.py::test_first_last_name -
  AssertionError: assert 'Janis  Joplin' == 'Janis Joplin'
==================== 1 failed, 1 passed in 0.08s ================
```

---

### Evaluating the Failures and Debugging

Now we see `F.`, so we know we passed the second test and failed the first 
(where we omitted the middle name).

Let's have a look at why.

We can review an explanation of the failed assertion:

```
E       AssertionError: assert 'Janis  Joplin' == 'Janis Joplin'
E
E         - Janis Joplin
E         + Janis  Joplin
E         ?      +
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
==================== test session starts ====================
platform win32 -- Python 3.11.4, pytest-8.3.2, pluggy-1.5.0
rootdir: ...\3rd Edition (pytest)
collected 2 items

test_name_function.py ..                                        [100%]

==================== 2 passed in 0.02s ======================
```

At last, we see `..`, so our tests passed, and our function is debugged.

---

