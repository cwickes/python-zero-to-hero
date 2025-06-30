import random

from card import Card

ranks = [
    'Ace',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
]
suits = [
    'Spades',
    'Hearts',
    'Diamonds',
    'Clubs',
]

class Deck:
    def __init__(self, count=1):
        """Initialize a new deck containing {count} standard decks."""
        self.cards = []
        for _ in range(count):
            for rank in ranks:
                for suit in suits:
                    card = Card(suit, rank)
                    self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()