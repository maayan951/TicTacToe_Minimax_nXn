
from math import sqrt
from random import randint
from beautifultable import BeautifulTable

class TicTacToe:
    def __init__(self,n):
        self.n = n
        self.board = [f' {i+1} ' for i in range(n**2)]

        self.currentPlayer = randint(0,1)
        if self.currentPlayer == 1:
            print('You are X, you go first.\n')
            self.player = 'X'
            self.computer = 'O'
        else:
            print('You are O, you go second.\n')
            self.player = 'O'
            self.computer = 'X'
            
        self.printBoard()
        self.gameOver = False
        self.winner = None
        self.draw = False
        self.turn = 0
        self.move = 0
        self.bestMove = 0
        self.bestScore = -1000
    
    def printBoard(self):
        '''
    Prints the board in a nXn grid.
    '''
        table = BeautifulTable()
        for i in range(self.n):
            table.append_row(self.board[i*self.n:(i+1)*self.n])
        print(table)
    
    def printBoard1(self):
        '''
    Prints the board in a nXn grid.
    '''
        for i in range(self.n):
            print('\t |\t'.join(self.board[i*self.n:(i+1)*self.n]))
            if (i != self.n - 1):
                print('-'*(self.n*(self.n)*2))

        
        
b = TicTacToe(3)
