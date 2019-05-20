from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock

def handleCribRoom(userInput, state):
    if userInput == 'GO NORTH':
            return goToLevel(state, 'TOY_CAR_ROOM', userInput)
    elif userInput == 'GO EAST':
        if 'nurseryRhyme' in state ['inventory']:
            return goToLevel(state, 'NURSERY_ROOM_NO_RHYME', userInput)
        else:
            return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == "TAKE CRIB":
        return takeItem(state, 'crib')
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCribRoomNoCrib(userInput, state):
    if userInput == 'GO NORTH':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO EAST':
        if 'nurseryRhyme' in state ['inventory']:
            return goToLevel(state, 'MESSY_ROOM_NO_RHYME', userInput)
        else:
            return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == 'GO WEST':
        return handleInvalidDirection(state)
    elif userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomNoDoll(userInput, state):
    if userInput == 'GO EAST':
        if 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, 'NURSING_ROOM_NO_PACIFIER', userInput)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
            return goToLevel(state, 'TOY_CAR_ROOM', userInput)
    elif userInput == "USE CRIB" and 'crib' and 'wornDoll' and 'moldyPacifier' and 'dirtyBlanket' and 'nurseryRhyme' not in state['inventory']: 
        return handleDoorLock(state, 'BABY_ROOM', userInput)
    elif userInput == "USE CRIB" and 'crib' and 'wornDoll' and 'moldyPacifier' and 'dirtyBlanket' and 'nurseryRhyme' in state['inventory']:
        return goToLevel(state, 'BABY_ROOM_CRIB', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoom(userInput, state):
    if userInput == 'GO EAST':
        if 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, "NURSING_ROOM_NO_PACIFIER", userInput)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
            return goToLevel(state, 'TOY_CAR_ROOM', userInput)
    elif userInput == "TAKE WORN DOLL" or userInput == "TAKE DOLL":
        return takeItem(state, 'wornDoll')
    elif userInput == "USE CRIB" and 'crib' and 'wornDoll' and 'moldyPacifier' and 'dirtyBlanket' and 'nurseryRhyme' not in state['inventory']: 
        return handleDoorLock(state, 'BABY_ROOM', userInput)
    elif userInput == "USE CRIB" and 'crib' and 'wornDoll' and 'moldyPacifier' and 'dirtyBlanket' and 'nurseryRhyme' in state['inventory']:
        return goToLevel(state, 'BABY_ROOM_CRIB', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomCrib(userInput, state):
    if userInput == "USE WORN DOLL" or userInput == "USE DOLL" and 'wornDoll' in state['inventory']: 
        return goToLevel(state, 'BABY_ROOM_DOLL', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomDoll(userInput, state):
    if userInput == "USE DIRTY BLANKET" or userInput == "USE BLANKET" and 'dirtyBlanket' in state['inventory']: 
        return goToLevel(state, 'BABY_ROOM_BLANKET', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomBlanket(userInput, state):
    if userInput == "USE MOLDY PACIFIER" or userInput == "USE PACIFIER" and 'moldyPacifier' in state['inventory']: 
        return goToLevel(state, 'BABY_ROOM_PACIFIER', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleToyCarRoom(userInput, state):
    if userInput == 'GO NORTH':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        if 'crib' in state ['inventory']:
            return goToLevel(state, 'CRIB_ROOM_NO_CRIB', userInput)
        else:
            return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomPacifier(userInput, state):
    if userInput == "USE NURSERY RHYME" or userInput == "USE RHYME" and 'nurseryRhyme' in state['inventory']: 
        return goToLevel(state, 'BABY_ROOM_KEY', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoomKey(userInput, state):
    if userInput == "TAKE PINK KEY" or userInput == "TAKE KEY":
        return takeItem(state, 'pinkKey')
    elif userInput == "GO EAST" and 'pinkKey' in state['inventory']: 
        return goToLevel(state, 'BLUE_START', userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleNursingRoom(userInput, state):
    if userInput == 'GO WEST':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
        return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == "TAKE MOLDY PACIFIER" or userInput == "TAKE PACIFIER":
        return takeItem(state, 'moldyPacifier')
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNursingRoomNoPacifier(userInput, state):
    if userInput == 'GO WEST':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
        return goToLevel(state, 'BABY_ROOM_NO_DOLL', userInput)
    if userInput == 'GO SOUTH':
        if 'dirtyBlanket' in state ['inventory']:
            return goToLevel(state, 'STUDY_ROOM_NO_BLANKET', userInput)
        else:
            return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleStudyRoomNoBlanket(userInput, state):
    if userInput == 'GO NORTH':
        if 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, 'NURSING_ROOM_NO_PACIFIER', userInput)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    if userInput == 'GO SOUTH':
        if 'nurseryRhyme' in state ['inventory']:
            return goToLevel(state,'MESSY_ROOM_NO_RHYME', userInput)
        else:
            return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state) 

def handleMessyRoomNoRhyme(userInput, state):
    if userInput == 'GO NORTH':
        if 'dirtyBlanket' in state ['inventory']:
            return goToLevel(state, 'STUDY_ROOM_NO_BLANKET', userInput)
        else:
            return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO WEST':
        if 'crib' in state ['inventory']:
            return goToLevel(state, 'CRIB_ROOM_NO_CRIB', userInput)
        else:
            return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleStudyRoom(userInput, state):
    if userInput == 'GO NORTH':
        if 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, 'NURSING_ROOM_NO_PACIFIER', userInput)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == "TAKE DIRTY BLANKET" or userInput == "TAKE BLANKET":
        return takeItem(state, 'dirtyBlanket')
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMessyRoom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO WEST':
        if 'crib' in state ['inventory']:
            return goToLevel(state, 'CRIB_ROOM_NO_CRIB', userInput)
        else:
            return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == "TAKE NURSERY RHYME" or userInput == "TAKE RHYME" or userInput == "TAKE NOTEBOOK":
        return takeItem(state, 'nurseryRhyme')
    elif userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def finishPuzzleFirst(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelChatboxText": "Before you move on you need to solve the puzzle for this level.",
        }
    }
    return response