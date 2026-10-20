"""Assignment 4.4"""

# One Million: Make a list of the numbers from one to one million,
#              and then use a for loop to print the numbers.

print("Try-it-Yourself:")
print("Assignment 4.4")

million = list(range(1, 1_000_001))

# Printing just the first and last five to avoid flooding the terminal
for num in million[:5] + million[-5:]:
    print(num)

# Uncomment this block to print all one million numbers
# for num in million:
#     print(num)
