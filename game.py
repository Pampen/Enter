from flask import Flask, request, Response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def getRequest():
    getUserInput = request.get_json()
    userInput = getUserInput.get('message')
    response = getResponse(userInput)
    print(userInput)
    return jsonify(response) #Return value of variable 'response' to JavaScript

def getResponse(userInput):
    #TODO Change dict. entries to corresponding functions, modules.
    # userInput contains string that corresponds with what the player did
    return {
        "newGameState": {
            "levelTitle": None,
            "levelDescription": 'This is a very so much like a description.',
            "levelChatboxText": 'This appears in the chatbox.'
        },
        "inventory": {
            "firstObject": True,
            "secondObject": False
        }
    }