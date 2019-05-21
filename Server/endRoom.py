from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock, handlePersistantItems

def handleLastRoom(userInput, state):
    if userInput == "GO NORTH" or userInput == "GO SOUTH" or userInput == "GO WEST" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)