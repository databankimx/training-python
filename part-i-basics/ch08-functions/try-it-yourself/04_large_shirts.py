"""Assignment 8.4"""

# Large Shirts: Modify the `make_shirt()` function so that shirts
#               are large by default with a message that reads
#               "I love Python." Make a large shirt and a medium
#               shirt with the default message, and a shirt of any
#               size with a different message.

print("Try-it-Yourself:")
print("Assignment 8.4")

def make_shirt(size="large", message="I ♥  Python"):
    """Print a message describing a shirt order"""
    print(f"You ordered a {size} t-shirt saying '{message}'.")

my_size = "medium"
my_message = "I ♥  Coding"
make_shirt()
make_shirt(size=my_size)
make_shirt(message=my_message)
