from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock, handlePersistantItems

def handleOutside(userInput, state):
    if userInput == 'GO WEST':
        if "lightswitch" in state['usedItems'] and "brassKey" in state['inventory']:
            return goToLevel(state, 'GREENHOUSE_LIGHT_AND_KEY_ON', userInput)
        elif "lightswitch" in state['usedItems']:
            return goToLevel(state, 'GREENHOUSE_LIGHT_ON', userInput)
        else:
            return goToLevel(state, 'GREENHOUSE', userInput)
    elif userInput == 'LICK DOOR':
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'PET THE BABY':
        return goToLevel(state, 'CRIB_ROOM', userInput)
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
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'PORCH', userInput)
    elif userInput == 'GO EAST' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleGreenHouse(userInput, state):
    if userInput == 'GO EAST':
        return goToLevel(state, 'OUTSIDE', userInput)
    elif userInput == "USE LIGHTSWITCH":
        return handlePersistantItems(state, "lightswitch", "GREENHOUSE_LIGHT_ON")
    elif userInput == "TAKE BRASS KEY" or userInput == "TAKE KEY":
        if "lightswitch" in state['usedItems']:
            return takeItem(state, 'brassKey')
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