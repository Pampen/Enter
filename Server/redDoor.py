from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem

def handleLivingRoom(userInput, state):
    if userInput == 'GO SOUTH':
<<<<<<< HEAD
        return goToLevel(state, 'MAIN HALL', userInput)
=======
        return goToLevel(state, 'MAIN_HALL')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'TAKE RED KEY':
        return takeItem(state, 'redKey')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'HALL', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
<<<<<<< HEAD
        return goToLevel(state, 'LIVING ROOM', userInput)
=======
        return goToLevel(state, 'LIVING_ROOM')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'TAKE PHOTOGRAPH':
        return takeItem(state, 'photograph') 
    elif userInput == 'TAKE STAIRS':
        return goToLevel(state, 'BASEMENT', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
<<<<<<< HEAD
        return goToLevel(state, 'LIVING ROOM', userInput)
    elif userInput == 'TAKE CAR KEYS':
        return takeItem(state, 'carKeys')
    elif userInput == 'TAKE STAIRS':
        return goToLevel(state, 'UPPER FLOOR', userInput)
=======
        return goToLevel(state, 'LIVING_ROOM')
    elif userInput == 'TAKE CAR KEYS':
        return takeItem(state, 'carKeys')
    elif userInput == 'TAKE STAIRS':
        return goToLevel(state, 'UPPER_FLOOR')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'TAKE STAIRS':
        return goToLevel(state, 'HALL', userInput)
    elif userInput == 'GO WEST':
        return goToLevel(state, 'BEDROOM', userInput)
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'ATTIC', userInput)
    elif userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO SOUTH':
<<<<<<< HEAD
        return goToLevel(state, 'UPPER FLOOR', userInput)
=======
        return goToLevel(state, 'UPPER_FLOOR')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'TAKE GREY KEY':
        return takeItem(state, 'greyKey')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBedroom(userInput, state):
    if userInput == 'GO EAST':
<<<<<<< HEAD
        return goToLevel(state, 'UPPER FLOOR', userInput)
=======
        return goToLevel(state, 'UPPER_FLOOR')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'TAKE CANVAS':
        return takeItem(state, 'canvas')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
<<<<<<< HEAD
    if userInput == 'TAKE STAIRS':
        return goToLevel(state, 'KITCHEN', userInput)
=======
    if userInput == 'TAKE_STAIRS':
        return goToLevel(state, 'KITCHEN')
>>>>>>> 1054ee99653a122feb05cfc34a2239d858530d39
    elif userInput == 'TAKE LADDER':
        return takeItem(state, 'ladder')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)