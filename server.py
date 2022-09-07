from flask import Flask, request, jsonify
from TicTacToe import TicTacToe
import pickle

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    b = request.get_json()
    res = game(b)
    return jsonify(res)


def game(b):
    
    # Load the previously saved game if exists
    if 'name' in b and 'n' in b:
        try:
            d = None
            with open("./client games/" + b['name'] + '.pkl', 'rb') as file:
                g = pickle.load(file)
                d = pickle.load(file)
            # if the game is over skip to create a new game
            if len(d['board']) == b['n'] and d["winner"] == None and d["draw"] == False:
                return d
        except FileNotFoundError:
            pass
    
    # Create a new game if no previous game exists
    if 'n' in b:
        n = b['n']
        name = b['name']
        ttt = TicTacToe(n)

        d = dict()
        d["currentPlayer"] = ttt.currentPlayer
        d["player"] = ttt.player
        d["board"] = ttt.board
        d["winner"] = ttt.winner
        d["draw"] = ttt.draw
        d["name"] = name
        
        with open("./client games/" + name + '.pkl', 'wb') as file:
            pickle.dump(ttt, file)
            pickle.dump(d, file)
        return d
    
    
    # Load the previously saved game
    with open("./client games/" + b['name'] + '.pkl', 'rb') as file:
        g = pickle.load(file)
    
    
    # Make the computer's move and check if the game is over
    g.board = b['board']
    g.currentPlayer = b['currentPlayer']
    
    if g.checkForWin(g.player):
        g.winner = g.player
    elif g.checkDraw(g.board):
        g.draw = True
    else:   
        g.computerMove()
    
    if g.checkForWin(g.computer):
        g.winner = g.computer
    elif g.checkDraw(g.board):
        g.draw = True
    
    
    # Swap the current player
    g.currentPlayer = 1 - g.currentPlayer
    
    # Save the current state of the game
    b["currentPlayer"] = g.currentPlayer
    b["board"] = g.board
    b["winner"] = g.winner
    b["draw"] = g.draw

    with open("./client games/" + b['name'] + '.pkl', 'wb') as file:
        pickle.dump(g, file)
        pickle.dump(b, file)
    
    
    return b


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
