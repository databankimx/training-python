"""Assignment 8.3"""

# T-Shirt: Write a function called `make_shirt()` that accepts a
#          size and the text of a message that should be printed
#          on the shirt. The function should print a sentence
#          summarizing the size of the shirt and the message printed
#          on it. Call the function once using positional arguments
#          to make a shirt. Call the function a second time using
#          keyword arguments.

print("Try-it-Yourself:")
print("Assignment 8.3")

def make_shirt(size, message):
    """Print a message describing a shirt order"""
    print(f"You ordered a {size} t-shirt saying '{message}'.")

my_size = "large"
my_message = "I ♥  Python"
make_shirt(my_size, my_message)
make_shirt(message=my_message, size=my_size)
