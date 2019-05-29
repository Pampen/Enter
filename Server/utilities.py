import json
import os

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
                response['pageChanges']['levelChatboxText'] = 'You cannot ' + userInput + '. ' + lockDescrption[descriptionName]
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
                'levelChatboxText': 'You picked up ' + item["itemName"].upper() + '. You are now back at the Main Hall. The items you no longer need were left behind. There is something new to explore.'
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
    cwd = os.getcwd()
    filePath = cwd + '/Server/tools/levelDescription.json'
    
    with open(filePath, "r") as getData:
        data = json.loads(getData.read())
        return data
        
def openItemFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/tools/inventory.json'
    
    with open(filePath, "r") as getData:
        data = json.loads(getData.read())
        return data

def openUseDescriptionFile():
    cwd = os.getcwd()
    filePath = cwd + '/Server/tools/invalidUseDescription.json'
    
    with open(filePath, 'r') as getData:
        data =json.loads(getData.read())
        return data