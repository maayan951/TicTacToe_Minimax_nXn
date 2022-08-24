from client_funcs import *

address = "http://127.0.0.1:5000/"


while True:
    try:
        name = input("Enter your name: ")
        if name.isalnum():
            break
        else:
            print("Invalid input. Please enter alphanumeric characters.")
    except ValueError:
        print("Invalid input. Please enter a string.")
        continue

while True:
    try:
        ans = input("Enter 'n' for new game, 'q' to quit: ")
        if len(ans) != 1:
            print("Invalid input. Please enter a single character.")
            continue
        elif ans == 'n' or ans == 'N':
            clearConsole()
            startGame(address, name)
        elif ans == 'q' or ans == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'n' or 'q'.")
        continue        
    except KeyboardInterrupt:
        print("\nQuitting...")
        break

