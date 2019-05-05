import json
import os

def redPuzzle(state, userInput): 
    newState = state
    objectList = state["isBurned"]
    if len(objectList) == 0 and userInput == 'THROW CANVAS':
        objectList.append('canvas')
        print(objectList)
        newState['isBurned'] = objectList
        return {
            'state': newState, 
            'pageChanges': {
                'levelChatboxText': "You burn the canvas"
            }
        }
    elif 'canvas' in state['inventory'] and 'canvas' in state['isBurned'] and userInput == 'THROW PHOTOGRAPH':
        objectList.append('photograph')
        newState['isBurned'] = objectList
        return {
        'state': newState, 
        'pageChanges': {
            'levelChatboxText': "You burn the photograph."
        }
    }
    elif 'photograph' in state['inventory'] and 'photograph' in state['isBurned'] and userInput == 'THROW CAR KEYS':
        objectList.append('carKeys')
        newState['isBurned'] = objectList
        return {
        'state': newState, 
        'pageChanges': {
            'levelChatboxText': "You burn car keys. The fire slowly dies and what is left of the fire is ashes and a red key."
        }
    }
    else:
        newState['isBurned'] = []
        return {
            'state': newState,
            'pageChanges': {
                'levelChatboxText': 'It is not in the right order, you might want to read the description for each item for this level to solve this puzzle...'
            }
        }

def goToLevel(state, currentLevel, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": '',
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    } 
    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def checkTorchItem(state, currentLevel, userInput):
    if "torch" in state['inventory']:
        if "rustyKey" not in state['inventory']:
            return torchBlueDescription(state, currentLevel, userInput)
        elif state['inventory']['rustyKey']['itemUse'] == False:
            return falseKeyDescription(state, currentLevel, userInput)
        elif state['inventory']['rustyKey']['itemUse'] == True:
            return trueKeyDescription(state, currentLevel, userInput)
    elif currentLevel != None:
        return goToLevel(state, currentLevel, userInput)
        
def torchBlueDescription(state, currentLevel, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": '',
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    } 
    data = openTorchFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def falseKeyDescription(state, currentLevel, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": '',
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    } 
    data = openFalseKeyFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def trueKeyDescription(state, currentLevel, userInput):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            'levelChatboxText': 'YOU ' + userInput.upper() + '.'
        }
    } 
    data = openTrueKeyFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def takeItem(state, currentItem):
    if currentItem in state['inventory']:
        response = {
            'state': state, 
            'pageChanges': {
                    'levelChatboxText': 'You already seem to be carrying ' + currentItem.upper() + '.'
            }
        }
        return response
    else:
        itemData = openItemFile()
        newState = state
        item = itemData[currentItem]
        newState['inventory'][currentItem] = item
        response = {
            'state': newState, 
            'pageChanges': {
                    'levelChatboxText': 'You picked up ' + item["itemName"].upper() + '.'
            }
        }
        return response
    
def inspectItem(state, userInput):
    itemData = openItemFile()
    for item in itemData:
        print(item)
        if itemData[item]['itemName'].upper() in userInput:
            print(itemData[item]['itemName'])
            if item in state['inventory']:
                itemDescription = itemData[item]['itemDescription']
                response = {
                    'state': state, 
                    'pageChanges': {
                            'levelChatboxText': itemDescription
                    }
                }
                return response
    return {
            'state': state, 
            'pageChanges': {
                    'levelChatboxText': "You do not seem to be carrying that."
    }
}

def handlePersistantItems(state, currentItem, currentLevel):
    if currentItem in state['usedItems']:
        response = {
            'state': state, 
            'pageChanges': {
                    'levelChatboxText': "You've already used the " + currentItem.upper() + "."
            }
        }
        return response
    else: 
        newState = state
        newState['usedItems'] = currentItem
        response = {
        'state': newState, 
        'pageChanges': {
                'levelChatboxText': 'You used the ' + currentItem.upper() + '.'
            }
        }
        data = openLevelFile()
        for level in data:
            if level["level"] == currentLevel:
                response['pageChanges']['levelTitle'] = level['levelTitle']
                response['pageChanges']['levelDescription'] = level['levelDescription']
                response['state']['level'] = level['level']
        return response

def handleInvalidDirection(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot go that way.'
        }
    }
    return response 

def handleInvalidInput(userInput, state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot ' + userInput + '.'
        }
    }
    return response

def handleDoorLock(state, currentLevel, userInput):
    response = {
                'state': state,
                'pageChanges': {
                    'levelChatboxText': ''
                    }
                }
    data = openUseDescriptionFile()
    for lockDescrption in data:
        for descriptionName in lockDescrption.keys():
            if descriptionName == currentLevel:
                response['pageChanges']['levelChatboxText'] = ('You cannot ' + userInput + '. ' + lockDescrption[descriptionName])
                return response

def handleUseItemBlueRoom(state, currentLevel):
    response = {
        'state': state,
        'pageChanges': {
            "levelChatboxText": ''
        }
    } 
    data = openTrueKeyFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelChatboxText'] = level['levelDescription']
            response['state']['level'] = level['level']
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

def returnToMainHall(state, currentItem, currentLevel):
    print(currentItem)
    itemData = openItemFile()
    item = itemData[currentItem]
    newState = state
    newState['inventory'][currentItem] = item
    response = {
        'state': newState, 
        'pageChanges': {
                'levelChatboxText': 'You picked up ' + item["itemName"].upper() + '. You are now back at the Main Hall'
        }
    }

    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def openLevelFile():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    filePath = cwd + '/Server/tutorial.json'
    
    with open(filePath, 'r') as getData:
        data = json.loads(getData.read())
        return data
        
def openItemFile():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    filePath = cwd + '/Server/inventory.json'
    
    with open(filePath, 'r') as getData:
        data = json.loads(getData.read())
        return data

def openTorchFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/blueTorchDescription.json'
    
    with open(filePath, 'r') as getData:
        data =json.loads(getData.read())
        return data

def openFalseKeyFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/blueFalseKeyDescription.json'
    
    with open(filePath, 'r') as getData:
        data =json.loads(getData.read())
        return data

def openTrueKeyFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/blueTrueKeyDescription.json'
    
    with open(filePath, 'r') as getData:
        data =json.loads(getData.read())
        return data

def openUseDescriptionFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/invalidUseDescription.json'
    
    with open(filePath, 'r') as getData:
        data =json.loads(getData.read())
        return data