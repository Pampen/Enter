from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
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
    
def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHED')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handlePorch(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'OUTSIDE')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'OUTSIDE')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO NORTH':
        return goToLevel (state, 'LIVING ROOM')
    elif userInput == 'GO WEST' or  userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

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