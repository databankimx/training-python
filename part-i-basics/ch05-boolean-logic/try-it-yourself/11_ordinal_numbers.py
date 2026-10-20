"""Assignment 5.11"""

# Ordinal Numbers: Store 1-9 in a list. Loop and print each with the
#                  correct ordinal suffix (1st, 2nd, 3rd, 4th...).

print("Try-it-Yourself:")
print("Assignment 5.11")

numerals = list(range(1, 10))
for numeral in numerals:
    if numeral == 1:
        suffix = "st"
    elif numeral == 2:
        suffix = "nd"
    elif numeral == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{numeral}{suffix}")
