from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem
from blueDoor import handleBlueStart

def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'GREENHOUSE')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handlePorch(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'OUTSIDE')
    elif userInput == 'GO NORTH' and "brassKey" in state["inventory"]:
        if userInput == 'USE BRASS KEY':
            return goToLevel(state, 'MAIN_HALL')
        else:
            return handleInvalidInput(userInput, state)
    elif userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleGreenHouse(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'OUTSIDE')
    elif userInput == "TAKE BRASS KEY":
        return takeItem(state, 'brassKey')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)