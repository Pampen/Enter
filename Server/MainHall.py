from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput

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