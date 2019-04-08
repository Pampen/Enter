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
    elif state['level'] == 'FURY':
        return handleFury(userInput, state)
    elif state['level'] == 'ANGER':
        return handleAnger(userInput, state)
    elif state['level'] == 'WRATH':
        return handleWrath(userInput, state)
    elif state['level'] == 'RESENTMENT':
        return handleResentment(userInput, state)
    elif state['level'] == 'BITTERNESS':
        return handleBitterness(userInput, state)
    elif state['level'] == 'RAGE':
        return handleRage(userInput, state)
    
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
        return goToLevel (state, 'FURY')
    elif userInput == 'GO WEST' or  userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleFury(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'ANGER')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'WRATH')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAnger(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'FURY')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'RAGE')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleWrath(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'FURY')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'RESENTMENT')
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleResentment(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'WRATH')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'BITTERNESS')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBitterness(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'RESENTMENT')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleRage(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'ANGER')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
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