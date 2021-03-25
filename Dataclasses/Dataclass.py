from dataclasses import dataclass
from typing import List


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (
            f"{self.__class__.__name__}" f"(rank={self.rank!r}, suit={self.suit!r})"
        )  # !r ask for the __repr__ representation

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


@dataclass
class DataClassCard:
    rank: str
    suit: str


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = DataClassCard(rank="Q", suit="Hearts")
# print(queen_of_hearts)
qoh = RegularCard(rank="Q", suit="Hearts")
# print(qoh)

queen_of_hearts = PlayingCard("Q", "Hearts")
ace_of_spades = PlayingCard("A", "Spades")
two_cards = Deck([queen_of_hearts, ace_of_spades])
# print(two_cards)


RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "Spades Diamonds Hearts Clubs".split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


df = make_french_deck()
print(df)
