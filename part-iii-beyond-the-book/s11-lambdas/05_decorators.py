"""Lambdas as decorators"""

def trace(func: callable) -> callable:
    """Decorator to trace function calls"""
    def _trace(*args, **kwargs):
        print(f"[TRACE] func: {func.__name__}, args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return _trace

@trace
def add_two(x: int) -> int:
    """Add two numbers"""
    return x + 2

def main() -> None:
    """Main function"""
    print(add_two(3), "\n")

    print((trace(lambda x: x + 2))(3), "\n")

    print(list(map(trace(lambda x: x * 2), range(3))), "\n")

if __name__ == "__main__":
    main()
