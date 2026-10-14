"""Closures in Loops"""

def wrapped_function(n: int) -> callable:
    """Simple wrapper for a closure"""
    def func() -> None:
        """The inner function captures n as a closure"""
        print(n, end=" ")
    return func

def call_wrapped_function() -> None:
    """Consume the wrapped function"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        funcs.append(wrapped_function(n))
    for func in funcs:
        func()
    print()

def call_wrapped_lambda() -> None:
    """Consume a wrapped lambda"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        # pylint: disable=cell-var-from-loop
        funcs.append(lambda: print(n, end=" "))
    for func in funcs:
        func()
    print()

def call_wrapped_lambda_defined() -> None:
    """Consume a wrapped lambda with the free variable defined"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        funcs.append(lambda n=n: print(n, end=" "))
    for func in funcs:
        func()
    print()

def main() -> None:
    """Main function"""
    call_wrapped_function()
    print()

    call_wrapped_lambda()
    print()

    call_wrapped_lambda_defined()

if __name__ == "__main__":
    main()
