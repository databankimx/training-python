"""Tests for the deck and hand classes"""

from sm_utils import clear_terminal, pause
from deck import Deck

def main() -> None:
    """Main function"""
    deck = Deck("poker")

    # View deck
    clear_terminal()
    for i in range(4):
        for r in range(5):
            for j in range(13):
                card = deck.cards[i * 13 + j]
                data = card.ascii[r] if r < 4 else f"{str(card):>3}  "
                print(data, end = " ")
            print()
        print()
    pause()

    # View hand
    clear_terminal()
    hand = deck.deal_hand(5)
    print("Hand dealt:")
    print(hand)
    hand.show()
    print()
    hand.show(use_glyph=True)
    print()
    hand.hidden = [2, 3, 4]
    print("With hidden cards:")
    print(hand)
    hand.show()
    print()
    hand.show(use_glyph=True)
    print()
    print(f"Game:  {hand.game.title()}\nValue: {hand.value}\n")

    # View hand as JSON
    # pause()
    # clear_terminal()
    # print(repr(hand))

if __name__ == "__main__":
    main()
