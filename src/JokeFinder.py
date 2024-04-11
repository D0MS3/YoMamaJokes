
import random
import json

def __init__(self): pass

def openFile(path: str) -> dict:
    try:
        with open(path) as json_file:
            return json.load(json_file)
    except:
        print("No source file for jokes found!")
        exit()

def checkJokeTypes(jokeDict: dict, types: list[str]) -> list[str]:   

    # extract relevant joke types from user input
    # no args: then choose all keys, non existing types in args are ignored     
    if len(types) == 0:
        types = list(jokeDict.keys())
        return types
    # no valid args found
    elif len([value for value in types if value in list(jokeDict.keys())])==0:
        print("No valid joke type found!")
        exit()
    else:
        return types
    

def getRandomJoke(dict_jokes: dict, types: list[str]) -> str:
        # get all relevant jokes
    jokes_selection = []
    for ele in types:
        if (ele in dict_jokes):
            jokes_selection += dict_jokes[ele]

    # print a random joke
    if len(jokes_selection)!=0:
        return random.choice(jokes_selection)
    else:
        print("No jokes found!")

