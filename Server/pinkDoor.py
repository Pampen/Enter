from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem

def handleCribRoom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO EAST':
        return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == "TAKE CRIB":
        return takeItem(state, 'crib')
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoom(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == "TAKE WORN DOLL":
        return takeItem(state, 'wornDoll')
    elif userInput == "USE CRIB" and 'crib' in state['inventory']: 
        return goToLevel(state, 'BABYROOMCRIB', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

<<<<<<< HEAD
def handleBabyroomcrib(userInput, state):
    if userInput == "USE WORN DOLL" and 'wornDoll' in state['inventory']: 
        return goToLevel(state, 'BABYROOMDOLL', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroomdoll(userInput, state):
    if userInput == "USE DIRTY BLANKET" and 'dirtyBlanket' in state['inventory']: 
        return goToLevel(state, 'BABYROOMBLANKET', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroomblanket(userInput, state):
    if userInput == "USE MOLDY PACIFIER" and 'moldyPacifier' in state['inventory']: 
        return goToLevel(state, 'BABYROOMPACIFIER', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroompacifier(userInput, state):
    if userInput == "Bye baby Bunting Mommy's gone hunting gone to get a rabbit skin to wrap the baby Bunting in" and 'nurseryRhyme' in state['inventory']: 
        return goToLevel(state, 'BABYROOMKEY', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyroomkey(userInput, state):
    if userInput == "TAKE PINK KEY":
        return takeItem(state, 'pinkKey')
    elif userInput == "GO EAST" and 'pinkKey' in state['inventory']: 
        return goToLevel(state, 'BLUE_START', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleNursingroom(userInput, state):
=======
def handleNursingRoom(userInput, state):
>>>>>>> 3eecd09b533e04a835fd4e16a88358969bebebef
    if userInput == 'GO WEST':
        return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO EAST':
        return goToLevel(state, 'BLUE_START', userInput)
    elif userInput == "TAKE MOLDY PACIFIER":
        return takeItem(state, 'moldyPacifier')
    elif userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleStudyRoom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == "TAKE DIRTY BLANKET":
        return takeItem(state, 'dirtyBlanket')
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMessyRoom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO WEST':
<<<<<<< HEAD
        return goToLevel(state, 'CRIBROOM', userInput)
    elif userInput == "TAKE NURSERY RHYME":
        return takeItem(state, 'nurseryRhyme')
=======
        return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == "TAKE TORN PAGES":
        return takeItem(state, 'tornPages')
>>>>>>> 3eecd09b533e04a835fd4e16a88358969bebebef
    elif userInput == 'GO EAST':
        return goToLevel(state, 'BLUE_START', userInput)
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)