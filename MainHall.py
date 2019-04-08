import json

def handleMainHall(userInput, state):
    if userInput == 'GO EAST':
        return handleBluePorch(userInput, state) 
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)