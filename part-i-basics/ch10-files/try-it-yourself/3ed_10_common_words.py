"""Assignment 10.10 (3rd Edition)"""

# Common Words: Visit Project Gutenberg (https:// gutenberg.org/) and find
#               a few texts you'd like to analyze. Download the text files
#               for these works, or copy the raw text from your browser
#               into a text file on your computer. You can use the count()
#               method to find out how many times a word or phrase appears
#               in a string. For example, the following code counts the
#               number of times 'row' appears in a string:
#               ------------------------------------
#               >>> line = "Row, row, row your boat"
#               >>> line.count('row')
#               2
#               >>> line.lower().count('row')
#               3
#               ------------------------------------
#               Notice that converting the string to lowercase using lower()
#               catches all appearances of the word you're looking for,
#               regardless of how it's formatted. Write a program that reads
#               the files you found at Project Gutenberg and determines how
#               many times the word 'the' appears in each text. This will be
#               an approximation because it will also count words such as
#               'then' and 'there'. Try counting 'the ', with a space in the
#               string, and see how much lower your count is.

from pathlib import Path
from relative_paths import get_path

def examine_file(filename, search_words):
    """Count word occurrences in file passed"""
    file_path = get_path(filename, "Files")
    terminators = [" ", ".", ",", "?", "\n"]

    try:
        file = Path(file_path)
        content = file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nFile {filename} could not be found!")
    else:
        print(f"\nWord analysis in [{filename}]:")
        for word in search_words:
            num = 0
            for start_term in terminators:
                for end_term in terminators:
                    num += content.count(f"{start_term}{word}{end_term}")
            print(f"{word}: {num}")

print("Try-it-Yourself:")
print("Assignment 10.10")

file_names = ["frankenstein.txt", "little_fuzzy.txt",
              "star_hunter.txt", "snow_crash.txt", "the_republic.txt"]
search_terms = ["man", "woman", "person"]

for file_name in file_names:
    examine_file(file_name, search_terms)
