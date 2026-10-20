"""A module containing name-formatting functions"""

# This function will fail both tests
# def formatted_name(first: str, last: str, middle: str | None="") -> str:
#     """Generate a neatly formatted full name."""
#     ...

# This function will fail the test without a middle name argument
# def formatted_name(first: str, last: str, middle: str | None="") -> str:
#     """Generate a neatly formatted full name."""
#     full_name =  f"{first} {middle} {last}"
#     return full_name.title()

# This function will pass both tests
def formatted_name(first: str, last: str, middle: str | None="") -> str:
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
