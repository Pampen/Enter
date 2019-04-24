from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem

def handleCribroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'BABYROOM')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'MESSYROOM')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'MAIN HALL')
    elif userInput == "TAKE CRIB":
        return takeItem(state, 'crib')
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'NURSINGROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == "TAKE WORN DOLL":
        return takeItem(state, 'wornDoll')
    elif userInput == "TAKE PINK KEY":
        return takeItem(state, 'pinkKey')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNursingroom(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BABYROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'STUDYROOM')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue start')
    elif userInput == "TAKE MOLDY PACIFIER":
        return takeItem(state, 'moldyPacifier')
    elif userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleStudyroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'NURSINGROOM')
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'MESSYROOM')
    elif userInput == "TAKE DIRTY BLANKET":
        return takeItem(state, 'dirtyBlanket')
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMessyroom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'STUDYROOM')
    elif userInput == 'GO WEST':
        return goToLevel(state, 'CRIBROOM')
    elif userInput == "TAKE TORN PAGES":
        return takeItem(state, 'tornPages')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'Blue start')
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)