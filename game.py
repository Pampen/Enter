from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getRequest():
    file_name = "result.json"
    gameState = get_result_from_file(file_name)
    currentLevel = saveCurrentLevel(gameState)

    getUserInput = request.get_json()
    userInput = getUserInput.get('message')

    response = getResponse(userInput, currentLevel)
    save_results_to_file(file_name, response)
    return jsonify(response) #Return value of variable 'response' to JavaScript

def getResponse(userInput, currentLevel):
    #TODO Change dict. entries to corresponding functions, modules.
    # userInput contains string that corresponds with what the player did
    return {
        "newGameState": allLevelsControl(userInput, currentLevel),
        "inventory": {
            "firstObject": True,
            "secondObject": False
        }
    }

def allLevelsControl(userInput, currentLevel):
    print(currentLevel)
    if currentLevel == "Main porch":
        return porch(userInput, currentLevel)
    elif currentLevel == "Outside":
        return outside(userInput, currentLevel)
    elif currentLevel == "Shed":
        return shed(userInput, currentLevel)
    else:
        return None

def porch(userInput, currentLevel):
    levelPorch = currentLevel
    if userInput == "go forward" and levelPorch:
        return wrongPorchDirection()
    elif userInput == "go back" and levelPorch:
        return {
            "levelTitle": "Outside",
            "levelDescription": "Youre outside",
            "levelChatboxText": "YAY"
        }
    elif userInput == "go left" and levelPorch:
        return wrongPorchDirection()
    elif userInput == "go right" and levelPorch:
        return wrongPorchDirection()

def wrongPorchDirection():
    return {
            "levelTitle": "Main porch",
            "levelDescription": "Youre on the main porch",
            "levelChatboxText": "You cant do that"
        }

def outside(userInput, currentLevel):
    levelOutside = currentLevel
    if userInput == "go forward" and levelOutside:
        return {
            "levelTitle": "Main porch",
            "levelDescription": "Youre on the main porch",
            "levelChatboxText": "YAY"
        }
    elif userInput == "go back" and levelOutside:
        return wrongOutsideDirection()
    elif userInput == "go left" and levelOutside:
        return {
            "levelTitle": "Shed",
            "levelDescription": "Youre in the shed",
            "levelChatboxText": "YAY"
        }
    elif userInput == "go right" and levelOutside:
        return wrongOutsideDirection()
    
def wrongOutsideDirection():
    return {
            "levelTitle": "Outside",
            "levelDescription": "Youre outside",
            "levelChatboxText": "You cant do that"
        }

def shed(userInput, currentLevel):
    levelShed = currentLevel
    print(levelShed)
    if userInput == "go forward" and levelShed:
        return wrongShedDirection()
    elif userInput == "go back" and levelShed:
        return wrongShedDirection()
    elif userInput == "go left" and levelShed:
        return wrongShedDirection()
    elif userInput == "go right" and levelShed:
       return {
            "levelTitle": "Outside",
            "levelDescription": "The outside",
            "levelChatboxText": "YAY"
        }

def wrongShedDirection():
    return {
            "levelTitle": "Shed",
            "levelDescription": "The Shed",
            "levelChatboxText": "You cant do that"
        }

def saveCurrentLevel(gameState):
    currentLevel = gameState["newGameState"]["levelTitle"]
    return currentLevel

def get_result_from_file(file_name):
    try:
        my_file = open(file_name, "r")
        result_from_file = my_file.read()
        result = json.loads(result_from_file)

        return result
    
    except FileNotFoundError:
        my_file = open(file_name, "w")
        my_file.write(json.dumps({ 
        "newGameState": {
            "levelTitle": "Outside",
            "levelDescription": "You wake up outside",
            "levelChatboxText": "What do you want to do?"
            }
        }))
        my_file.close()
        my_file = open(file_name, "r")
        result_from_file = my_file.read()
        result = json.loads(result_from_file)

        return result

def save_results_to_file(file_name, response):
    jsonResponse = json.dumps(response)
    my_file = open(file_name, "w")
    my_file.write(jsonResponse)
    my_file.close()