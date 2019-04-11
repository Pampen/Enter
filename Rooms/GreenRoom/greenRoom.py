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
    if state['level'] == 'BEACH':
        return handleRoom(userInput, state)
    elif state['level'] == 'GATE':
        return handleGate(userInput, state)
    elif state['level'] == 'LIGHTHOUSE_OUTSIDE':
        return lighthouseOutside(userInput, state)
    elif state['level'] == 'LIGHTHOUSE':
        return lighthouse(userInput, state)
    elif state['level'] == 'LIGHTHOUSE_TOP':
        return lighthouseTop(userInput, state)
    elif state['level'] == 'OUTSIDE_SHED':
        return handleOutsideShed(userInput, state)
    elif state['level'] == 'SHED':
        return handleShed(userInput, state)
    elif state['level'] == 'OUTSIDE_SHIPWRECK':
        return handleOutsideShipwreck(userInput, state)
    elif state['level'] == 'SHIPWRECK':
        return handleShipwreck(userInput, state)
    elif state['level'] == 'CABIN':
        return handleCabin(userInput, state)
    elif state['level'] == 'CELLAR':
        return handleCellar(userInput, state)

def handleRoom(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'OUTSIDE_SHED')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'GATE')
    elif userInput == 'GO SOUTH':
        return handleOcean(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "OUTSIDE_SHIPWRECK")
    else:
        return handleInvalidInput(userInput, state)

def handleGate(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE_OUTSIDE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def lighthouseOutside(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def lighthouse(userInput, state):
    if userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == "GO NORTH":
        return goToLevel(state, "LIGHTHOUSE_TOP")
    else:
        return handleInvalidInput(userInput, state)

def lighthouseTop(userInput, state):
    if userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "LIGHTHOUSE")
    else:
        return handleInvalidInput(userInput, state)

def handleOutsideShed(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHED')
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH")
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        return goToLevel(state, "CELLAR")
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH")
    else:
        return handleInvalidInput(userInput, state)

def handleOutsideShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'SHIPWRECK')
    elif userInput == 'GO SOUTH' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH')
    elif userInput == "GO EAST":
        return goToLevel(state, "CABIN")
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCabin(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHIPWRECK')
    elif userInput == "GO EAST" or userInput == "GO NORTH" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCellar(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO NORTH" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, "SHED")
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
            'levelChatboxText': 'You cannot {}'.format(userInput) + '.'
        }
    }
    return response

def openLevelFile():
    with open('Rooms/GreenRoom/room_data.json', 'r') as getData:
        data = json.loads(getData.read())
        return data

def handleOcean(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The sea is behind you, going south isn't going to work."
        }
    }
    return response  