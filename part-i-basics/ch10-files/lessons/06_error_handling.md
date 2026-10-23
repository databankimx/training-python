## Handling Errors

Because working with files introduces more opportunities for errors to occur,
now is a good time to divert our attention and discuss error handling.

---

There are four general kinds of errors (or exceptions) that can occur in
programs:

* Syntax Errors
    * Syntax errors are places in your code where the code is not valid Python,
      like a missing colon, an unmatched bracket, or a misspelled keyword.
    * Python finds these when it compiles the file, before any of the code runs.
      A syntax error stops the program before it produces any output.
* Runtime Errors
    * Python is an interpreted language, so most errors occur at runtime (when
      the program is executing).
    * A runtime error halts the program in progress.
    * Runtime errors can occur due to many possible scenarios:
        * Addressing an out of range index in a collection
        * Receiving the wrong type of data (or no data at all) in a function
          call
        * Searching for a resource (like a file) that isn't there
        * Performing an invalid arithmetic operation
        * Etc.
    * In Python (like most languages), when a runtime error occurs, the
      interpreter raises an exception object that contains information about
      what went wrong.
* Logical Errors
    * Logic errors do not halt the program.
    * Instead, they result in invalid or unexpected behavior.
    * Logic errors are caused by invalid data, incorrect conditions and
      constraints, failure to consider a possible use case, etc.
    * These can be the most difficult to troubleshoot, because they don't
      present an error message.

This lesson focuses on handling runtime errors.

---

### Handling Runtime Errors

Since runtime errors occur during execution, they cause the program to crash.

In general, it's a bad idea to allow your program to crash, as that impacts the
user experience negatively.

Instead, we should consider the cases where an error might possibly occur and
add code to gracefully handle the errors.

Python, like most languages, lets you catch an error as it happens and handle it
with a `try` ... `except` construction.

The general structure of this mechanism looks like this:

```python
try:
    # Code here executes until either it completes or an error occurs
except ZeroDivisionError:
    # Code here runs if a ZeroDivisionError is raised during the `try` block
    # Note: You can have multiple `except` blocks for different errors
else:
    # Code here runs if no exceptions occurred during the `try` block
finally:
    # Code here runs after all other blocks are complete (or skipped)
    # regardless of whether an exception occurs
```

Most frequently, you will only use the `try` and `except` blocks.

### Crashing Due to a `ZeroDivisionError`

If we run this code without error handling, eventually an exception will occur.

```python
from random import randrange
for i in range(100):
    x = randrange(10)
    y = randrange(10)
    print(f"{x} / {y} = {x / y}")
```

Output:

```
-- SNIP -- May be some successful iterations before an exception is thrown

Traceback (most recent call last):
  File "...\06_error_handling.py", line 12, in <module>
    print(f"{x} / {y} = {x / y}")
                         ~~^~~
ZeroDivisionError: division by zero
```

This is because `y` is a random number from `0` to `9`, and when it is `0` the
program is attempting to divide by zero. Division by zero is mathematically
undefined, so Python raises a `ZeroDivisionError`.

The code file has this loop commented out, so the rest of the file can run.
Uncomment it to see the crash for yourself.

---

### Handling a `ZeroDivisionError`

Using the `try` ... `except` pattern, we can avoid the program crashing.

While you can use an `except` block without specifying a type and allow it to
capture all exceptions, it's considered a best practice to specify the error
type you are handling and include code specific to that error type.

In this example, we're concerned with the possibility of a `ZeroDivisionError`.

```python
from random import randrange
for i in range(100):
    try:
        x = randrange(10)
        y = randrange(10)
        print(f"{x} / {y} = {x / y}")
    except ZeroDivisionError:
        print("Caught attempt to divide by zero...")
        print("Halting loop!\n")
        break
```

Output:

```
-- SNIP -- May be some successful iterations before an exception is thrown

Caught attempt to divide by zero...
Halting loop!

```

We've stopped the loop gracefully instead of crashing.

---

### Preventing a Crash Without Halting

Sometimes an error can occur, but the program should be allowed to continue.

In cases like this, we can still use the `try` ... `except` pattern to
prevent crashes while still allowing the program to continue:

```python
while True:
    print("Input numbers to divide or 'q' to quit.")
    first_number = input("\nFirst number:\n> ")
    if first_number == 'q':
        break
    second_number = input("Second number:\n> ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!\n")
    else:
        print(f"\n{first_number} / {second_number} = {answer}\n")
```

Output: (numbers are examples - yours will differ)

```
-- SNIP -- ... earlier iterations

Input numbers to divide or 'q' to quit.

First number:
> 7
Second number:
> 8

7 / 8 = 0.875

Input numbers to divide or 'q' to quit.

First number:
> 9
Second number:
> 0
You can't divide by zero!

-- SNIP -- ... later iterations

Input numbers to divide or 'q' to quit.

First number:
> q
```

---
