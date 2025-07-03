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
            hand_str = [str(card) for card in self.hand]
            print('{} shows '.format(self.name) + ' and '.join(hand_str))
    
    def hit(self, card):
        self.hand.append(card)

    def bet(self, amt=None):
        if amt is None:
            amt = self.bet_amt
        if amt > self.money:
            print('{} cannot bet more money than they have'.format(self.name))
            return 0
        elif amt == 0:
            print('{} must bet more than 0'.format(self.name))
            return 0
        else:
            self.money -= amt
            print('{} bets {}'.format(self.name, amt))
            return amt
        
class Dealer(Player):
    def __init__(self, deck):
        super().__init__('Dealer', -1)
        self.deck = deck
    
    def initial_deal(self, players):
        """Perform the initial deal--two cards to every player."""
        for _ in range(2):
            for player in players:
                player.hand.append(self.deck.deal_card())
    
    def deal(self, player):
        """Add card to player's hand."""
        card = self.deck.deal_card()
        player.hit(card)
        return card
    
    def print_dealer_hand(self):
        """Print dealer's hand before all players have gone.
        print_hand() should be used after all players moves are final.
        """
        if len(self.hand) == 0:
            print('{} holds no cards'.format(self.name))
        else:
            print('{} shows '.format(self.name) + str(self.hand[0]))
    
    def collect_cards(self, players):
        """Collect all cards from all players and discard."""
        for player in players:
            player.deck = []