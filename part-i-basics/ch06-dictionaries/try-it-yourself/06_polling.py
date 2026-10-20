"""Assignment 6.6"""

# Polling: Make a list of people who should take the languages poll.
#          Include some who have and some who haven't. Thank or invite accordingly.

print("Try-it-Yourself:")
print("Assignment 6.6")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people = ["jen", "sarah", "adam", "edward", "eleanor", "phil"]
for name in people:
    if name in favorite_languages:
        print(f"Hi {name.title()}! Thanks for taking the poll.")
    else:
        print(f"Hi {name.title()}, please take the poll.")
