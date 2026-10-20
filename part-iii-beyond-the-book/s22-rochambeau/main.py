"""Test Rochambeau (Rock, Paper, Scissors) Game"""

from rock_paper_scissors import RockPaperScissors

def main():
    """Start the game"""
    answer = input("Should the computer use a strategy? (Y|N)\n> ")[:1].lower()
    RockPaperScissors({"y": True, "n": False}.get(answer)).play()

if __name__ == "__main__":
    main()
