from deck import Deck
from player import Player, Dealer

def is_natural(hand):
    """Check if hand is a natural blackjack."""
    # Ace and (Ten, Jack, Queen, King)
    if hand[0] == 1 and hand[1] == 10:
        return True
    # (Ten, Jack, Queen, King) and Ace
    if hand[0] == 10 and hand[1] == 1:
        return True
    return False

def get_move():
    while True:
        move = input('Hit (H) or Stand (S)? ').upper()
        if move == 'H' or move == 'S':
            return move

# Create and prepare deck for six-deck game
deck = Deck(6)
deck.shuffle()

# Create players and populate lists
dealer = Dealer(deck)
player = Player('Julian Braun', 1000)
player.bet_amt = 25
players = [player]

while any(player.money > 0 for player in players):
    active_players = []

    # Betting
    bets = {}
    for player in players:
        bet = player.bet()
        if bet > 0:
            bets[player] = bet
            active_players.append(player)

    # active_players needs players for game to continue
    if len(active_players) > 0:
        # The Deal
        dealer.initial_deal(active_players + [dealer])

        for player in active_players:
            player.print_hand()

        # Naturals
        if is_natural(dealer.hand):
            print('Dealer has a blackjack.')
            dealer.print_hand()
            for player in active_players:
                if is_natural(player.hand):
                    # Stand-off--player gets their bet back
                    player.amount += bets[player]
                    print('{} pushes with a blackjack.'.format(player.name))
        # Dealer does not have a blackjack, proceed with game
        else:
            # The Play
            players_to_remove = []
            for player in active_players:
                if is_natural(player.hand):
                    win_amt = bets[player] * 1.5
                    player.money += bets[player] + win_amt
                    player.print_hand()
                    print('{} wins {} with a blackjack!'.format(player.name, win_amt))
                    players_to_remove.append(player)
                else:
                    dealer.print_dealer_hand()
                    player.print_hand()
                    while sum(int(card) for card in player.hand) < 21:
                        move = get_move()
                        if move == 'H':
                            dealer.deal(player)
                            player.print_hand()
                        else:
                            break
                    if sum(int(card) for card in player.hand) > 21:
                        print('{} busts!'.format(player.name))
                        players_to_remove.append(player)
            
            # Update active_players to those that haven't already won/lost
            for player in players_to_remove:
                active_players.remove(player)

            # Check if there are players that haven't already won/lost
            if len(active_players) > 0:
                # The Dealer's Play
                print("It is now the dealer's turn.")
                dealer.print_hand()
                dealer_total = 0
                ace_in_hand = False
                for card in dealer.hand:
                    if card == 1:
                        ace_in_hand = True
                    dealer_total += int(card)
                while True:
                    # No ace
                    if not ace_in_hand:
                        # No ace < 17, hit and check for ace
                        if dealer_total < 17:
                            card = dealer.deal(dealer)
                            dealer.print_hand()
                            if card == 1:
                                ace_in_hand = True
                            dealer_total += int(card)
                        # No ace >= 17, stand
                        else:
                            break
                    # Ace
                    else:
                        # Soft ace <= 17, hit
                        if dealer_total + 10 <= 17:
                            card = dealer.deal(dealer)
                            dealer.print_hand()
                            dealer_total += int(card)
                        # 17 < soft ace <= 21, stand
                        elif 17 < dealer_total + 10 <= 21:
                            dealer_total += 10
                            break
                        # Soft ace > 21
                        elif dealer_total + 10 > 21:
                            # Hard ace < 17, hit
                            if dealer_total < 17:
                                card = dealer.deal(dealer)
                                dealer.print_hand()
                                dealer_total += int(card)
                            # Hard ace >= 17, stand
                            else:
                                break
                
                # Determine winners, if any
                if dealer_total > 21:
                    print('Dealer busts!')
                    for player in active_players:
                        win_amt = bets[player]
                        player.money += bets[player] + win_amt
                        print('{} wins {}!'.format(player.name, win_amt))
                else:
                    for player in active_players:
                        player.print_hand()
                        player_total = 0
                        ace_in_hand = False
                        for card in player.hand:
                            if card == 1:
                                ace_in_hand = True
                            player_total += int(card)
                        if ace_in_hand and player_total + 10 <= 21:
                            player_total += 10
                        if player_total == dealer_total:
                            player.money += bets[player]
                            print("For {}, it's a push.".format(player.name))
                        elif player_total > dealer_total:
                            win_amt = bets[player]
                            player.money += bets[player] + win_amt
                            print('{} wins {}!'.format(player.name, win_amt))
                        else:
                            print('{} loses.'.format(player.name))

            print('This round has ended.')
            dealer.collect_cards(players + players_to_remove)