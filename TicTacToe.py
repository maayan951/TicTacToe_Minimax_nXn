
from random import randint
import math
import threading

class TicTacToe:
    def __init__(self,n:int=5):
        self.n = n
        self.board = [[' ' for j in range(n)] for i in range(n)]
        self.__randomizeStartingPlayer()
        # self.printBoard()
        self.winner = None
        self.draw = False
    
    def __randomizeStartingPlayer(self):
        '''
        Randomly chooses who starts the game.
        '''
        self.currentPlayer = randint(0,1)
        if self.currentPlayer == 1:
            print('You are X, you go first.\n')
            self.player = 'X'
            self.computer = 'O'
        else:
            print('You are O, you go second.\n')
            self.player = 'O'
            self.computer = 'X'
    
    def __checkRange(self, lst: list, mark: str):
        '''
        Checks if the given list contains only the same element.
        '''
        for m in lst:
            if m != mark:
                return False
        return True
    
    def checkForWin(self, mark: str):
        '''
        Checks if the given mark has won the game.
        '''
        for i in range(self.n):
            # Check rows
            if self.__checkRange(self.board[i], mark):
                return True
            # Check columns
            if self.__checkRange([self.board[j][i] for j in range(self.n)], mark):
                return True
            
        # Check diagonals
        if self.__checkRange([self.board[i][i] for i in range(self.n)], mark):
            return True
        if self.__checkRange([self.board[i][self.n-1-i] for i in range(self.n)], mark):
            return True
        
        return False
    
    def checkDraw(self, board):
        '''
        Checks if the game is a draw.
        '''
        for line in board:
            for tile in line:
                if tile == ' ':
                    return False
        return True
    
    def computerMove(self):
        '''
        Makes the computer's move.
        '''
        def minimax(board, depth, alpha, beta, maximizingPlayer):
            if self.checkForWin(self.computer):
                return 1
            elif self.checkForWin(self.player):
                return -1
            elif self.checkDraw(board):
                return 0.5
            elif depth == 5:
                return 0
            elif maximizingPlayer:
                value = -math.inf
                for i in range(self.n):
                    for j in range(self.n):
                        if board[i][j] == ' ':
                            board[i][j] = self.computer
                            value = max(value, minimax(board, depth+1, alpha, beta, False))
                            board[i][j] = ' '
                            alpha = max(alpha, value)
                            if beta <= alpha:
                                return value
            else:
                value = math.inf
                for i in range(self.n):
                    for j in range(self.n):
                        if board[i][j] == ' ':
                            board[i][j] = self.player
                            value = min(value, minimax(board, depth+1, alpha, beta, True))
                            board[i][j] = ' '
                            beta = min(beta, value)
                            if beta <= alpha:
                                return value
            return value
        
          
        bestScore = -1000
        bestMove = 0
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == ' ':
                    self.board[r][c] = self.computer
                    score = minimax(self.board, 0, -1000, 1000, False)
                    self.board[r][c] = ' '
                    if score > bestScore:
                        bestScore = score
                        bestMove = (r, c)
                        
        self.board[bestMove[0]][bestMove[1]] = self.computer

    def play(self):
        '''
        Plays the game.
        '''
        while self.winner is None and self.draw is False:
            if self.currentPlayer == 1:
                self.playerMove()
            else:
                self.computerMove()
            
            self.printBoard()
                
            if self.checkForWin(self.player):
                self.winner = self.player
                continue
            elif self.checkForWin(self.computer):
                self.winner = self.computer
                continue
            elif self.checkDraw(self.board):
                self.draw = True
                break
            
            self.currentPlayer = 1 - self.currentPlayer
        
        if self.winner != None:
            print(f'{self.winner} wins!')
        elif self.draw:
            print('\nIt\'s a Draw!')





# # testing
        
# b = TicTacToe(3)

# b.play()