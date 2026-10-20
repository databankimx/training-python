"""Assignment 5.6"""

# Stages of Life: if-elif-else chain that determines a person's stage of life.
#   < 2: baby | 2-3: toddler | 4-12: kid | 13-19: teenager
#   20-64: adult | 65+: elder

print("Try-it-Yourself:")
print("Assignment 5.6")

age = int(input("Enter your age: "))
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")
