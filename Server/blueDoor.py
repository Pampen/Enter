from saveLevelAndWrongUserInput import checkTorchItem, handleInvalidDirection, handleInvalidInput,takeItem, checkTorchItem, goToLevel

def handleBlueStart(userInput, state):
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_TORCH_ROOM', userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleTorchRoom(userInput, state):
    if userInput == "TAKE TORCH":
        return takeItem(state, 'torch')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_START', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor1(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_START', userInput)
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_2', userInput)
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_5', userInput)
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_4', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor2(userInput, state):
    if userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_3', userInput)
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1', userInput)
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor3(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_2', userInput)
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_4', userInput)
    elif userInput == "TAKE RUSTY KEY":
        return takeItem(state, 'rustyKey')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor4(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1', userInput)
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_3', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor5(userInput, state):
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1', userInput)
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6', userInput)
    if userInput == 'GO SOUTH' or userInput == 'GO EAST':
       return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor6(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_5', userInput)
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_7', userInput)
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_8', userInput)
    elif userInput == 'GO WEST': 
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor7(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6', userInput)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor8(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_9', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor9(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH': 
        return checkTorchItem(state, 'BLUE_FINISH', userInput)
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_9', userInput)
    else:
        return handleInvalidInput(userInput, state)


def handleBlueFinish(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_9', userInput)
    elif userInput == "TAKE BlUE KEY":
        return takeItem(state, 'blueKey')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
