from saveLevelAndWrongUserInput import handleInvalidDirection, goToLevel, handleInvalidInput, takeItem

def handleBeach(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'OUTSIDE_SHED')
    elif userInput == 'GO NORTH':
        return goToLevel(state, 'GATE')
    elif userInput == 'GO SOUTH':
        return handleOcean(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "OUTSIDE_SHIPWRECK")
    else:
        return handleInvalidInput(userInput, state)

def handleGate(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE_OUTSIDE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "BEACH")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseOutside(userInput, state):
    if userInput == 'GO NORTH':
        return goToLevel(state, 'LIGHTHOUSE')
    elif userInput == "GO SOUTH":
        return goToLevel(state, "GATE")
    elif userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouse(userInput, state):
    if userInput == 'GO WEST' or userInput == 'GO EAST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    elif userInput == "GO SOUTH":
        return goToLevel(state, "LIGHTHOUSE_OUTSIDE")
    elif userInput == 'TAKE STAIRS':
        return goToLevel(state, "LIGHTHOUSE_TOP")
    else:
        return handleInvalidInput(userInput, state)

def handleLighthouseTopFloor(userInput, state):
    if userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    elif userInput == "TAKE STAIRS":
        return goToLevel(state, "LIGHTHOUSE")
    elif userInput == "TAKE GREEN KEY" or userInput == "TAKE KEY":
        return takeItem(state, "greenKey")
    else:
        return handleInvalidInput(userInput, state)

def handleOutsideShed(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHED')
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    elif userInput == 'GO EAST':
        return goToLevel(state, "BEACH")
    else:
        return handleInvalidInput(userInput, state)

def handleShed(userInput, state):
    if userInput == 'GO WEST' or userInput == "GO SOUTH" or userInput == "GO NORTH":
        return handleInvalidDirection(state)
    elif userInput == 'TAKE STAIRS':
        #return handleBasement(state)
        return goToLevel(state, "CELLAR")
    elif userInput == 'GO EAST':
        return goToLevel(state, "OUTSIDE_SHED")
    else:
        return handleInvalidInput(userInput, state)
  
def handleOutsideShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'BEACH')
    elif userInput == 'GO EAST':
        return goToLevel(state, 'SHIPWRECK')
    elif userInput == 'GO SOUTH' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleShipwreck(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHIPWRECK_OUTSIDE')
    elif userInput == "GO EAST":
        return goToLevel(state, "CABIN")
    elif userInput == 'GO NORTH' or userInput == "GO SOUTH":
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleCabin(userInput, state):
    if userInput == 'GO WEST':
        return goToLevel(state, 'SHIPWRECK')
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
        return goToLevel(state, "SHED")
    elif userInput == "INSPECT GLIMMER":
        return handleGlimmer(state)
    elif userInput == "TAKE BRONZE KEY":
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
            'levelChatboxText': "While trying to make your way downstairs, a door is blocking your way from moving forward. The door appears to be locked with a bunch of chains put onto it, there's a padlock that requires you to enter 6 words in a certain order."
        }
    }
    return response

def handleGlimmer(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "While taking a closer look at the glimmer, you can see the reflection of a key that sits right besides a big cogwheel. You could probably grab it if you tried hard enough."
        }
    }
    return response  