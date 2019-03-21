from flask import Flask, request, Response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def getMessage():
    userInput = request.get_json()
    message = userInput.get('message')
    response = getResponse(message)
    print(message)
    return jsonify(response) #Return value of var. 'response' to JavaScript
    '''
        Vi sparar ner ett värde i response från
        funktionen getResponse. Saker som skickas
        med kan ni hitta i konsolen genom att:
        1) Kör servern. Öppna en terminal, gå till
        mappen som servern (vår python) ligger i. Skriv:
                    FLASK_APP=game.py FLASK_DEBUG = 1 flask run
        i terminalen.
        2)Kör react. Skriv 'npm start' i terminalen. (körs på localhost:3000)
        3) Klicka på knappen 'clickme'.
        4) Öppna konsolen, välj tabben "network".
        5) Under network borde ni se två länkar, "localhost". Den första länken som kommer
        visar vad servern har skickat. Klicka på den andra "localhost" och välj "response".
        Här borde det som skickats med komma upp om allt fungerar som det ska.
    '''

def getResponse(userInput):
    #TODO Change dict. to corresponding functions, modules. 
    return {
        "newGameState": {
            "levelTitle": None,
            "levelDescription": 'This is a very so much like a description.',
            "levelChatboxText": 'This appears in the chatbox.'
        },
        "inventory": {
            "firstObject": True,
            "secondObject": False
        }
    }