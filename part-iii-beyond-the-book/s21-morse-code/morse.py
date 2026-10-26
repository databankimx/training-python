"""Morse code encoder/decoder"""

#pylint: disable=line-too-long, too-many-arguments, too-many-positional-arguments

from node import Node

# Each character and its Morse code, where "." is a dot and "-" is a dash
CODES = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", ";": "-.-.-.", ":": "---...",
    "-": "-....-", "/": "-..-.", "'": ".----.", "\"": ".-..-.", "!": "-.-.--",
    "(": "-.--.", ")": "-.--.-", "_": "..--.-",
}

UNKNOWN = "□"

class Morse:
    """Implement a Morse code encoder/decoder using a binary tree"""

    def __init__(self) -> None:
        """Build the tree by walking each character's code from the root"""
        self.tree = Node(None)
        for char, code in CODES.items():
            node = self.tree
            for symbol in code:
                attr = "left" if symbol == "." else "right"
                if getattr(node, attr) is None:
                    setattr(node, attr, Node(None))
                node = getattr(node, attr)
            node.value = char

    def decode(self, encoded: str, delimiter: str = " ", separator: str = "_",
               invalid_char_sub: str = UNKNOWN, space_char_sub: str = "■") -> str:
        """Decode Morse code to letters"""
        # Give every word break and unknown character its own token, so the
        # encoder's substitutions decode the same as the separator
        spaced = encoded.replace(separator, f" {separator} ") \
            .replace(space_char_sub, f" {separator} ") \
            .replace(invalid_char_sub, f" {invalid_char_sub} ")
        words = [""]
        for token in spaced.split(delimiter):
            if token == separator:
                words.append("")
            elif token == invalid_char_sub:
                words[-1] += invalid_char_sub
            elif token:
                words[-1] += self.decode_code(token)
        return " ".join(word for word in words if word)

    def decode_code(self, code: str) -> str:
        """Follow a dot or dash path from the root to find one character"""
        node = self.tree
        for symbol in code:
            assert symbol in ".-"
            node = node.left if symbol == "." else node.right
            if node is None:
                return UNKNOWN
        # Internal nodes that are not the end of any code have no character
        return node.value if node.value is not None else UNKNOWN

    def encode(self, message: str, delimiter: str = " ", invalid_char_sub: str = UNKNOWN,
               space_char_sub: str = "■") -> str:
        """Encode letters to Morse code"""
        codes = []
        for char in message.upper():
            if char == " ":
                codes.append(space_char_sub)
            elif char in CODES:
                encoded: list[str] = []
                self.get_code(self.tree, char, encoded)
                codes.append("".join(encoded))
            else:
                codes.append(invalid_char_sub)
        return delimiter.join(codes) \
            .replace(f" {invalid_char_sub} ", invalid_char_sub) \
            .replace(f" {space_char_sub} ", space_char_sub)

    def get_code(self, node: Node | None, character: str, code: list[str]) -> bool:
        """Search the tree for a character, building its code on the way back"""
        if node is None:
            return False
        if node.value == character:
            return True
        if self.get_code(node.left, character, code):
            code.insert(0, ".")
            return True
        if self.get_code(node.right, character, code):
            code.insert(0, "-")
            return True
        return False
