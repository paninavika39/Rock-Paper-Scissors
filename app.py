import random
from flask import Flask, request, jsonify
from flask_cors import CORS  # Импортируйте модуль для обработки CORS

app = Flask(__name__)
CORS(app)

@app.route('/play', methods=['POST'])
def play():
    choices = ['rock', 'paper', 'scissors']
    client_choice = request.json['choice']
    server_choice = random.choice(choices)
    result = get_result(client_choice, server_choice)
    response = jsonify({'server_choice': server_choice, 'result': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_result(client_choice, server_choice):
    if client_choice == server_choice:
        return 'tie'
    elif (client_choice == 'rock' and server_choice == 'scissors') or \
         (client_choice == 'paper' and server_choice == 'rock') or \
         (client_choice == 'scissors' and server_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

app.run(debug=True, port=5500)
