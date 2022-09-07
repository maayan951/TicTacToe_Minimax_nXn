from client_funcs import *

# address = "http://127.0.0.1:5000/"
address = "http://10.0.1.97:5000/"  # This is the address of the local server(IPv4 Address)

# To find the IPv4 address of the local server, run the following command in the terminal:
## Windows powershell/command prompt: ipconfig
## Linux terminal: ifconfig

clearConsole()
# Get name
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


# Mini menu
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

