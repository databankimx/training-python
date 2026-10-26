"""Lesson 8.13"""

print("Chapter 8:")
print("Exercise 13 - Bonus Lesson - Type Hints")

#pylint: disable=anomalous-backslash-in-string, too-many-return-statements

def calculate(operation: str, x: int | float, y: int | float) -> int | float | None:
    """Perform selected arithmetic calculation.

    Args:
        operation: Arithmetic operation to perform on the provided operands.
            * \[a\]dd
            * \[s\]ubtract
            * \[m\]ultiply
            * \[d\]ivide  
            
        x: Left numerical operand.
        y: Right numerical operand.

    Returns:
        The result of the arithmetic operation, or None if it can't be performed.
    """
    if not operation:
        print("No operation was given.")
        return None

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
        if y == 0:
            print("Cannot divide by zero.")
            return None
        return x / y

    print(f"Operation [{operation}] not supported!")
    return None


a = 3
b = 2
print(f"{a} + {b} = {calculate('add', a, b)}")
print(f"{a} - {b} = {calculate('subtract', a, b)}")
print(f"{a} * {b} = {calculate('multiply', a, b)}")
print(f"{a} / {b} = {calculate('divide', a, b)}")
