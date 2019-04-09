from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO NORTH':
        return goToLevel (state, 'LIVING ROOM')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue start')
    elif userInput == 'GO WEST':  
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)