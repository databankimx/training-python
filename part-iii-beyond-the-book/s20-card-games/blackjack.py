"""Models a game of blackjack"""

import sys
from sm_utils import clear_terminal, pause
from deck import Deck
from hand import Hand
from ranks import Ranks
from colors import Colors

class Blackjack():
    """Models a game of blackjack"""

    INITIAL_BANKROLL = 5_000
    DEALER_STANDS = 17

    def __init__(self, color: Colors = Colors.WHITE) -> None:
        """Initialize"""
        self.game = "blackjack"
        self.color = color
        self.deck: Deck | None = None
        self.player_hands: list[Hand] | None = None
        self.dealer_hand: Hand | None = None
        self.player_bankroll: int
        self.reset_bankroll()

    def play(self) -> None:
        """Play hands until the player runs out of money or quits"""
        self.show_rules()
        pause()
        while True:
            if self.player_bankroll < 1:
                self.game_over(True)
            bet = self.place_bet()
            self.deal_hand()
            self.play_hand(bet)

    def play_hand(self, bet: int) -> None:
        """Play the player's turn and the dealer's turn, then settle the bet"""
        player = self.player_hands[0]
        if self.is_blackjack(player) or self.is_blackjack(self.dealer_hand):
            self.dealer_hand.hidden = []
            self.show_hands()
            if self.is_blackjack(player) and self.is_blackjack(self.dealer_hand):
                return self.settle("push", bet)
            if self.is_blackjack(player):
                return self.settle("blackjack", bet)
            return self.settle("lose", bet)

        bet = self.player_turn(bet)
        if self.hand_value(player) > 21:
            return self.settle("lose", bet)
        self.dealer_turn()
        player_total = self.hand_value(player)
        dealer_total = self.hand_value(self.dealer_hand)
        if dealer_total > 21 or player_total > dealer_total:
            return self.settle("win", bet)
        if player_total < dealer_total:
            return self.settle("lose", bet)
        return self.settle("push", bet)

    def player_turn(self, bet: int) -> int:
        """Let the player hit, stand, or double down; return the final bet"""
        player = self.player_hands[0]
        while True:
            self.show_hands()
            if self.hand_value(player) >= 21:
                return bet
            can_double = len(player.cards) == 2 and self.player_bankroll >= 2 * bet
            options = "(H)it or (S)tand" + (" or (D)ouble down" if can_double else "")
            choice = input(f"{options}?\n> ")[:1].lower()
            if choice == "s":
                return bet
            if choice == "h":
                self.draw(player)
            elif choice == "d" and can_double:
                self.draw(player)
                self.show_hands()
                return bet * 2

    def dealer_turn(self) -> None:
        """Reveal the dealer's hidden card and hit until reaching the stand value"""
        self.dealer_hand.hidden = []
        self.show_hands()
        while self.hand_value(self.dealer_hand) < Blackjack.DEALER_STANDS:
            self.draw(self.dealer_hand)
            self.show_hands()

    def settle(self, outcome: str, bet: int) -> None:
        """Pay out or collect the bet and report the result"""
        if outcome == "push":
            print("Push: your bet is returned.")
        elif outcome == "lose":
            self.player_bankroll -= bet
            print(f"You lose ${bet:,}.")
        else:
            winnings = bet * 3 // 2 if outcome == "blackjack" else bet
            self.player_bankroll += winnings
            print(f"You win ${winnings:,}!")
        pause()

    def draw(self, hand: Hand) -> None:
        """Deal one card to a hand, reshuffling a fresh deck if the current one is empty"""
        if not self.deck.cards:
            self.deck = Deck(self.game, self.color)
        self.deck.deal(hand, 1)

    def is_blackjack(self, hand: Hand) -> bool:
        """Check for a two-card 21, counting any hidden cards"""
        full_hand = Hand(self.game, cards=hand.cards)
        return len(full_hand.cards) == 2 and self.hand_value(full_hand) == 21

    def place_bet(self) -> int:
        """Let the player place a bet"""
        while True:
            clear_terminal()
            print(f"You have ${self.player_bankroll:,} remaining...\n")
            print(f"How much do you want to bet? (1 - {self.player_bankroll:,}, or [q]uit)")
            entry = input("> ")
            if entry == "":
                continue
            if not entry.isdigit():
                if entry[0].lower() == "q":
                    self.game_over()
                continue
            bet = int(entry)
            if 1 <= bet <= self.player_bankroll:
                return bet

    def deal_hand(self) -> None:
        """Deal the initial two cards to the dealer and player"""
        if self.deck is None or len(self.deck.cards) < 10:
            self.deck = Deck(self.game, self.color)
        self.player_hands, self.dealer_hand = [Hand(self.game)], Hand(self.game, cards=[])
        for _ in range(2):
            for hand in [self.player_hands[0], self.dealer_hand]:
                self.deck.deal(hand, 1)
        self.dealer_hand.hidden = [1]

    def reset_bankroll(self) -> None:
        """Reset the player's bankroll back to the default value"""
        self.player_bankroll = Blackjack.INITIAL_BANKROLL

    def show_rules(self) -> None:
        """Display the blackjack rules"""
        print("Blackjack")
        print("Rules:")
        print("  Try to get as close to 21 without going over.")
        print("  Kings, Queens, and Jacks are worth 10 points.")
        print("  Aces are worth 1 or 11 points.")
        print("  Cards 2 through 10 are worth their face value.")
        print("  (H)it to take another card.")
        print("  (S)tand to stop taking cards.")
        print("  On your first play, you can (D)ouble down to increase your" + \
              " bet but must hit exactly one more time before standing.")
        print("  A two-card 21 is a blackjack and pays 3 to 2.")
        print("  In case of a tie, the bet is returned to the player.")
        print("  The dealer stops hitting at 17.")

    def game_over(self, lost: bool = False) -> None:
        """Close out the game"""
        if lost:
            print("You're broke!\nGood thing you weren't playing with real money.")
        print("Thanks for playing!")
        sys.exit(0)

    def hand_value(self, hand: Hand) -> int:
        """Get the value of the given hand, counting aces as 11 where that fits"""
        val = hand.value
        for _ in range(hand.count(Ranks.ACE)):
            if val <= 11:
                val += 10
        return val

    def show_hands(self) -> None:
        """Show the player's and dealer's hands"""
        print(f"Dealer: {self.hand_value(self.dealer_hand)}" + \
              f"{' + ??' if self.dealer_hand.hidden else ''}")
        self.dealer_hand.show()
        p_val = self.hand_value(self.player_hands[0])
        print(f"\nPlayer: {p_val}", end="")
        if p_val > 21:
            print(" (Busted!)")
        elif p_val == 21 and len(self.player_hands[0].cards) == 2:
            print(" (Blackjack!)")
        else:
            print()
        self.player_hands[0].show()
        print()

def main() -> None:
    """Run the game"""
    Blackjack().play()

if __name__ == "__main__":
    main()
