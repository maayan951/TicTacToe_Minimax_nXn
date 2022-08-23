from flask import Flask
from TicTacToe import TicTacToe

app = Flask(__name__)

@app.route('/')
def mainMenu():
    return 'start game'

if __name__ == '__main__':
    app.run()
