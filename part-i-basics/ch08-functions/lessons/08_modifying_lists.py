"""Lesson 8.8"""

print("Chapter 8:")
print("Exercise 8 - Modifying Lists with Functions")


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")


my_unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
my_completed_models = []

print_models(my_unprinted_designs, my_completed_models)
show_completed_models(my_completed_models)
print(my_unprinted_designs)

pause()

my_unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
my_completed_models = []

print_models(my_unprinted_designs[:], my_completed_models)
show_completed_models(my_completed_models)
print(my_unprinted_designs)
