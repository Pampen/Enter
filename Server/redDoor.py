from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock

def handleLivingRoom(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'TAKE RED KEY':
        return takeItem(state, 'redKey')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'HALL', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomdDesc(state)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE PHOTOGRAPH':
        return takeItem(state, 'photograph') 
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        return goToLevel(state, 'BASEMENT', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomdDesc(state)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE CAR KEYS':
        return takeItem(state, 'carKeys')
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        return goToLevel(state, 'HALL', userInput)
    elif userInput == 'USE GREY KEY' and "greyKey" in state["inventory"]:
        return goToLevel(state, 'BEDROOM', userInput)
    elif userInput == 'GO WEST':
        return handleDoorLock(state, 'UPPER_FLOOR_W', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        return goToLevel(state, 'ATTIC', userInput)
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'UPPER_FLOOR_N', userInput)
    elif userInput == 'GO EAST' or  userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO SOUTH':
        return handleDoorLock(state, 'ATTIC', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE GREY KEY':
        return takeItem(state, 'greyKey')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBedroom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE CANVAS':
        return takeItem(state, 'canvas')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'TAKE LADDER':
        return takeItem(state, 'ladder')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNewLivingRoomdDesc(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Living Room",
            'levelDescription': "With the canvas, car keys and the photograph in your possesion you can feel the heat from the fireplace, some things are meant to be burned down to ashes."
        }
    }
    return response