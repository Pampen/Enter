from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from blueDoor import handleBlueStart, handleBlueFinish, handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleTourchRoom
from tutorial import handleOutside, handleShed, handlePorch
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