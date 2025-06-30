class Player:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.hand = []
        self.bet_amt = 0
    
    def __str__(self):
        return '{} has ${}'.format(self.name, self.money)
    
    def print_hand(self):
        if len(self.hand) == 0:
            print('{} holds no cards'.format(self.name))
        else:
            print('{} shows '.format(self.name) + ' and '.join(self.hand))
    
    def hit(self, card):
        self.hand.append(card)

    def bet(self, amt=None):
        if amt is None:
            amt = self.bet_amt
        if amt > self.money:
            print('{} cannot bet more money than they have'.format(self.name))
            return 0
        else:
            self.money -= amt
            print('{} bets {}'.format(self.name, amt))
            return amt
    
    def prepare_deal(self):
        self.hand = []
        
class Dealer(Player):
    def __init__(self, deck):
        super().__init__('Dealer', -1)
        self.deck = deck
    
    def initial_deal(self, players):
        for _ in range(2):
            for player in players:
                player.hand.append(self.deck.deal_card())
    
    def deal(self, player):
        player.hit(self.deck.deal_card())
    
    def print_hand(self):
        if len(self.hand) == 0:
            print('{} holds no cards'.format(self.name))
        else:
            print('{} shows '.format(self.name) + self.hand[0])