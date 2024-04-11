
import random
import json

def __init__(self): pass

def openDict(path: str) -> dict:
    try:
        with open(path) as json_file:
            return json.load(json_file)
    except:
        print("No source file for jokes found!")
        exit()
    

def getRandomJoke(dict_jokes: dict, types: list[str]) -> str:
    # extract all relevant jokes
    jokes_selection = []
    for ele in types:
        if (ele in dict_jokes):
            jokes_selection += dict_jokes[ele]

    # return a random joke
    if len(jokes_selection)!=0:
        return random.choice(jokes_selection)
    else:
        return "No jokes found!"

