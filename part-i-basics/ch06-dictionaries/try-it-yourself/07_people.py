"""Assignment 6.7"""

# People: Make two more person dictionaries, store all three in a list called
#         people. Loop through and print everything about each person.

print("Try-it-Yourself:")
print("Assignment 6.7")

person1 = {"first_name": "Marcus", "last_name": "Reyes", "age": 38, "city": "Toledo"}
person2 = {"first_name": "Jeremy", "last_name": "McLean", "age": 47, "city": "Columbus"}
person3 = {"first_name": "Hillary", "last_name": "Taylor", "age": 50, "city": "Twinsburg"}
people = [person1, person2, person3]
for person in people:
    print()
    for key, value in person.items():
        print(f"{key} = {value}")
