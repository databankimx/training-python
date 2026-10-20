prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(message)
