def print_board(board):
    """Print board with formatting."""
    print(' {0} | {1} | {2} '.format(*board))
    print('-----------')
    print(' {3} | {4} | {5} '.format(*board))
    print('-----------')
    print(' {6} | {7} | {8} '.format(*board))

def get_winner(board):
    """Return winning symbol ('X', 'O') or ' ' if none found."""
    # Check for rows
    for i in range(0, 9, 3):
        if board[i] == 'X' or board[i] == 'O':
            if board[i] == board[i + 1] == board[i + 2]:
                return board[i]
    # Check for columns
    for i in range(0, 3):
        if board[i] == 'X' or board[i] == 'O':
            if board[i] == board[i + 3] == board[i + 6]:
                return board[i]
    # Check for diagonals
    if board[4] == 'X' or board[4] == 'O':
        if (
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]
        ):
            return board[4]
    # No winning moves found
    return ' '

def game():
    # Create empty board with 9 spaces
    board = [' '] * 9
    user_continue = True
    current_player = 'X'
    # Start of new game
    while user_continue:
        winner = ' '
        unavailable_moves = set()
        print('Game Start')
        # Start of new turn
        while winner == ' ' and len(unavailable_moves) < 9:
            print("{}'s turn".format(current_player))
            print_board(board)
            player_pos = input('Select position: ')
            # Check input for numbers in range that haven't been taken
            while (
                not player_pos.isnumeric() or
                int(player_pos) < 1 or
                int(player_pos) > 9 or
                int(player_pos) in unavailable_moves
            ):
                player_pos = input('Invalid input. Enter a number 1-9 that corresponds to an empty space: ')
            # Accept player input and update accordingly
            unavailable_moves.add(int(player_pos))
            board[int(player_pos) - 1] = current_player
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
            # Check board for winner after new move has been added
            winner = get_winner(board)
        if winner != ' ':
            print('Game over. {} wins!'.format(winner))
        else:
            print("Game over. It's a draw!")
        print_board(board)
        continue_input = input('New game (Y/N)? ')
        if continue_input.upper() == 'Y':
            user_continue = True
            board = [' '] * 9
        else:
            user_continue = False

print('Tic Tac Toe')
print('===========')
game()