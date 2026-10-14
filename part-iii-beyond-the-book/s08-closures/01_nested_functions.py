"""Nested functions"""

def outer_function() -> None:
    """Executes the inner function"""
    def inner_function() -> None:
        print("Hello World!\n")
    inner_function()

def outer_function_with_args(name: str) -> None:
    """Executes the inner function (sharing variable 'name')"""
    def inner_function() -> None:
        print(f"Hello {name.title()}!\n")
    inner_function()

def add(x: int, y: int) -> int:
    """Adds two numbers"""
    return x + y

def calculate(func: callable, x: int, y: int) -> int:
    """Calls the given function with the given arguments"""
    return func(x, y)

def greeting(name: str) -> callable:
    """Returns a function that greets a user"""
    def hello() -> None:
        print(f"Hello {name.title()}!\n")
    return hello

def main() -> None:
    """Main function"""
    outer_function()
    outer_function_with_args("Scott")
    x, y, = 2, 3
    z = calculate(add, x, y)
    print(f"{x} + {y} = {z}\n")
    hello_scott = greeting("Scott")
    hello_scott()

if __name__ == "__main__":
    main()
