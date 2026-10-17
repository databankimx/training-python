"""Lesson 2.1 - Formatting JSON Data"""

import json
from pathlib import Path
from relative_paths import get_path

# Read in data from JSON file
folder = "Data"
filename = "eq_data_1_day_09102023.json"
filepath = get_path(filename, folder)

contents = Path(filepath).read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Reformat the JSON data and store as a new file
formatted_filename = "readable_" + filename
formatted_filepath = get_path(formatted_filename, folder)

path = Path(formatted_filepath)
# The indent argument sets how many spaces are added for each level of indentation
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding="UTF-8")
