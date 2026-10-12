"""Assignment 8.9"""

# Messages: Make a list containing a series of short text messages.
#           Pass the list to a function called `show_messages()`,
#           which prints each text message.

print("Try-it-Yourself:")
print("Assignment 8.9")

def show_messages(messages):
    """Print each message from the list"""
    for message in messages:
        print(message)

my_messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
show_messages(my_messages)
