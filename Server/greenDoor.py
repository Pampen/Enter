from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

def handleBeach(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'OUTSIDE_SHED')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'GATE')
    elif userInput == 'GO SOUTH':
        return handleOcean(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "OUTSIDE_SHIPWRECK")
    else:
        return handleInvalidInput(userInput, state)

def handleGate(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE_OUTSIDE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseOutside(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouse(userInput, state):
    if userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == "GO NORTH":
        return goToLevel(state, "LIGHTHOUSE_TOP")
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseTop(userInput, state):
    if userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "LIGHTHOUSE")
    else:
        return handleInvalidInput(userInput, state)

def handleOutsideShed(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHED')
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH")
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        return goToLevel(state, "CELLAR")
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH")
    else:
        return handleInvalidInput(userInput, state)

def handleOutsideShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'SHIPWRECK')
    elif userInput == 'GO SOUTH' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH')
    elif userInput == "GO EAST":
        return goToLevel(state, "CABIN")
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCabin(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHIPWRECK')
    elif userInput == "GO EAST" or userInput == "GO NORTH" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCellar(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO NORTH" or userInput == "GO EAST":
        return handleInvalidDirection(state)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, "SHED")
    else:
        return handleInvalidInput(userInput, state)

def handleOcean(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The sea is behind you, going south isn't going to work."
        }
    }
    return response  