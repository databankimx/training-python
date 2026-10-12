"""Lesson 8.16"""

# pylint: disable=dangerous-default-value
def my_bad_function(my_arg: list[str]=[]) -> list[str]:
    """Demonstrate the result of a default mutable argument"""
    print("Using an empty list as a default argument:")
    my_arg.append("new item")
    print(my_arg, "\n")
    return my_arg

def my_good_function(my_arg: list[str]=None) -> list[str]:
    """Demonstrate the result of a default None argument"""
    print("Using `None` as a default argument:")
    if my_arg is None:
        my_arg = []
    my_arg.append("new item")
    print(my_arg, "\n")
    return my_arg

def counter(func: callable) -> callable:
    """Counts the number of calls to the passed function"""
    def _counter(*args, **kwargs):
        _counter.calls += 1
        return func(*args, **kwargs)
    _counter.calls = 0
    return _counter

# pylint: disable=dangerous-default-value
@counter
def fibonacci(n: int, memo: dict[int, int]={0: 0, 1: 1}) -> int:
    """Return the nth Fibonacci number (memoized algorithm)"""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def run_repeat(repeat: int, functions: list[callable], *args, **kwargs) -> dict[str, callable]:
    """Execute a list of functions, repeating each a specified number of times"""
    ret = {}
    for function in functions:
        print(f"\nFunction: {function.__name__}")
        for i in range(repeat):
            ret[f"{function.__name__}_{i}"] = function(*args, **kwargs)
    return ret

def main() -> None:
    """Main program"""
    run_repeat(3, [my_bad_function, my_good_function])
    n = 40
    for _ in range(2):
        fibonacci.calls = 0
        print(f"F({n}) = {fibonacci(n)} : {fibonacci.calls} call(s)\n")

if __name__ == "__main__":
    main()
