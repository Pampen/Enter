from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock

def handleCribRoom(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'TOY_CAR_ROOM', userInput)
    elif userInput == 'GO EAST':
        if 'nurseryRhyme' in state ['inventory']:
            return goToLevel(state, 'MESSY_ROOM', userInput) and messyRoomWithRhymePickedUp(state)
        else:
            return goToLevel(state, 'MESSY_ROOM', userInput)
        return handleInvalidDirection(state)
    elif userInput == "TAKE CRIB":
        return takeItem(state, 'crib')
    elif userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)
    
def handleToyCarRoom(userInput, state):
    if userInput == 'GO NORTH':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM', userInput) and babyRoomWithDollPickedUp(state)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        if 'crib' in state ['inventory']:
            return goToLevel(state, 'CRIB_ROOM', userInput) and cribRoomWithCribPickedUp(state)
        else:
            return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBabyRoom(userInput, state):
    if userInput == 'GO EAST':
        if len(state['pinkPuzzleItems']) != 0:
                return handleInvalidDirection(state)
        elif 'pinkKey' in state['inventory']:
            return goToLevel(state, "NURSING_ROOM", userInput) and studyRoomWithPinkKeyPickedUp(state)
        elif 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, "NURSING_ROOM", userInput) and nursingRoomWithPacifierPickedUp(state)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
            if len(state['pinkPuzzleItems']) != 0:
                return handleInvalidDirection(state)
            else:
                return goToLevel(state, 'TOY_CAR_ROOM', userInput)
    elif userInput == "TAKE WORN DOLL" or userInput == "TAKE DOLL":
        return takeItem(state, 'wornDoll')
    elif 'USE' in userInput:
        puzzleList = state['pinkPuzzleItems']
        if len(puzzleList) == 0:
            items=[
                'crib', 'moldyPacifier', 'wornDoll', 'dirtyBlanket', 'nurseryRhyme'
            ]
            currentItems=state['inventory']
            for item in items:
                if item not in currentItems:
                    return handleDoorLock(state, 'BABY_ROOM', userInput)
            return pinkRoomPuzzle(state, userInput)
        else:
            return pinkRoomPuzzle(state, userInput)
    elif userInput == "TAKE PINK KEY" or userInput == "TAKE KEY":
        return takeItem(state, 'pinkKey')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNursingRoom(userInput, state):
    if userInput == 'GO WEST':
        if 'wornDoll' in state['inventory']:
            return goToLevel(state, 'BABY_ROOM', userInput) and babyRoomWithDollPickedUp(state)
        else:
            return goToLevel(state, 'BABY_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        if 'dirtyBlanket' in state ['inventory']:
            return goToLevel(state, 'STUDY_ROOM', userInput) and studyRoomWithBlanketPickedUp(state)
        else:
            return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == "TAKE MOLDY PACIFIER" or userInput == "TAKE PACIFIER":
        return takeItem(state, 'moldyPacifier')
    elif userInput == "GO EAST":
        if 'pinkKey' in state['inventory']:
            return goToLevel(state, 'BLUE_START', userInput)
        else:
            return finishPuzzleFirst(state)
    elif userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleStudyRoom(userInput, state):
    if userInput == 'GO NORTH':
        if 'moldyPacifier' in state ['inventory']:
            return goToLevel(state, 'NURSING_ROOM', userInput) and nursingRoomWithPacifierPickedUp(state)
        else:
            return goToLevel(state, 'NURSING_ROOM', userInput)
    elif userInput == 'GO SOUTH':
        if 'nurseryRhyme' in state ['inventory']:
            return goToLevel(state, 'MESSY_ROOM', userInput) and messyRoomWithRhymePickedUp(state)
        else:
            return goToLevel(state, 'MESSY_ROOM', userInput)
    elif userInput == "TAKE DIRTY BLANKET" or userInput == "TAKE BLANKET":
        return takeItem(state, 'dirtyBlanket')
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleMessyRoom(userInput, state):
    if userInput == 'GO NORTH':
        if 'dirtyBlanket' in state ['inventory']:
            return goToLevel(state, 'STUDY_ROOM', userInput) and studyRoomWithBlanketPickedUp(state)
        else:
            return goToLevel(state, 'STUDY_ROOM', userInput)
    elif userInput == 'GO WEST':
        if 'crib' in state ['inventory']:
            return goToLevel(state, 'CRIB_ROOM', userInput) and cribRoomWithCribPickedUp(state)
        else:
            return goToLevel(state, 'CRIB_ROOM', userInput)
    elif userInput == "TAKE NURSERY RHYME" or userInput == "TAKE RHYME" or userInput == "TAKE NOTEBOOK":
        return takeItem(state, 'nurseryRhyme')
    elif userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def pinkRoomPuzzle(state, userInput):
    print(state)
    newState = state
    puzzleList = state['pinkPuzzleItems']
    print(puzzleList)
    print(state)
    if 'CRIB' in userInput or 'DOLL' in userInput or 'WORN DOLL' or 'BLANKET' in userInput or 'DIRTY BLANKET' in userInput or 'PACIFIER' in userInput or 'MOLDY PACIFIER' in userInput or 'RHYME' in userInput or 'NURSERY RHYME' in userInput:
        if userInput == "USE CRIB" and "crib" not in puzzleList:
            puzzleList.append("crib")
            newState['pinkPuzzelItems'] = puzzleList
            newState['inventory'].pop('crib')
            response = {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "You use the crib",
                    "levelDescription": "The crib looks beautiful, almost surreal... but it also looks empty."
                }
            }
            return response
        elif userInput == "USE WORN DOLL" or userInput == "USE DOLL" and "crib" in puzzleList and "doll" not in puzzleList:
            puzzleList.append("doll")
            newState['pinkPuzzelItems'] = puzzleList
            newState['inventory'].pop('wornDoll')
            response = {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "You use the doll",
                    "levelDescription": "The doll almost looks like it is shivering in cold..."
                }
            }
            return response
        elif userInput == "USE DIRTY BLANKET" or userInput == "USE BLANKET" and "doll" in puzzleList and "blanket" not in puzzleList:
            puzzleList.append("blanket")
            newState['pinkPuzzelItems'] = puzzleList
            newState['inventory'].pop('dirtyBlanket')
            response = {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "You use the blanket",
                    "levelDescription": "The doll looks unhappy. Is it... pucking it's lips?"
                }
            }
            return response
        elif userInput == "USE MOLDY PACIFIER" or userInput == "USE PACIFIER" and "blanket" in puzzleList and "pacifier" not in puzzleList:
            puzzleList.append("pacifier")
            newState['pinkPuzzelItems'] = puzzleList
            newState['inventory'].pop('moldyPacifier')
            response = {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "You use the pacifier",
                    "levelDescription": "Do you remember the nursery rhyme? It feels like you should use it..."
                }
            }
            return response
        elif userInput == "USE NURSERY RHYME" or userInput == "USE RHYME" and "pacifier" in puzzleList:
            puzzleList.clear() 
            newState['pinkPuzzelItems'] = puzzleList
            newState['inventory'].pop('nurseryRhyme')
            response = {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "As you begin to sing the rhyme a pink key appears in the crib",
                    "levelDescription": "A pink key appears in the crib. You also hear a blue door swing open in the room to your right, better check it out"
                }
            }
            return response
        else: 
            response = {
                'state': newState,
                'pageChanges': {
                    "levelChatboxText": "That's not the right order, try using another item you picked up in this level"
                }
            }
            return response
    else:
        return {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "That doen't seems to be the right thing to do..."
                }
            }

