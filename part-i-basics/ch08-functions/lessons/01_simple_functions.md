## Functions

Up to this point, we have written code line-by-line whenever it was needed, and when we executed a
Python file, our code just ran from top to bottom.

In the real world, we will almost always want to create our code using functions. A function is a
named block of code that does a specific task.

Functions allow us to write reusable code, which:

* Helps avoid redundancy (writing similar code repeatedly)
* Ensures that we can make changes in one place instead of many

Avoiding redundancy and ensuring maintainability are among the important goals of good programmers.

---

### A Simple Function

Functions are defined using the `def` keyword.

Syntax:  
`def function_name():`

As you can see, the function declaration ends with a colon `:`  
Just like loops and conditionals, this is a block indicator, so all lines inside the function are
indented.

> Note:
>
> When implemented in a top-down script, functions must be declared before they are called.
>
> Many of the examples later in this chapter put their code in a `main()` function, which keeps the
> top level of a file tidy. It's a convention, not a requirement.

Typically, the first line inside a function is called a documentation or "doc" string, surrounded by
triple quotes: `"""doc string"""`.

```python
def greet_user():
    """Display a simple greeting"""
    print("\nHello!")
```

You execute a function in your code by calling it by name:

```python
greet_user()
```

Output:

```
Hello!
```

The docstring is stored with the function, so you can read it back with `__doc__`:

```python
print(greet_user.__doc__)
```

Output:

```
Display a simple greeting
```

---

