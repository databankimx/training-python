"""Test the morse code encoder and decoder"""

import sys
from morse import Morse

def prog(morse: Morse) -> None:
    """Run the interactive encoder/decoder until the user quits"""
    print("Morse code notes:")
    print("  * Letters are separated by a single space.")
    print("  * ■ marks a space between words.")
    print("  * □ marks a character that has no Morse code.")
    while True:
        task = input("\nSelect a task: ([e]ncode, [d]ecode, [q]uit)\n> ")[:1].lower()
        if task == "q":
            break
        if task not in ("e", "d"):
            print("Invalid selection!")
            continue
        action = morse.encode if task == "e" else morse.decode
        prefix = "en" if task == "e" else "de"
        print(action(input(f"Enter the message to {prefix}code:\n> ")))

def demo(morse: Morse) -> None:
    """Run a set of example encodings and decodings"""
    print(morse.decode("... --- ..."))
    print(morse.encode("SOS"))
    print(morse.decode("... -.-. --- - -_-- -.-. .-.. . .- -."))
    print(morse.encode("Scott McLean"))
    print(morse.encode("Scott McLean: 'Enjoyer of Python'"))
    print(morse.encode("ABCDEFCHIJKLMNOPQRSTUVWXYZ1234567890.,?;:-/'\"()_"))
    print(morse.encode("~"))

def main() -> None:
    """Run the program, or the demo if 'demo' is given on the command line"""
    morse = Morse()
    if "demo" in sys.argv[1:]:
        demo(morse)
    else:
        prog(morse)

if __name__ == "__main__":
    main()
