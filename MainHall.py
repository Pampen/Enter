from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'PORCH')
    elif userInput == 'GO NORTH':
        return goToLevel (state, 'LIVING ROOM')
    elif userInput == 'GO WEST' or  userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)