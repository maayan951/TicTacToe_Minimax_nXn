

### Q10 - using minimax algorithm

'''
Minimax learning resources used:
Wikipedia: https://en.wikipedia.org/wiki/Minimax
Geeksforgeeks: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/?ref=lbp
               https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/?ref=lbp
Youtube: https://www.youtube.com/watch?v=l-hh51ncgDI
'''

from random import randint

#region Functions

def printBoard(board):
    '''
    Prints the board in a 3x3 grid.
    '''
    for i in range(3):
        print(' ' + board[i * 3] + ' | ' + board[i * 3 + 1] + ' | ' + board[i * 3 + 2])
        if (i != 2):
            print('-----------')


def checkForWin(mark):
    '''
    Checks if the given mark has won the game.
    '''
    for i in range(3):
        # Check rows
        if (board[i * 3] == board[i * 3 + 1] and board[i * 3] == board[i * 3 + 2] and board[i * 3] == mark):
            return True
        # Check columns
        if (board[i] == board[i + 3] and board[i] == board[i + 6] and board[i] == mark):
            return True

    # Check diagonals
    if (board[0] == board[4] and board[0] == board[8] and board[0] == mark):
        return True
    if (board[2] == board[4] and board[2] == board[6] and board[2] == mark):
        return True
    
    return False


def checkDraw(board):
    '''
    Checks if the game is a draw.
    '''
    for tile in board:
        if (tile == ' '):
            return False
    return True


def minimax(board, depth, isMaximizing):
    '''
    Minimax algorithm.
    '''
    if (checkForWin(computer)):
        return 1
    if (checkForWin(player)):
        return -1
    if (checkDraw(board)):
        return 0
    if depth == 0:
        return 0

    if (isMaximizing):
        bestScore = -1000    # -INFINITY
        for key in range(len(board)):
            if (board[key] == ' '):
                board[key] = computer
                score = minimax(board, depth - 1, not isMaximizing)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000   # INFINITY
        for key in range(len(board)):
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth - 1, not isMaximizing)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def getBestMove(board):
    bestScore = -1000 #INFINITY
    bestMove = 0
    for tile in range(len(board)):
        if (board[tile] == ' '):
            board[tile] = computer
            score = minimax(board, 10, False)
            board[tile] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = tile
    return bestMove

#endregion


#region Main
    
currentPlayer = randint(0,1)
if currentPlayer == 1:
    print('You are X, you go first.\n')
    player = 'X'
    computer = 'O'
else:
    print('You are O, you go second.\n')
    player = 'O'
    computer = 'X'
    
board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

winner = False
draw = False

printBoard(board)

while winner == False and draw == False:
    if currentPlayer == 1:
        print('\nIt is your turn.\n')
        while True:
            move = input('Enter your move (number from 1 to 9): ')
            if move.isdigit():
                move = int(move) - 1
                if move >= 0 and move <= 8 and board[move] == ' ':
                    board[move] = player
                    break
                else:
                    print('That place is already taken or invalid. try again.')
            else:
                print('That is not a number. Try again.')
    else:
        print('\nIt is the computer\'s turn.')
        board[getBestMove(board)] = computer            
        
    printBoard(board)    
    
    if checkForWin(player) or checkForWin(computer):
        winner = True
        continue
    
    draw = checkDraw(board)
    
    currentPlayer = 1 - currentPlayer
    

if winner == True:
    if currentPlayer == 1:
        print(f'\nYou won!, Let\'s Go {player}')
    else:
        print('\nThe computer won! Better luck next time!')
else:
    print('\nIt\'s a draw!')

#endregion
