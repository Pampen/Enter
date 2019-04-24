from saveLevelAndWrongUserInput import checkTorchItem, handleInvalidDirection, handleInvalidInput, takeItem, checkTorchItem, handleDoorLock, handleUseItemBlueRoom

def handleBlueStart(userInput, state):
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_TORCH_ROOM')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1')
    else:
        return handleInvalidInput(userInput, state)

def handleTorchRoom(userInput, state):
    if userInput == "TAKE TORCH":
        return takeItem(state, 'torch')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_START')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor1(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_START')
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_2')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_5')
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_4')
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor2(userInput, state):
    if userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_3')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor3(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_2')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_4')
    elif userInput == "TAKE RUSTY KEY":
        return takeItem(state, 'rustyKey')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor4(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1')
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_3')
    elif userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor5(userInput, state):
    if userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_1')
    elif userInput == 'GO NORTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6')
    if userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor6(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_5')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_7')
    elif userInput == 'GO NORTH':
        if "rustyKey" in state['inventory']:
            if state['inventory']['rustyKey']['itemUse'] == True:
                return checkTorchItem(state, 'BLUE_CORRIDOR_8')
            else:
                return handleDoorLock(state, 'BLUE_CORRIDOR_6')
        else:
            return handleDoorLock(state, 'BLUE_CORRIDOR_6')
    elif userInput == 'GO WEST': 
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor7(userInput, state):
    if userInput == 'USE RUSTY KEY' and "rustyKey" in state["inventory"]:
        state['inventory']['rustyKey']['itemUse'] = True
        return handleUseItemBlueRoom(state, 'BLUE_CORRIDOR_7')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6')
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor8(userInput, state):
    if userInput == 'GO SOUTH':
        return checkTorchItem(state, 'BLUE_CORRIDOR_6')
    elif userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_9')
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor9(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH': 
        return checkTorchItem(state, 'BLUE_FINISH')
    elif userInput == 'GO EAST':
        return checkTorchItem(state, 'BLUE_CORRIDOR_8')
    else:
        return handleInvalidInput(userInput, state)

def handleBlueFinish(userInput, state):
    if userInput == "TAKE BLUE KEY":
        return takeItem(state, 'blueKey')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
