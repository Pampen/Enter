from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO NORTH':
        return goToLevel (state, 'LIVING ROOM')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == 'GO WEST':  
        return goToLevel(state, 'BEACH')
    else:
        return handleInvalidInput(userInput, state)