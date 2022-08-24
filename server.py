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
    
    if 'name' in b and 'n' in b:
        try:
            d = None
            with open("./client games/" + b['name'] + '.pkl', 'rb') as file:
                g = pickle.load(file)
                d = pickle.load(file)
            if len(d['board']) == b['n']:
                return d
        except FileNotFoundError:
            pass
    
    if 'n' in b:
        n = b['n']
        name = b['name']
        ttt = TicTacToe(n)

        d = dict()
        d["currentPlayer"] = ttt.currentPlayer
        d["board"] = ttt.board
        d["winner"] = ttt.winner
        d["draw"] = ttt.draw
        d["name"] = name
        
        with open("./client games/" + name + '.pkl', 'wb') as file:
            pickle.dump(ttt, file)
            pickle.dump(d, file)
        return d
    
    with open("./client games/" + b['name'] + '.pkl', 'rb') as file:
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
    

    # b = dict()
    b["currentPlayer"] = g.currentPlayer
    b["board"] = g.board
    b["winner"] = g.winner
    b["draw"] = g.draw

    with open("./client games/" + b['name'] + '.pkl', 'wb') as file:
        pickle.dump(g, file)
        pickle.dump(b, file)
    
    return b

if __name__ == '__main__':
    app.run()
