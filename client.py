import requests
import json


address = "http://127.0.0.1:5000/"

n=None
while True:
    try:
        n = int(input("Enter the size of the board(2<n<7): "))
        if n < 2 or n > 6:
            print("Invalid input. Number out of range (2-6)")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

d = {'n': n}

response = requests.post(address, json=d)
returned_object=json.loads(response.text)
print(returned_object)


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





def playerMove(self):
    '''
    Gets the input from the user.
    '''
    while True:
        try:
            inp = input(f'Enter your move (2 number from 1 to {self.n}): ')
            r, c = map(int, inp.split())
            if r < 1 or r > self.n or c < 1 or c > self.n:
                print(f'Invalid input. Number out of range (1-{self.n})\n')
                continue
            if self.board[r-1][c-1] != ' ':
                print('Invalid input. Tile already taken\n')
                continue
            self.board[r-1][c-1] = self.player
            break
        except ValueError:
            print('Invalid input, Please enter 2 numbers.\n')
            continue