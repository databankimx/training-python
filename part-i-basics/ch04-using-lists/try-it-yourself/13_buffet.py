"""Assignment 4.13"""

# Buffet: Think of five simple foods, store them in a tuple,
#         loop over them, try to modify one, then replace the tuple.

print("Try-it-Yourself:")
print("Assignment 4.13")

menu = ("sandwich", "pastry", "coffee", "tea", "bagel")
print("Menu:")
for food in menu:
    print(f" - {food}")

# Uncomment this line to see the immutability error:
# menu[0] = "toast"

menu = ("toast", "pastry", "coffee", "tea", "yoghurt")
print("Updated Menu:")
for food in menu:
    print(f" - {food}")
