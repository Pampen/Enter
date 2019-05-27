from utilities import handleInvalidDirection, goToLevel, handleInvalidInput, takeItem, handleDoorLock, returnToMainHall, openLevelFile

global shedCalled
global gateCalled
shedCalled = 0
gateCalled = 0 

def handleBeach(userInput, state):
    if userInput == 'GO WEST':
        if "oilLamp" in state["inventory"]:
            return goToLevel(state, "SHED_FRONT_DOOR", userInput) and handleNewShedFrontDoorDesc(state, userInput)
        else:
            return goToLevel(state, "SHED_FRONT_DOOR", userInput)
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'GATE', userInput)
    elif userInput == 'GO SOUTH':
        return handleOcean(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH_EAST_SIDE", userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleGate(userInput, state):
    global gateCalled
    if userInput == "USE BRONZE KEY" or userInput == 'USE KEY' and "bronzeKey" in state["inventory"]:
        gateCalled = gateCalled + 1
        return goToLevel(state, 'LIGHTHOUSE_OUTSIDE', userInput)
    elif userInput == "GO NORTH":
        if "bronzeKey" in state["inventory"] and gateCalled >= 1:
            return goToLevel(state, "LIGHTHOUSE_OUTSIDE", userInput) and handleNewGateDesc(state)
        else:
            return handleDoorLock(state, "GATE", userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH", userInput) and handleNewBeachDesc(state, userInput)
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseOutside(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE', userInput)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "GATE", userInput)
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouse(userInput, state):
    if userInput == 'GO WEST' or userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "LIGHTHOUSE_OUTSIDE", userInput)
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        return goToLevel(state, "LIGHTHOUSE_TOP_FLOOR", userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseTopFloor(userInput, state):
    global gateCalled
    global shedCalled
    if userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "TAKE STAIRS" or userInput == 'USE STAIRS':
        return goToLevel(state, "LIGHTHOUSE", userInput)
    elif userInput == 'TAKE GREEN KEY' or userInput == 'TAKE KEY':
        gateCalled = gateCalled - 1
        shedCalled = shedCalled - 1
        return state['inventory'].pop('oilLamp') and state['inventory'].pop('bronzeKey') and state['inventory'].pop('tornPages') and returnToMainHall(state, 'greenKey', 'MAIN_HALL_RETURN_FROM_GREEN')
    else:
        return handleInvalidInput(userInput, state)

def handleShedFrontDoor(userInput, state):
    if userInput == 'GO WEST':
        if "oilLamp" in state["inventory"]:
            return goToLevel(state, "SHED", userInput) and handleNewShedDesc(state, userInput)
        else:
            return goToLevel(state, "SHED", userInput)
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH", userInput) and handleNewBeachDesc(state, userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    global shedCalled
    if userInput == 'GO WEST' or userInput == "GO SOUTH" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if "oilLamp" in state["inventory"] and shedCalled < 1:
            return handleBasement(state)
        elif "oilLamp" not in state["inventory"]:
            return handleNoOillamp(state)
        elif "bronzeKey" not in state["inventory"] and shedCalled >= 1:
            return goToLevel(state, "CELLAR", userInput) and handleNewStairsNoLamp(state)
        elif "bronzeKey" in state["inventory"] and shedCalled >= 1:
            return goToLevel(state, "CELLAR", userInput) and handleNewStairsDesc(state)
        else:
            goToLevel(state, "SHED", userInput)
    elif userInput == "TAKE OIL LAMP" or userInput == "TAKE LAMP" or userInput == "TAKE OLD FASHIONED OIL LAMP" or userInput == "TAKE OLD-FASHIONED OIL LAMP":
        return takeItem(state, 'oilLamp')
    elif userInput == "THROW OIL LAMP" and "oilLamp" in state["inventory"]:
        return handleNewShedDescOilLamp(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "SHED_FRONT_DOOR", userInput) and handleNewShedFrontDoorDesc(state, userInput)
    elif userInput == "TAKE FISHERMAN GEAR" or userInput == "TAKE OLD FISHERMAN GEAR":
        return handleInvalidGear(state)
    elif userInput == "USE PADLOCK" or userInput == "USE LOCK":
        if shedCalled >= 1:
            return handlePadlockUsed(state)
        else:
            shedCalled = shedCalled + 1
            return handlePadlock(state)
    elif userInput == "JOYFUL" and shedCalled >= 1:
        if "tornPages" in state["inventory"] and "oilLamp" in state["inventory"]:
            return goToLevelShedPuzzle(state, "CELLAR", userInput)
        else:
            return handleDoorLock(state, "SHED", userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleBeachEastSide(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH', userInput) and handleNewBeachDesc(state, userInput)
    elif userInput == 'GO EAST':
        if "tornPages" in state["inventory"]:
            return goToLevel(state, 'SHIPWRECK', userInput) and handleNewShipwreckDesc(state, userInput)
        else:
            return goToLevel(state, "SHIPWRECK", userInput)
    elif userInput == 'GO SOUTH' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH_EAST_SIDE', userInput)
    elif userInput == "GO EAST":
        if "tornPages" in state["inventory"]:
            return goToLevel(state, 'CAPTAINS_CABIN', userInput) and handleNewCabinDesc(state, userInput)
        else:
            return goToLevel(state, "CAPTAINS_CABIN", userInput)
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCaptainsCabin(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHIPWRECK', userInput) and handleNewShipwreckDesc(state, userInput)
    elif userInput == "GO EAST" or userInput == "GO NORTH" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == "TAKE TORN PAGES" or userInput == "TAKE PAGES":
        return takeItem(state, "tornPages")
    elif userInput == "TAKE FAMILY PHOTOGRAPH" or userInput == "TAKE PHOTOGRAPH" or userInput == "TAKE FAMILY PHOTO" or userInput == "TAKE FRAMED FAMILY PHOTOGRAPH":
        return handleInvalidPhoto(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCellar(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO NORTH" or userInput == "GO EAST" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if "oilLamp" in state["inventory"]:
            return goToLevel(state, 'SHED', userInput) and handleNewShedDesc(state, userInput)
        else:
            return goToLevel(state, "SHED", userInput)
    elif userInput == "USE OIL LAMP" and "oilLamp" in state["inventory"]:
        return handleNewCellarDesc(state)
    elif userInput == "TAKE BRONZE KEY" or userInput == "TAKE KEY":
        return takeItem(state, 'bronzeKey')
    else:
        return handleInvalidInput(userInput, state)

def handleOcean(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The sea is behind you, going south isn't going to work."
        }
    }
    return response  

def handleBasement(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "While trying to make your way downstairs, a door is blocking your way from moving forward. The door appears to be locked with a bunch of chains put onto it, there's a padlock that you can use."
        }
    }
    return response

def handleNewCellarDesc(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelDescription': "The Room lights up making it easier to see your surroundings. There's a table in front of you with a bronze key on it."
        }
    }
    return response

def handleNewShedDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Shed",
            'levelDescription': "You stand inside the shed. It's filled with what looks to be a bunch of old fisherman gear. There are stairs leading down to the basement.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }       
    }
    return response

def handleNewBeachDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Beach",
            'levelDescription': "You find yourself on the beach. There's a Lighthouse right in front of you up the hill, a shipwreck by the coast and what looks to be a shed to your left by the seaside.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    }
    return response

def handleNewCabinDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Captains Cabin",
            'levelDescription': "You are currently inside the captains cabin.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    }
    return response

def handleNewShedFrontDoorDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Shed Frontdoor",
            'levelDescription': "You stand outside the shed.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }       
    }
    return response

def handleNewShipwreckDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Shipwreck",
            'levelDescription': "You find yourself on the old rustic shipwreck.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    }
    return response

def handleNewBeachEastSide(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Beach East side",
            'levelDescription': "You're standing on the east side of the beach.",
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    }
    return response

def handleInvalidPhoto(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The Family photograph is stuck on the wall..."
        }
    }
    return response

def inspectPhoto(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "It's a family photo of the people who used to live here..."
        }
    }
    return response

def handleNewShedDescOilLamp(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "Throwing the oil lamp would result in a fire..."
        }
    }
    return response

