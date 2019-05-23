from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput, handleDoorLock, takeItem

def handleMirrorRoom1(userInput, state):
    if userInput == "GO EAST":
        return goToLevel(state, 'MIRROR_ROOM_2', userInput)
    elif userInput == "GO SOUTH" or userInput == "GO WEST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMirrorRoom2(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'JOY', userInput)
    elif userInput == "GO WEST":
        return goToLevel(state, 'MIRROR_ROOM_1', userInput)
    elif userInput == "GO SOUTH" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleJoy(userInput, state):
    if userInput == "GO WEST":
        return goToLevel(state, 'ANGER_1', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'MIRROR_ROOM_2', userInput)
    elif userInput == "NORTH" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAnger1(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'ANGER_2', userInput)
    elif userInput == "GO EAST":
        return goToLevel(state, 'JOY', userInput)
    elif userInput == "GO WEST" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAnger2(userInput, state):
    if userInput == "GO EAST":
        return goToLevel(state, 'LOVE', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'ANGER_1', userInput)
    elif userInput == "GO WEST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLove(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'SADNESS_1', userInput)
    elif userInput == "GO WEST":
        return goToLevel(state, 'ANGER_2', userInput)
    elif userInput == "GO SOUTH" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleSadness1(userInput, state):
    if userInput == "GO WEST":
        return goToLevel(state, 'SADNESS_2', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'LOVE', userInput)
    elif userInput == "GO EAST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleSadness2(userInput, state):
    if userInput == 'TAKE POCKET WATCH' or userInput == 'TAKE WATCH':
        return goToLevel(state, "END", userInput)
    elif userInput == "GO EAST":
        return goToLevel(state, 'SADNESS_1', userInput)
    elif userInput == "GO WEST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)