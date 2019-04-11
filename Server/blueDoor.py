from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput

def handleBlueStart(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'Blue Torch Room')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'Blue Corridor 1')
    else:
        return handleInvalidInput(userInput, state)

def handleTorchRoom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'Blue start')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor1(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue start')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'Blue Corridor 2')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue Corridor 5')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'Blue Corridor 4')
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor2(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'Blue Corridor 3')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue Corridor 1')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor3(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue Corridor 2')
    if userInput == 'GO EAST':
        return goToLevel(state, 'Blue Corridor 4')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor4(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue Corridor 1')
    if userInput == 'GO WEST':
        return goToLevel(state, 'Blue Corridor 3')
    elif userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor5(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO EAST':
        handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'Blue Corridor 1')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'Blue Corridor 6')
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor6(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue Corridor 5')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue Corridor 7')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'Blue Corridor 8')
    elif userInput == 'GO WEST': 
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor7(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'Blue Corridor 6')
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor8(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue Corridor 6')
    elif userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'Blue Corridor 9')
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor9(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH': 
        return goToLevel(state, 'Blue Finish')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue Corridor 9')
    else:
        return handleInvalidInput(userInput, state)


def handleBlueFinish(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'Blue Corridor 9')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
