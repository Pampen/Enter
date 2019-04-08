def handleFury(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'ANGER')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'WRATH')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAnger(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'FURY')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'RAGE')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleWrath(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'FURY')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'RESENTMENT')
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleResentment(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'WRATH')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'BITTERNESS')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBitterness(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'RESENTMENT')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleRage(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'ANGER')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)