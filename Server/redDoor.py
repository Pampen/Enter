from saveLevelAndWrongUserInput import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock

def handleLivingRoom(userInput, state):
    if userInput == 'GO SOUTH':
        return goToLevel(state, 'MAIN_HALL', userInput)
    elif userInput == 'TAKE RED KEY':
        return takeItem(state, 'redKey')
    elif userInput == 'GO EAST':
        if 'photograph' in state['inventory']: 
            return goToLevel(state, 'KITCHEN', userInput) and handleNewKitchenDesc(state, userInput)
        else:
            return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'GO WEST':
        if 'carKeys' in state['inventory']: 
            return goToLevel(state, 'HALL', userInput) and handleNewHallDesc(state, userInput)
        else:
            return goToLevel(state, 'HALL', userInput)
    elif userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomDesc(state, userInput)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE PHOTOGRAPH':
        return takeItem(state, 'photograph') 
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'ladder' in state['inventory']: 
            return goToLevel(state, 'BASEMENT', userInput) and handleNewBasementDesc(state, userInput)
        else:
            return goToLevel(state, 'BASEMENT', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'photograph' in state['inventory']: 
            return goToLevel(state, 'KITCHEN', userInput) and handleNewKitchenDesc(state, userInput)
        else:
            return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'TAKE LADDER':
        return takeItem(state, 'ladder')
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomDesc(state, userInput)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE CAR KEYS':
        return takeItem(state, 'carKeys')
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'UPPER_FLOOR', userInput) and handleFireLoudDesc(state, userInput)
        else:
            return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'carKeys' in state['inventory']: 
            return goToLevel(state, 'HALL', userInput) and handleNewHallDesc(state, userInput)
        else:
            return goToLevel(state, 'HALL', userInput)
    elif userInput == 'USE GREY KEY' and "greyKey" in state["inventory"]:
        if 'canvas' in state['inventory']: 
            return goToLevel(state, 'BEDROOM', userInput) and handleNewBedroomDesc(state, userInput)
        else:
            return goToLevel(state, 'BEDROOM', userInput)
    elif userInput == 'GO WEST':
        return handleDoorLock(state, 'UPPER_FLOOR_W', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        if 'greyKey' in state['inventory']: 
            return goToLevel(state, 'ATTIC', userInput) and handleNewAtticDesc(state, userInput)
        else:
            return goToLevel(state, 'ATTIC', userInput)
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'UPPER_FLOOR_N', userInput)
    elif userInput == 'GO EAST' or  userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO SOUTH':
        return handleDoorLock(state, 'ATTIC', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE GREY KEY':
        return takeItem(state, 'greyKey')
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBedroom(userInput, state):
    if userInput == 'GO EAST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'UPPER_FLOOR', userInput) and handleFireLoudDesc(state, userInput)
        else:
            return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE CANVAS':
        return takeItem(state, 'canvas')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNewLivingRoomDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Living Room",
            'levelDescription': "With the canvas, car keys and the photograph in your possession, you can feel the heat getting stronger and more violent. There is a huge message painted in red all over the room. Three Objects, Three Memories. You should try to throw objects into the fire.",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewKitchenDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Kitchen",
            'levelDescription': "An old kitchen, but with some modern modifications. There are some plates and glasses in the sink that needs to be washed. By the looks of it, it seems that the person who lived here hasn't done her or his dishes for a while. The fridge is old, and it doesn't work anymore. There are some stairs leading down to the basement.",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewHallDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Hall",
            'levelDescription': "A small hall with a clothing rack on the side and a small red carpet with the letter 'A' on it. Why the letter 'A'? There are also some pictures and the wall, however, you can't seem to see persons' faces in the pictures for some reasons. Every face is blurry. Beneath the pictures is a small table with an empty bowl. There are some stairs leading up to the upper floor.",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewBasementDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Basement",
            'levelDescription': "It's cold in the basement. There is not so much down here, just some old furnitures and some boxes filled with old toys, pictures, watches and so on. Most of it seems to be covered by a red cloth to protect them from getting all dusty. There are some stairs leading up.",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewAtticDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Attic",
            'levelDescription': "The attic is very dark, but the sunbeams from the windows make it much easier to distinguish what hides behind the dark. There are some boxes with the label 'memories'.",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewBedroomDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Bedroom",
            'levelDescription': "It looks like a regular bedroom, the walls are red, a bookcase filled with obviously books, photos, a tiny leather boot and a box full of old watches. There is a big round window in the room which is painted black, but it doesn't block the sunlight which is kind of odd.",
            'levelChatbox': ' YOU ' + userInput.upper() + ".",
        }
    }
    return response

def handleFireLoudDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Upper Floor",
            'levelDescription': "You can hear a loud noise coming from the living room, it sounds like fire, but why is the fire so loud?",
            'levelChatbox': ' YOU ' + userInput.upper() + "."
        }
    }
    return response