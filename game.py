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
    elif state['level'] == 'CRIBROOM':
        return handleCribroom(userInput, state)
    elif state['level'] == 'BABYROOM':
        return handleBabyroom(userInput, state)
    elif state['level'] == 'NURSINGROOM':
        return handleNursingroom(userInput, state)
    elif state['level'] == 'STUDYROOM':
        return handleStudyroom(userInput, state)
    elif state['level'] == 'MESSYROOM':
        return handleMessyroom(userInput, state)
    
    
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
    if userInput == 'GO EAST':
        return handleInvalidDirection(state)
    if userInput == 'GO NORTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHall(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
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

def handleCribroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'BABYROOM')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'MESSYROOM')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'NURSINGROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)

def handleNursingroom(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BABYROOM')
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'STUDYROOM')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)

def handleStudyroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'NURSINGROOM')
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MESSYROOM')
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)

def handleMessyroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'STUDYROOM')
    if userInput == 'GO WEST':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)

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