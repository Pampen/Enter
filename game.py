from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getRequest():
    file_name = "result.json"

    getUserInput = request.get_json()
    userInput = getUserInput.get('message')
    userInput = userInput.lower()

    response = getResponse(userInput)
    return jsonify(response) #Return value of variable 'response' to JavaScript

def getResponse(userInput):
    #TODO Change dict. entries to corresponding functions, modules.
    # userInput contains string that corresponds with what the player did
    gameState = getLevelInfo()
    currentLevel = gameState["newGameState"]["levelTitle"]
    return allLevelsControl(userInput, currentLevel)

def allLevelsControl(userInput, currentLevel):
    if currentLevel == "Main porch":
        return porch(userInput, currentLevel)
    elif currentLevel == "Outside":
        return outside(userInput, currentLevel)
    elif currentLevel == "Shed":
        return shed(userInput, currentLevel)

def porch(userInput, currentLevel):
    levelPorch = currentLevel
    if userInput == "go forward" and levelPorch:
        return wrongPorchDirection()
    elif userInput == "go back" and levelPorch:
        newLevelInfo = {
            "newGameState": {
                "levelTitle": "Outside",
                "levelDescription": "outside",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
        saveNewLevelInfo(newLevelInfo)
        return newLevelInfo
    elif userInput == "go left" and levelPorch:
        return wrongPorchDirection()
    elif userInput == "go right" and levelPorch:
        return wrongPorchDirection()
    else:
        return wrongUserInput()

def wrongPorchDirection():
    return {
            "newGameState": {
                "levelTitle": "Outside",
                "levelDescription": "outside",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }

def outside(userInput, currentLevel):
    if userInput == "go forward":
        newLevelInfo = {
            "newGameState": {
                "levelTitle": "Main porch",
                "levelDescription": "Youre in porch",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
        saveNewLevelInfo(newLevelInfo)
        return newLevelInfo
    elif userInput == "go back":
        return wrongOutsideDirection()
    elif userInput == "go left":
        #open file, overwrite with new level info, then return file info
        newLevelInfo = {
            "newGameState": {
                "levelTitle": "Shed",
                "levelDescription": "Youre in the shed",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
        saveNewLevelInfo(newLevelInfo)
        return newLevelInfo
    elif userInput == "go right":
        return wrongOutsideDirection()
    else: 
        return wrongUserInput()

def wrongOutsideDirection():
    return {
            "newGameState": {
                "levelTitle": "Shed",
                "levelDescription": "Youre in the shed",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
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
        newLevelInfo = {
            "newGameState": {
                "levelTitle": "Outside",
                "levelDescription": "Youre in outside",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
        saveNewLevelInfo(newLevelInfo)
        return newLevelInfo
    else:
        return wrongUserInput()
        

def wrongShedDirection():
    return {
            "newGameState": {
                "levelTitle": "Shed",
                "levelDescription": "Youre in outside",
                "levelChatboxText": "YAY"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }

def wrongUserInput():
    return {
            "newGameState": {
                "levelTitle": None,
                "levelDescription": None,
                "levelChatboxText": "invalid input"
            },
            "inventory": {
                "firstObject": True,
                "secondObject": False
            }
        }
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

def getLevelInfo():
    with open("result.json", "r") as getTheFile:
        theFile = json.load(getTheFile)
        return theFile

def saveNewLevelInfo(response):
    with open("result.json", "w") as theFile:
        json.dump(response, theFile,  indent=2)

        

        