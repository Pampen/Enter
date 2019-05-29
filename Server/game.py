from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from levelChecker import levelChecker
from utilities import inspectItem
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getRequest():
    getState = request.get_json()
    userInput = getState.get('message')
    state = getState.get('state')
    
    userInput = userInput.upper()

    response = getResponse(userInput, state)

    return jsonify(response)

def getResponse(userInput, state):
    if 'INSPECT' in userInput:
        print("sdasdsa")
        return inspectItem(state, userInput)
    else: 
        return levelChecker(userInput, state)
