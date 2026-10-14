"""Copy to the clipboard and paste from it!"""

import pyperclip

# Copies to the clipboard
pyperclip.copy("Hello")

# Pastes from the clipboard
my_var = pyperclip.paste()
print(my_var)