def finishPuzzleFirst(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelChatboxText": "Before you move on you need to solve the puzzle for this level.",
        }
    }
    return response

def cribRoomWithCribPickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Crib Room",
            "levelDescription": "Absolutely nothing in here... The emptiness is too much. Best to move on...",
        }
    }
    return response

def messyRoomWithRhymePickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Messy Room",
            "levelDescription": "This room is a mess. Broken bottles and thrashed books. A nursery rhyme is scribbled on the walls..."
        }
    }
    return response

def babyRoomWithDollPickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Baby Room",
            "levelDescription": "This room is filled with baby things. The walls have painted unicorns, and the shelves are filled with toys. The only thing missing is the crib...",
        }
    }
    return response

def nursingRoomWithPacifierPickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Nursing Room",
            "levelDescription": "A nursing room... and a changing table. A funky smell envelopes you as you enter. The smell is sweet, but somewhat earthy... strange.",
        }
    }
    return response

def studyRoomWithBlanketPickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Study Room",
            "levelDescription": "A study. A nice, comfy chair, rows upon rows of books on the shelves and a decanter filled with a golden liquid  standing besides a used glass... Dust everywhere.",
        }
    }
    return response

def studyRoomWithPinkKeyPickedUp(state):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": "Study Room",
            "levelDescription": "To your right is a open big blue door, you should through it and continue on your quest.",
        }
    }
    return response