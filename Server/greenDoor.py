from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput, takeItem, handleDoorLock, goToLevelShedPuzzle, returnToMainHall

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
    if userInput == "USE BRONZE KEY" and "bronzeKey" in state["inventory"]:
        return goToLevel(state, 'LIGHTHOUSE_OUTSIDE', userInput)
    elif userInput == "GO NORTH":
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
    elif userInput == 'TAKE STAIRS':
        return goToLevel(state, "LIGHTHOUSE_TOP_FLOOR", userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseTopFloor(userInput, state):
    if userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "TAKE STAIRS":
        return goToLevel(state, "LIGHTHOUSE", userInput)
    elif userInput == 'TAKE GREEN KEY' or userInput == 'TAKE KEY':
        return returnToMainHall(state, 'greenKey', 'MAIN_HALL')
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
        return goToLevel(state, "BEACH", userInput)
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO SOUTH" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    elif userInput == 'TAKE STAIRS':
        return handleBasement(state)
    elif userInput == "TAKE OIL LAMP" or userInput == "TAKE LAMP":
        return takeItem(state, 'oilLamp')
    elif userInput == 'GO EAST':
        return goToLevel(state, "SHED_FRONT_DOOR", userInput) and handleNewShedFrontDoorDesc(state, userInput)
    elif userInput == "JOYFUL":
        if "tornPages" in state["inventory"]:
            return goToLevelShedPuzzle(state, "CELLAR", userInput)
        else:
            return handleDoorLock(state, "SHED", userInput)
    else:
        return handleInvalidInput(userInput, state)
  
def handleBeachEastSide(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH', userInput) and handleNewBeachDesc(state, userInput)
    elif userInput == 'GO EAST':
        return goToLevel(state, 'SHIPWRECK', userInput)
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
        return goToLevel(state, 'SHIPWRECK', userInput)
    elif userInput == "GO EAST" or userInput == "GO NORTH" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == "TAKE TORN PAGES" or userInput == "TAKE PAGES":
        return takeItem(state, "tornPages")
    else:
        return handleInvalidInput(userInput, state)

def handleCellar(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO NORTH" or userInput == "GO EAST" or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'TAKE STAIRS':
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
            'levelChatboxText': "While trying to make your way downstairs, a door is blocking your way from moving forward. The door appears to be locked with a bunch of chains put onto it, there's a padlock that requires you to enter six words in a certain order."
        }
    }
    return response

def handleNewCellarDesc(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelDescription': "The Room lights up making it easier to see your surruondings. There's a table in front of you with a bronze key on it."
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
            'levelDescription': "You find yourself on the beach. There's a Lighthouse right infront of you up the hill, a shipwreck by the coast and what looks to be a shed to your left by the seaside.",
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