import json
import os

def goToLevel(state, currentLevel):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": ''
        }
    }
    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def pickUpItem(state, currentItem):
    print(currentItem)
    response = {
        'state': state, 
        'pageChanges': {
                "itemName": '',
                "itemDescription": '',
        }
    }

    itemData = openItemFile()
    for item in itemData:
        if item["itemName"] == currentItem:
            response['pageChanges']['itemName'] = item['itemName']
            response['pageChanges']['itemDescription'] = item['itemDescription']
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

def handleInvalidPickUp(userInput, state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot pick up ' + userInput + '.'
        }
    }
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