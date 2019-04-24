from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'PORCH', userInput)
    elif userInput == 'GO NORTH':
        return goToLevel (state, 'LIVING ROOM', userInput)
    elif userInput == 'GO EAST':
        return goToLevel(state, 'CRIBROOM', userInput)
    elif userInput == 'GO WEST':  
        return goToLevel(state, 'BEACH', userInput)
    else:
        return handleInvalidInput(userInput, state)