def handleInvalidGear(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "Doesn't seem worth taking the fisherman gear..."
        }
    }
    return response

def handleNoOillamp(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "It's seems to be very dark down there, you need something to light up your surrounding..."
        }
    }
    return response

def handlePadlock(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "You are holding the padlock in your hand. It requires you to enter six letters in a certain order. What do you want to input?"
        }
    }
    return response

def handleNewStairsDesc(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Cellar",
            'levelDescription': "You find yourself in the basement of the shed. There seems to be nothing worthwhile to do here...",
            'levelChatboxText': 'The door has already been unlocked from before...'
        }       
    }
    return response

def handleNewStairsNoLamp(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Cellar",
            'levelDescription': "You find yourself in the basement of the shed. There seems to be nothing but bunch of old junk. Your vision is very limited due to the darkness, maybe you have something that can help you light up the room",
            'levelChatboxText': 'The door has already been unlocked from before...'
        }       
    }
    return response

def handleNewGateDesc(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Lighthouse Outside",
            'levelDescription': "You stand outside the lighthouse",
            'levelChatboxText': 'The door has already been unlocked from before...'
        }       
    }
    return response

def handlePadlockUsed(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'The padlock has already been used...'
        }       
    }
    return response

def goToLevelShedPuzzle(state, currentLevel, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": '',
            'levelChatboxText': "You managed to open the door and went further into the cellar..."
        }
    } 
    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response