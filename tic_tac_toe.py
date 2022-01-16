''' Introduction: Ponder and Prove - Tic-Tac-Toe
    Adam Denning
'''

#space possibilities (constants)
X = 'X'
O = 'O'
BLANK = ' '

def display_board(board):
    '''Display's board in user friendly way.'''

    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def is_x_turn(board):
    '''Determine whose turn it is.
    True = x's turn, False = o's turn.'''

    x_count = 0
    o_count = 0
    i = 0

    #loops through board
    while i < 9:
        if board[i] == X:
            x_count += 1
        elif board[i] == O:
            o_count += 1
        i += 1

    #determines turn
    if x_count == o_count:
        return True
    else:
        return False

def game_done(board):
    '''Determines if game is finished, prints user friendly message if it is.'''

    #row case
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            print(f"The game was won by {board[row * 3]}")
            return True

    #column case
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            print(f"The game was won by {board[col]}")
            return True

    #diagonal case
    if board[4] != BLANK and (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
        print(f"The game was won by {board[4]}")
        return True

    #full board
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        print("The game is a tie!")
        return True

    return False

def main():

    #welcome and directions
    print("Welcome to tic-tac-toe.\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("To play, take turns entering a number (1-9) corresponding to an empty space on the board. Get 3 in a row in any direction to win.")
    
    #initialize board
    board = [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK]

    #plays game until finished
    while not game_done(board):

        #display current board
        display_board(board)

        #determine whose turn it is
        x_determ = is_x_turn(board)

        if x_determ:
            entry = input("Choose an empty space (1-9) X> ")
            entry = int(entry)
        else:
            entry = input("Choose an empty space (1-9) O> ")
            entry = int(entry)
        
        #updates board with entry
        if x_determ:
            board[entry-1] = 'X'
        else:
            board[entry-1] = 'O'

main()