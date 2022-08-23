
from math import sqrt
from random import randint
# from beautifultable import BeautifulTable

class TicTacToe:
    def __init__(self,n):
        self.n = n
        self.board = [[' ' for j in range(n)] for i in range(n)]
        self.__randomizeStartingPlayer()
        self.printBoard()
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
    
    def checkDraw(board):
        '''
        Checks if the game is a draw.
        '''
        for line in board:
            for tile in line:
                if tile == ' ':
                    return False
        return True
    
    
    def printBoard(self):
        '''
        Prints the board in a nXn grid.
        '''
        st = '   '
        for i in range(self.n):
            st += ' ' + str(i+1) + '  '
        st += '\n'
        print(st)
        for i in range(self.n):
            st = f'{str(i+1)}   '
            for j in range(self.n):
                st += self.board[i][j]
                if j != self.n-1:
                    st += ' | '
            if (i < self.n - 1):
                st += '\n   ' + '-'*(self.n*3 + self.n - 1)
            
            print(st)
        print('\n')
        
        
b = TicTacToe(3)
b.board[0][0] = 'X'
b.board[1][1] = 'X'
b.board[1][2] = 'X'
b.board[2][0] = 'O'
b.board[2][1] = 'O'
b.board[2][2] = 'O'
b.printBoard()
print(b.checkForWin('X'))
print(b.checkForWin('O'))