"""Assignment 10.7 (2nd Edition)"""

# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
#                      so the user can continue entering numbers even if
#                      they make a mistake and enter text instead of a
#                      number.

print("Try-it-Yourself:")
print("Assignment 10.7\n")

active = True

while True:
    print("Enter two integers and I will add them.")

    numbers = []

    while len(numbers) < 2:
        response = input("Enter a number:\n> ")
        if response is None or len(response) < 1:
            print("You cannot leave the entry blank.")
            continue
        if response.lower()[0] == "q":
            active = False
            break
        try:
            number = int(response)
            numbers.append(number)
        except ValueError:
            print("Please only enter numbers.")

    if not active:
        break

    my_sum = numbers[0] + numbers[1]
    print(f"\n{numbers[0]} + {numbers[1]} = {my_sum}\n")

print("\nGoodbye...\n")
