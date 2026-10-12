"""Lesson 8.11"""

print("Chapter 8:")
print("Exercise 13 - Bonus Lesson - Type Hints")

def calculate(operation: str, x: int|float, y: int|float) -> int|float:
    """
    Perform selected arithmetic calculation

    Parameters:  
    **operation**: Arithmetic operation to perform on the provided operands
    * [a]dd
    * [s]ubtract
    * [m]ultiply
    * [d]ivide  

    **x**: Left numerical operand  
    **y**: Right numerical operand

    **Returns**:  
    the result of the arithmetic operation
    """
    op = operation[0].lower()
    if op == "a":
        # add
        return x + y
    if op == "s":
        # subtract
        return x - y
    if op == "m":
        # multiply
        return x * y
    if op == "d":
        # divide
        return x / y

    print(f"Operation [{operation}] not supported!")
    return None

a = 3
b = 2
print(f"{a} + {b} = {calculate('add', a, b)}")
print(f"{a} - {b} = {calculate('subtract', a, b)}")
print(f"{a} * {b} = {calculate('multiply', a, b)}")
