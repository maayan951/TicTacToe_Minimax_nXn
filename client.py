from client_funcs import *

address = "http://127.0.0.1:5000/"

while True:
    try:
        ans = input("Enter 'n' for new game, 'q' to quit: ")
        if len(ans) != 1:
            print("Invalid input. Please enter a single character.")
            continue
        elif ans == 'n' or ans == 'N':
            clearConsole()
            startGame(address)
        elif ans == 'q' or ans == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'n' or 'q'.")
        continue        
    except KeyboardInterrupt:
        print("\nQuitting...")
        break

