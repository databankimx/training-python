"""Assignment 8.11"""

# Archived Messages: Start with your work from Exercise 8.10. Call
#                    the function `send_messages()` with a copy of
#                    the list of messages. After calling the function,
#                    print both of your lists to show that the
#                    original list has retained its messages.

print("Try-it-Yourself:")
print("Assignment 8.11")

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
send_messages(my_messages[:], my_sent_messages)
print("Messages:\n", my_messages)
print("Sent Messages:\n", my_sent_messages)
