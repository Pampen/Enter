from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getRequest():
    getUserInput = request.get_json()
    userInput = getUserInput.get('message')
    print(userInput)
    response = getResponse(userInput)
    return jsonify(response) #Return value of variable 'response' to JavaScript

def getResponse(userInput):
    #TODO Change dict. entries to corresponding functions, modules.
    # userInput contains string that corresponds with what the player did
    return {
        "newGameState": handleResponse(userInput),
        "inventory": {
            "firstObject": True,
            "secondObject": False
        }
    }

def handleResponse(userInput):
    if userInput == '1':
        return {
            "levelTitle": "Test1 ",
            "levelDescription": "Test 1",
            "levelChatboxText": 'Test 1'
        }
    elif userInput == '2':
        return {
            "levelTitle": 'Test 2',
            "levelDescription": 'Test 2',
            "levelChatboxText": 'Test 2!!'
        }
    else:
        return {
            "levelTitle": None,
            "levelDescription": None,
            "levelChatboxText": "Du vad gör du"
        }
'''
def outsideRoom(userInput):
    if UserInput == "go forward":
        return{
            "newGameState": {
                "LevelTitle": 'Main porch',
                "LevelDescription": 'Du försöka öppna dörren men den är låst, du ser ett nyckelhål',
                "LevelChatboxText": 'Ta dig tillbaka'
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }:
    if UserInput.lower() == "go left":
        return {
            "newGameState": {
                "LevelTitle": 'Shed',
                "LevelDescription": 'Du ser ett nerkört skjul och går in i den'
                "LevelChatboxText": 'Rör dig med text-kommandon'
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }:
    if UserInput.lower() == "go back":
        return {
            "newGameState": {
                "LevelTitle": 'Outside',
                "LevelDescription": 'Du kan inte gå dit'
                "LevelChatboxText": 'Rör dig med text-kommandon'
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
        }
'''