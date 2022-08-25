
from random import randint
import math

class TicTacToe:
    def __init__(self,n:int=5):
        self.n = n
        self.board = [[' ' for j in range(n)] for i in range(n)]
        self.__randomizeStartingPlayer()
        self.winner = None
        self.draw = False
    
    
    def __randomizeStartingPlayer(self):
        '''
        Randomly chooses who starts the game.
        '''
        self.currentPlayer = randint(0,1)
        if self.currentPlayer == 1:
            # print('You are X, you go first.\n')
            self.player = 'X'
            self.computer = 'O'
        else:
            # print('You are O, you go second.\n')
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
    
    
    def checkDraw(self, board: list[list]):
        '''
        Checks if the game is a draw.
        '''
        for line in board:
            for tile in line:
                if tile == ' ':
                    return False
        return True
    
    
    def heuristic(self):
        '''
        Returns the heuristic value of the given board.
        '''
        
        # Possible winning moves
        possibilitiesList = []
        # Adding all rows
        for l in self.board:
            possibilitiesList.append(l)
        # Adding all columns
        for i in range(self.n):
            possibilitiesList.append([self.board[j][i] for j in range(self.n)])
        # Adding all diagonals 
        possibilitiesList.append([self.board[i][i] for i in range(self.n)])
        possibilitiesList.append([self.board[i][self.n-1-i] for i in range(self.n)])
        
        # Score table
        Heuristic_Array = [[0 for j in range(self.n+1)] for i in range(self.n+1)]
        for i in range(1, self.n+1):
            Heuristic_Array[0][i] = -10**i
            Heuristic_Array[i][0] = 10**i
        
        score = 0
        for i in range(2*self.n + 2):
            p = c = 0
            for j in range(self.n):
                piece = possibilitiesList[i][j]
                if (piece == self.player):
                    p += 1
                elif (piece == self.computer):
                    c += 1
            score += Heuristic_Array[p][c]
            
        return score


    def computerMove(self):
        '''
        Makes the computer's move.
        '''
        def minimax(board, depth, alpha, beta, maximizingPlayer):
            
            if self.checkForWin(self.computer):
                return 10**self.n
            elif self.checkForWin(self.player):
                return -10**self.n
            elif self.checkDraw(self.board):
                return 5**self.n
            elif depth == 0 :
                return self.heuristic()
            elif maximizingPlayer:
                maxScore = -math.inf
                for i in range(self.n):
                    for j in range(self.n):
                        if board[i][j] == ' ':
                            board[i][j] = self.computer
                            maxScore = max(maxScore, minimax(board, depth-1, alpha, beta, not maximizingPlayer))
                            board[i][j] = ' '
                            alpha = max(alpha, maxScore)
                            if beta <= alpha:
                                break
                return maxScore
            else:
                minScore = math.inf
                for i in range(self.n):
                    for j in range(self.n):
                        if board[i][j] == ' ':
                            board[i][j] = self.player
                            minScore = min(minScore, minimax(board, depth-1, alpha, beta, not maximizingPlayer))
                            board[i][j] = ' '
                            beta = min(beta, minScore)
                            if beta <= alpha:
                                break
                return minScore
        
          
        bestScore = -math.inf
        bestMove = 0
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == ' ':
                    self.board[r][c] = self.computer
                    score = minimax(self.board, 4, -math.inf, math.inf, False)
                    self.board[r][c] = ' '
                    if score > bestScore:
                        bestScore = score
                        bestMove = (r, c)
                        
        self.board[bestMove[0]][bestMove[1]] = self.computer

