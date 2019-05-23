from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock, handlePersistantItems

def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        if "lightswitch" in state['usedItems'] and "brassKey" in state['inventory']:
            return goToLevel(state, 'GREENHOUSE', userInput) and handleKeyTakeGreenhouse(state)
        elif "lightswitch" in state['usedItems']:
            return goToLevel(state, 'GREENHOUSE', userInput) and handleLightGreenhouse(state)
        else:
            return goToLevel(state, 'GREENHOUSE', userInput)
    elif userInput == 'LICK DOOR':
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'LOOK NICE':
        return goToLevel(state, 'MIRROR_ROOM_1', userInput)
    elif userInput == 'MR JALS':
        return goToLevel(state, 'SADNESS', userInput)
    elif userInput == 'PET THE BABY':
        return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == 'GO NOWHERE':
        return goToLevel(state, 'NOWHERE', userInput)
    elif userInput == 'SMASH':
        return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'HAVE A NICE DAY':
        return goToLevel(state, 'BEACH', userInput)
    elif userInput == 'ABSOLUTE LEGEND':
        return goToLevel(state, 'MAIN_HALL_ALL_KEYS', userInput)
    elif userInput == 'TAKE A SAD SHOWER':
        return goToLevel(state, 'BLUE_START', userInput)
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'PORCH', userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handlePorch(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'OUTSIDE', userInput)
    elif userInput == 'USE BRASS KEY' or userInput == 'USE KEY' and "brassKey" in state["inventory"]:
        return state['inventory'].pop('brassKey') and goToLevel(state, 'MAIN_HALL', userInput) 
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'PORCH', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNowhere(userInput, state):
    if userInput == 'GET BACK':
        return goToLevel(state, 'NOWHERE', userInput)
    else:
        return handleInvalidDirection(state)
 

def handleGreenHouse(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'OUTSIDE', userInput)
    elif userInput == "USE LIGHTSWITCH":
        return handlePersistantItems(state, "lightswitch", "GREENHOUSE") and handleLightGreenhouse(state)
    elif userInput == "TAKE BRASS KEY" or userInput == "TAKE KEY":
        if "lightswitch" in state['usedItems']:
            return takeItem(state, 'brassKey') and handleKeyTakeGreenhouse(state)
        else:
            return {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "It's too dark to see anything, try turning on the light first"
        }
    } 
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLightGreenhouse(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "GREENHOUSE",
            "levelDescription": "There isn't that many things inside broken glass, a big bookcase and some dead plants. No one has been watering the plants for days. In the middle of all this mess, you can see a brass key.",
            'levelChatboxText': "YOU USED THE LIGHTSWITCH."
        }
    }
    return response

def handleKeyTakeGreenhouse(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "GREENHOUSE",
            "levelDescription": "There isn't that many things inside broken glass, a big bookcase and some dead plants.",
            'levelChatboxText': "YOU TAKE BRASS KEY."
        }
    }
    return response
    