from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['POST'])
@cross_origin(supports_credentials=True)
def getRequest():

    getState = request.get_json()
    print(getState)
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
    
def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        return goToShed(state)
    elif userInput == 'GO NORTH':
        return goToPorch(state)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handlePorch(userInput, state):
    if userInput == 'GO SOUTH':
        return goToOutside(state)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO EAST':
        return goToOutside(state)
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def goToOutside(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': 'Outside',
            'levelDescription': 'This is outside.'
        }
    }
    response['state']['level'] = 'OUTSIDE'
    print(response)
    return response

def goToShed(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': 'Shed',
            'levelDescription': 'This is a shed.'
        }
    }
    response['state']['level'] = 'SHED'
    return response

def goToPorch(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': 'Porch',
            'levelDescription': 'This is a porch.'
        }
    }
    response['state']['level'] = 'PORCH'
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