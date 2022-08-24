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
        
    
        
    pass

if __name__ == '__main__':
    app.run()
