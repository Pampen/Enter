from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock, usePersistantItem

def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        if "lightswitch" in state['usedItems']:
            return goToLevel(state, 'GREENHOUSE_LIGHT_ON', userInput)
        else:
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
        return usePersistantItem(state, "lightswitch", "GREENHOUSE_LIGHT_ON")
    elif userInput == "TAKE BRASS KEY" or userInput == "TAKE KEY":
        return takeItem(state, 'brassKey')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)