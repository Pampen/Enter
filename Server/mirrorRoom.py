from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput, handleDoorLock, takeItem

def handleMirrorRoom(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'JOY', userInput)
    elif userInput == "GO SOUTH" or userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleJoy(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'ANGER', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'MIRROR_ROOM', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAnger(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'LOVE', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'JOY', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLove(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'SADNESS', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'ANGER', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleSadness(userInput, state):
    if userInput == 'GO SOUTH':
        return handleDoorLock(state, 'MIRROR_ROOM', userInput)
    elif userInput == 'TAKE POCKET WATCH' or userInput == 'TAKE WATCH':
        return takeItem(state, 'pocketWatch')
    elif userInput == "GO WEST" or userInput == "GO EAST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)