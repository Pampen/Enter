from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from blueDoor import handleBlueStart, handleBlueFinish, handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleTourchRoom
from tutorial import handleOutside, handleShed, handlePorch
from MainHall import handleMainHall
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

    return jsonify(response) #Return value of variable 'response' to JavaScript

def getResponse(userInput, state):
    if state['level'] == 'OUTSIDE':
        return handleOutside(userInput, state)
    elif state['level'] == 'SHED':
        return handleShed(userInput, state)
    elif state['level'] == 'PORCH':
        return handlePorch(userInput, state)
    elif state['level'] == "Blue start":
        return handleBlueStart(userInput, state)
    elif state['level'] == "Blue Tourch Room":
        return handleTourchRoom(userInput, state)
    elif state['level'] == "Blue Corridor 1":
        return handleBlueCorridor1(userInput, state)
    elif state['level'] == "Blue Corridor 2":
        return handleBlueCorridor2(userInput, state)
    elif state['level'] == "Blue Corridor 3":
        return handleBlueCorridor3(userInput, state)
    elif state['level'] == "Blue Corridor 4":
        return handleBlueCorridor4(userInput, state)
    elif state['level'] == "Blue Corridor 5":
        return handleBlueCorridor5(userInput, state)
    elif state['level'] == "Blue Corridor 6":
        return handleBlueCorridor6(userInput, state)
    elif state['level'] == "Blue Corridor 7":
        return handleBlueCorridor7(userInput, state)
    elif state['level'] == "Blue Corridor 8":
        return handleBlueCorridor8(userInput, state)
    elif state['level'] == "Blue Corridor 9":
        return handleBlueCorridor9(userInput, state)
    elif state['level'] == "Blue Finish":
        return handleBlueFinish(userInput, state)
    elif state['level'] == 'MAIN HALL':
        return handleMainHall(userInput, state)
    elif state['level'] == 'LIVING ROOM':
        return handleLivingRoom(userInput, state)
    elif state['level'] == 'KITCHEN':
        return handleKitchen(userInput, state)
    elif state['level'] == 'HALL':
        return handleHall(userInput, state)
    elif state['level'] == 'UPPER FLOOR':
        return handleUpperFloor(userInput, state)
    elif state['level'] == 'BEDROOM':
        return handleBedroom(userInput, state)
    elif state['level'] == 'BASEMENT':
        return handleBasement(userInput, state)
    elif state['level'] == 'ATTIC':
        return handleAttic(userInput, state)

def handleLivingRoom(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'KITCHEN')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'HALL')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'LIVING ROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'BASEMENT')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'LIVING ROOM')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'UPPER FLOOR')
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'HALL')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'BEDROOM')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'ATTIC')
    elif userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'UPPER FLOOR')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBedroom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'UPPER FLOOR')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'KITCHEN')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def goToLevel(state, currentLevel):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": ''
        }
    }
    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def handleInvalidDirection(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot go that way.'
        }
    }
    return response  

def handleInvalidInput(userInput, state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot ' + userInput + '.'
        }
    }
    return response 

def openLevelFile():
    with open('tutorial.json', 'r') as getData:
        data = json.loads(getData.read())
        return data
