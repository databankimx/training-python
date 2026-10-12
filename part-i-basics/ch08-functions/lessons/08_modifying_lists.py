"""Lesson 8.8"""

print("Chapter 8:")
print("Exercise 8 - Modifying Lists with Functions")

def print_models(unprinted, completed):
    """
    Simulate printing each design, until none are left.
    Move each design to completed after printing.
    """
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)
        
def show_completed_models(completed):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed:
        print(completed_model)

def pause():
    """Wait for user to press <ENTER>"""
    input("\nPress <ENTER> to continue\n")

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

pause()

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
