from utilities import handleInvalidDirection, goToLevel, handleInvalidInput

def handleMainHall(userInput, state):
    if userInput == 'GO SOUTH':
        return handleInvalidDirection(userInput)
    elif userInput == 'GO NORTH' and 'greenKey' in state['inventory']:
        if 'redKey' in state['inventory']:
            return finishedLevel(userInput, state)
        else:
            return goToLevel (state, 'LIVING_ROOM', userInput)
    elif userInput == 'GO EAST' and 'redKey' in state['inventory']:
        if 'pinkKey' in state['inventory']:
            return finishedLevel(userInput, state)
        else:
            return goToLevel (state, 'CRIB_ROOM', userInput)
    elif userInput == 'GO WEST': 
        if 'greenKey' in state['inventory']:
            return finishedLevel(userInput, state)
        else:
            return goToLevel (state, 'BEACH', userInput)
    elif userInput == 'TAKE CREEPY PAINTINGS' or userInput == 'TAKE PAINTINGS':
        return handleInvalidPaintings(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHallAllKeys(userInput, state):
    if userInput == 'USE GREEN KEY':
        return goToLevel (state, 'MAIN_HALL_RED_KEY', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHallRedKey(userInput, state):
    if userInput == 'USE RED KEY':
        return goToLevel (state, 'MAIN_HALL_PINK_KEY', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHallPinkKey(userInput, state):
    if userInput == 'USE PINK KEY':
        return goToLevel (state, 'MAIN_HALL_BLUE_KEY', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleMainHallBlueKey(userInput, state):
    if userInput == 'USE BLUE KEY':
        return goToLevel (state, 'MIRROR_ROOM_1', userInput)
    else:
        return handleInvalidInput(userInput, state)

def finishedLevel(userInput, state):
    response = {
    'state': state,
    'pageChanges': {
        'levelChatboxText': 'You cannot go ' + userInput.upper() + '. You have already finished that level.'
    }
}
    return response

def handleInvalidPaintings(state):
    response = {
    'state': state,
    'pageChanges': {
        'levelChatboxText': 'Ehm...why would you even try that? You can do better.'
    }
}
    return response