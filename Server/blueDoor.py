from saveLevelAndWrongUserInput import checkTorchItem, handleInvalidDirection, handleInvalidInput, takeItem, checkTorchItem, handleDoorLock, handleUseItemBlueRoom, returnToMainHall, goToLevel, handlePersistantItems

def handleBlueStart(userInput, state):
    if userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_TORCH_ROOM', userInput)
        else:
            return goToLevel(state, 'BLUE_TORCH_ROOM', userInput) and handleTorchInTorchRoom(state, userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleTorchRoom(userInput, state):
    if userInput == "TAKE TORCH":
        return takeItem(state, 'torch')
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_START', userInput) 
        else:
            return goToLevel(state, 'BLUE_START', userInput) and handleTrueTorchLevel(state, userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor1(userInput, state):
    if userInput == 'GO SOUTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_START', userInput) 
        else:
            return goToLevel(state, 'BLUE_START', userInput) and handleTrueTorchLevel(state, userInput)
    elif userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_2', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_2', userInput) 
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_5', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_5', userInput) 
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_5', userInput) and handleRustyKeyPickupCorridor5(state, userInput)
    elif userInput == 'GO NORTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_4', userInput) and handleFalseTorchLevel(state, userInput) 
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_4', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor2(userInput, state):
    if userInput == 'GO NORTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput) and handleRustyKeyPickup(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput)
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleRustyKeyPickupCorridor1(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput)
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor3(userInput, state):
    if userInput == 'GO SOUTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_2', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_2', userInput) and handleRustyKeyPickupCorridor2(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_2', userInput)
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_4', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_4', userInput)
        else:
             return goToLevel(state, 'BLUE_CORRIDOR_4', userInput) and handleRustyKeyPickupCorridor4(state, userInput)
    elif userInput == "TAKE RUSTY KEY":
        return takeItem(state, 'rustyKey') and handleRustyKeyPickup(state, userInput)
    elif userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor4(userInput, state):
    if userInput == 'GO SOUTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleRustyKeyPickupCorridor1(state, userInput)
    if userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput) and handleRustyKeyPickup(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_3', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor5(userInput, state):
    if userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_1', userInput)
    elif userInput == 'GO NORTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_6', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_6', userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
       return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor6(userInput, state):
    if userInput == 'GO SOUTH':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_5', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_5', userInput)
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_7', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_7', userInput)
    elif userInput == 'GO NORTH':
        if "rustyKey" in state['inventory']:
            if state['inventory']['rustyKey']['itemUse'] == True:
                return goToLevel(state, 'BLUE_CORRIDOR_8', userInput)
            else:
                return handleDoorLock(state, 'BLUE_CORRIDOR_6', userInput)
        else:
            return handleDoorLock(state, 'BLUE_CORRIDOR_6', userInput)
    elif userInput == 'GO WEST': 
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor7(userInput, state):
    if userInput == 'USE RUSTY KEY' and "rustyKey" in state["inventory"]:
        state['inventory']['rustyKey']['itemUse'] = True
        return handlePersistantItems(state, 'rustyKey', 'BLUE_CORRIDOR_7') and handleUseRustyKey(state, userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_6', userInput) and handleFalseTorchLevel(state, userInput)
        elif 'rustyKey' in state['usedItems']:
            return goToLevel(state, 'BLUE_CORRIDOR_6', userInput) and handleRustyKeyPickupCorridor6(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_6', userInput)
    else:
        return handleInvalidInput(userInput, state)
    
def handleBlueCorridor8(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'BLUE_CORRIDOR_6', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO NORTH': 
        return handleInvalidDirection(state)
    elif userInput == 'GO WEST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_9', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_9', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueCorridor9(userInput, state):
    if userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == 'GO NORTH': 
        return goToLevel(state, 'BLUE_FINISH', userInput)
    elif userInput == 'GO EAST':
        if 'torch' not in state['inventory']:
            return goToLevel(state, 'BLUE_CORRIDOR_8', userInput) and handleFalseTorchLevel(state, userInput)
        else:
            return goToLevel(state, 'BLUE_CORRIDOR_8', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBlueFinish(userInput, state):
    if userInput == 'TAKE BLUE KEY' or userInput == 'TAKE KEY':
        return state['inventory'].pop('torch') and state['inventory'].pop('rustyKey') and returnToMainHall(state, 'blueKey', 'MAIN_HALL')
    elif userInput == 'GO WEST' or userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleFalseTorchLevel(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "A pitch black room, you can barely see your hands in front of you.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleTrueTorchLevel(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Blue start",
            "levelDescription": "With the torch in hand you can make out the end of the hallway in front of you. You also hear a faint sobbing.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleTorchInTorchRoom(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Torch Room",
            "levelDescription": "Looks like you've already done everything there's to do in this room.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickup(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "With the key in your hand the sobbing continues. You can make out that it's coming from your right.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickupCorridor4(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "The sobbing returns, you can make out that it's coming from behind you.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickupCorridor2(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "The sobbing returns, you can make out that it's coming from your right.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickupCorridor1(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "You can make out that the sobbing is coming from your right.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickupCorridor5(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "The sobbing increases, you can make out that it's coming infront of you.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleRustyKeyPickupCorridor6(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "With the gate open you can now make your way forward.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleUseRustyKey(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Corridor",
            "levelDescription": "The gate has now opened. You can make out that the sobbing is coming from your left.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response