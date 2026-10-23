"""Rochambeau (Rock, Paper, Scissors) Game"""

#pylint: disable=line-too-long

from random import choice, getrandbits

# Each action maps to the action it beats; BEATEN_BY is the inverse
BEATS = {"r": "s", "p": "r", "s": "p"}
BEATEN_BY = {beaten: beater for beater, beaten in BEATS.items()}
NAMES = {"r": "rock", "p": "paper", "s": "scissors"}

class RockPaperScissors:
    """Defines a Rochambeau game"""

    def __init__(self, use_strategy: bool | None = None) -> None:
        """Set up the game; if no strategy is chosen, flip a coin"""
        self.use_strategy = bool(getrandbits(1)) if use_strategy is None else use_strategy
        self.last_player = self.last_computer = None
        self.last_result = "ties"
        print("Welcome to Rochambeau (Rock, Paper, Scissors)!")

    def computer_choice(self) -> str:
        """Choose the computer's action, using win-stay/lose-shift if active"""
        if self.use_strategy and self.last_result == "wins":
            # The player will likely shift to what beats our last play
            return BEATEN_BY[BEATEN_BY[self.last_computer]]
        if self.use_strategy and self.last_result == "loses":
            # The player will likely stay, so beat their last play
            return BEATEN_BY[self.last_player]
        return choice(list(BEATS))

    def turn(self, player: str) -> None:
        """Play one turn and report the computer's result"""
        computer = self.computer_choice()
        self.last_player, self.last_computer = player, computer
        if computer == player:
            self.last_result = "ties"
        elif BEATS[computer] == player:
            self.last_result = "wins"
        else:
            self.last_result = "loses"
        print(f"Computer chooses {NAMES[computer]} and {self.last_result}\n")

    def play(self) -> None:
        """Play turns until the player quits"""
        while True:
            player = ""
            while player not in ("r", "p", "s", "q"):
                player = input("Enter your choice: ([r]ock, [p]aper, [s]cissors, [q]uit\n> ")[:1].lower()
            if player == "q":
                break
            self.turn(player)

if __name__ == "__main__":
    RockPaperScissors().play()
