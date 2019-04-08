def handleLivingRoom(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'KTICHEN')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'HALL')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'LIVING ROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'BASEMENT')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'LIVING ROOM')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'UPPER FLOOR')
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'HALL')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'ATTIC')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'UPPER FLOOR')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'KITCHEN')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)