from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock

def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'GREENHOUSE', userInput)
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'PORCH', userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handlePorch(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'OUTSIDE', userInput)
    elif userInput == 'USE BRASS KEY' and "brassKey" in state["inventory"]:
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'PORCH', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleGreenHouse(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'OUTSIDE', userInput)
    elif userInput == "USE LIGHTSWITCH":
        state['usedItems']['lightSwitch'] = True
        return goToLevel(state, 'GREENHOUSE_LIGHT_ON', userInput)
    elif userInput == "TAKE BRASS KEY":
        return takeItem(state, 'brassKey')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)