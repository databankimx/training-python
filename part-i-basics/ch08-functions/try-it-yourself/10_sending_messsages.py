"""Assignment 8.10"""

# Sending Messages: Start with a copy of your program from Exercise 8.9.
#                   Write a function called `send_messages()` that prints
#                   each text message and moves each message to a new list
#                   called `sent_messages` as it's printed. After calling
#                   the function, print both of your lists to make sure
#                   the messages were moved correctly.

print("Try-it-Yourself:")
print("Assignment 8.10")

def show_messages(messages):
    """Print each message from the list"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Move messages to sent_messages list"""
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)

my_messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
my_sent_messages = []
send_messages(my_messages, my_sent_messages)
print("Messages:\n", my_messages)
print("Sent Messages:\n", my_sent_messages)
