import re
import random
import json



def analyse_json(data):
    json_string = json.loads(data)
    for k,v in json_string.items():
        print(k,v)
    return json_string



def reponse_bot(username, message):
    print('Bot')
    bonjour = r"salut.*|bonjour.*|coucou.*|cc.*|hi.*|hello.*"
    reponse_bonjour_bot = ["bonjour à toi", "hello", "salut"]
    reponse_bateau_bot = ["je ne suis pas trés évolué, la conversation va être un peu limité"," J'aime faire des crêpes! tu en veux?",
    "J'espère que j'ai pas le coronavirus, je suis fatigué!", "Un peu d'humour: https://www.youtube.com/watch?v=QuGcoOJKXT8 "]
    message = message.lower()
    response = ''
    if (re.search("au revoir", message)):
        response = f"bye camarade, je t'aimais bien {username}"
    elif (re.fullmatch(bonjour, message)):
        response = f"{random.choice(reponse_bonjour_bot)} {username}"
    else:
        response = random.choice(reponse_bateau_bot)
        
    return response