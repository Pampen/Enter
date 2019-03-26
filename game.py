from flask import Flask, request, Response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
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
        "newGameState": {handleResponse(userInput)}
    }

def handleResponse(userInput):
    response = None
    if userInput == 'goforward':
        response = {
            "LevelTitle": "Test 2",
            "LevelDescription": "Test 2",
            "LevelChatboxText": "Test 2"
        }
    elif userInput == 'inget':
        response = { 
            "levelTitle": "Test1",
            "levelDescription": "Test 1",
            "levelChatboxText": "Test 1."
            }
    
    return response
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