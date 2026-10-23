"""Module to test the Trie class"""

from trie import Trie
from sm_utils import timer, clear_terminal, pause

@timer
def initialize_trie(file_name: str, folder: str | None = None) -> Trie:
    """Initialize the Trie for testing"""
    print("\nInitializing...")
    t = Trie()
    t.load_words(file_name, folder)
    print("Ready...\n")
    return t

def main() -> None:
    """Main executable entry point"""
    clear_terminal()
    t = initialize_trie("words.txt", "data")
    pause()
    clear_terminal()
    print("\n\nList of words that start with 'appall':\n")
    t.list_words("appall")
    pause()

    while True:
        clear_terminal()
        word = input("\nEnter a word to search (letters only)" + \
                     ", -word to delete it, or press <ENTER> to quit:\n> ").lower()
        print()
        if word == "":
            clear_terminal()
            print("\nGoodbye...\n")
            break
        if word.startswith("-"):
            target = word[1:]
            if not target.isalpha():
                print("\nPlease enter letters only!\n")
                pause()
                continue
            if t.delete(target):
                print(f"'{target}' has been deleted from the trie...\n")
            else:
                print(f"'{target}' is not in the trie, so nothing was deleted...\n")
            pause()
            continue
        if not word.isalpha():
            print("\nPlease enter letters only!\n")
            pause()
            continue
        result = "" if t.search(word) else "not "
        print(f"'{word}' is {result}in the dictionary...\n")
        pause()

if __name__ == "__main__":
    main()
