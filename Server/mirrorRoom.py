from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMirrorRoomJoy(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'MIRROR_ROOM_ANGER', userInput)
    elif userInput == "GO SOUTH" or userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMirrorRoomAnger(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state,  'MIRROR_ROOM_LOVE', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'MIRROR_ROOM_JOY', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMirrorRoomLove(userInput, state):
    if userInput == "GO NORTH":
        return goToLevel(state, 'MIRROR_ROOM_SADNESS', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, 'MIRROR_ROOM_ANGER', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMirrorRoomSadness(userInput, state):
    if userInput == "GO SOUTH":
        return goToLevel(state, 'MIRROR_ROOM_LOVE', userInput)
    elif userInput == "GO WEST" or userInput == "GO EAST" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)