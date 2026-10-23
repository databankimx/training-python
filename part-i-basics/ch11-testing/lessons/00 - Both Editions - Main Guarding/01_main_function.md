## Using a `main()` Function

Even though we have learned to create functions, classes, and modules, so far 
the parts of our code that have called those functions have been left in loose
scripts that just run when we execute the Python file.

So, for example, we might have a Python file with this content:

`hello.py`

```python
def say_hello():
    print("Hello World!")

say_hello()
```

We can execute this just fine, but if the function was useful and we wanted to 
import it in another file, we would have a problem.

`other_file.py`

```python
import hello
```

As soon as we call that import, it reads the contents of `hello.py`, and while 
it will successfully import the `say_hello()` function, we see an unexpected bit of output:

```
Hello World!
```

Wait a minute. We ran `other_file.py` but `hello.py` executed.

What gives?

---

### Python is an Interpreted Language

Remember that Python is interpreted. That means that the Python executable is
just processing all of the lines of the executed code.

When we import a module, all of its code is processed as well. That's fine for
functions, since they just get stored in memory for us to use later.

But code outside of functions will execute, which we don't want when importing.

---

### Migrating into a `main()` Function

The best practice technique is to migrate all code (with the exception of 
imports and global variables) into a function called `main()`.

After doing that, our file looks like this:

`hello.py`

```python
def say_hello():
    print("Hello World!")

def main():
    say_hello()
```

This protects against the call to `say_hello()` executing when we import the
module.

---

### How to Call `main()` to Execute a Script

But now we have a new problem. When we run `hello.py` nothing happens. This is
because we are never calling the `main()` function itself.

By now you've probably realized that we can't just add a call to `main()` ...

[`hello_no_guard.py`](./hello_no_guard.py)

```python
def say_hello():
    print("Hello World!")

def main():
    say_hello()

main()
```

... or we'll be back to the original problem of the code executing when we 
import the module.

```python
import hello_no_guard
```

Output:

```
Importing unguarded module:

Hello World!
```

So, how do we safely call main() when we run this file, but not when we import
it into another?

---

### Main Guarding with `__name__ == "__main__"`

When a Python script executes, a number of magic properties are populated. One
of these is `__name__`.

When a module is the main file you executed, its instance of `__name__` will be
equal to `"__main__"`. For any imported module, on the other hand, `__name__` 
will be equal to the name of the module, so in our example, if we call
`import hello`, in hello.py, the `__name__` property will equal `"hello"`.

We can use this to our advantage by using a pattern known as *main guarding*.

By checking to see that `__name__` is `"__main__"` before we call the `main()`
function, we allow the code to execute when we want it to but not when we 
don't.

With a main guard in place, our file looks like this:

[`hello_with_guard.py`](./hello_with_guard.py)

```python
def say_hello():
    print("Hello World!")

def main():
    say_hello()

if __name__ == "__main__":
    main()
```

Let's test...

```python
print("Importing guarded module:\n")
import hello_with_guard
```

Output:

```
Importing guarded module:
```

And it's just that simple.

---

### The Moral

You should always:

* Migrate all operational code into functions
* Migrate all calls to those functions into a `main()` function
* Guard the call to the `main()` function behind `__name__ == "__main__"`

---

### A Template

This gives us a basic template for the structure of a Python file

```python
# imports go here

# global variables and constants go here

def my_function(*args, **kwargs):
    # operational code goes here

def main():
    # function-consuming code goes here

if __name__ == "__main__":
    main()
```

A simplified version of this template is in the ready-made snippet file
[python.json](../../../../resources/snippets/python.json)
included in this repository, which can be imported into VS Code and accessed
by typing `&template` in any Python code file.

> Note: the code file turns off Pylint's `unused-import` and
> `import-outside-toplevel` warnings in `main()`. Those comments stay in the code
> file. The code file also pauses between sections, and clears the terminal
> before each section.

---
