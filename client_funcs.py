import requests
import json
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def printBoard(board, n):
    '''
    Prints the board in a nXn grid.
    '''
    st = '   '
    for i in range(n):
        st += ' ' + str(i+1) + '  '
    st += '\n'
    print(st)
    for i in range(n):
        st = f'{str(i+1)}   '
        for j in range(n):
            st += board[i][j]
            if j != n-1:
                st += ' | '
        if (i < n - 1):
            st += '\n   ' + '-'*(n*3 + n - 1)
        
        print(st)
    print('\n')



def playerMove(board, n, player):
    '''
    Gets the input from the user.
    '''
    while True:
        try:
            inp = input(f'Enter your move (2 number from 1 to {n}): ')
            r, c = map(int, inp.split())
            if r < 1 or r > n or c < 1 or c > n:
                print(f'Invalid input. Number out of range (1-{n})\n')
                continue
            if board[r-1][c-1] != ' ':
                print('Invalid input. Tile already taken\n')
                continue
            board[r-1][c-1] = player
            break
        except ValueError:
            print('Invalid input, Please enter 2 numbers.\n')
            continue
    return board






def startGame(address, name):
    n=None
    while True:
        try:
            n = int(input("Enter the size of the board(2<n<7): "))
            if n < 3 or n > 6:
                print("Invalid input. Number out of range (3-6)")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

    d = {'n': n, 'name': name}
    response = requests.post(address, json=d)
    g=json.loads(response.text)

    player = None
    if g["currentPlayer"] == 1:
        print("You are X, you go first")
        player = "X"
    else:
        print("You are O, you go second.")
        player = "O"

    print("\n")
    printBoard(g["board"], n)
    while g["winner"] == None and g["draw"] == False:
        
        if g["currentPlayer"] == 1:
            print("Your turn:")
            g["board"] = playerMove(g["board"], n, player)
            g["currentPlayer"] = 0
            printBoard(g["board"], n)
        
        print("Computer's turn:")
        response = requests.post(address, json=g)
        g = json.loads(response.text)
        printBoard(g["board"], n)
        
            
    if g["winner"] == None:
        print("Draw!")
    else:
        print(f"{g['winner']} wins!")
            
