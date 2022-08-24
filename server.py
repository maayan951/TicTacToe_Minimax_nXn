from flask import Flask, request, jsonify
import pickle
from TicTacToe import TicTacToe

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    b = request.get_json()
    res = game(b)
    return jsonify(res)

def game(b):
    if 'n' in b:
        n = b['n']
        ttt = TicTacToe(n)
        # pickling the model to file
        with open("./game" + '.pkl', 'wb') as file:
            pickle.dump(ttt, file)
        d = dict()
        d["currentPlayer"] = ttt.currentPlayer
        d["board"] = ttt.board
        d["winner"] = ttt.winner
        d["draw"] = ttt.draw
        return d
    
    with open('./game' + '.pkl', 'rb') as file:
        g = pickle.load(file)
    
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
        
    g.currentPlayer = 1 - g.currentPlayer

    with open("./game" + '.pkl', 'wb') as file:
        pickle.dump(g, file)
    
    b = dict()
    b["currentPlayer"] = g.currentPlayer
    b["board"] = g.board
    b["winner"] = g.winner
    b["draw"] = g.draw
    
    return b

if __name__ == '__main__':
    app.run()
