"""Lesson 10.16"""

import json

print("Chapter 10:")
print("Bonus - Classes and the __dict__ Property\n")

class Thing:
    """Models some thing"""

    def __init__(self, size: str, color: str) -> None:
        """Initialize the class attributes"""
        self.size = size
        self.color = color

def main():
    """Testing Function"""
    my_thing = Thing("Large", "Blue")

    # This would return a TypeError
    # print(json.dumps(my_thing, indent=4))

    print(json.dumps(my_thing.__dict__, indent=4))

    # print(json.dumps(
    #     {
    #         "type": "Thing",
    #         "name": "my_thing",
    #         "attributes": my_thing.__dict__
    #     },
    #     indent=4
    # ))

if __name__ == "__main__":
    main()
