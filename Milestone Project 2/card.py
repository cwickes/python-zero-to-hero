class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
    def __int__(self):
        if self.rank == 'Ace':
            return 1
        elif self.rank == 'Two':
            return 2
        elif self.rank == 'Three':
            return 3
        elif self.rank == 'Four':
            return 4
        elif self.rank == 'Five':
            return 5
        elif self.rank == 'Six':
            return 6
        elif self.rank == 'Seven':
            return 7
        elif self.rank == 'Eight':
            return 8
        elif self.rank == 'Nine':
            return 9
        elif self.rank in {'Ten', 'Jack', 'Queen', 'King'}:
            return 10