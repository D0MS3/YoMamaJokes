import json
from argparse import ArgumentParser
import src.JokeFinder as JF
import tkinter as TK

YO_MAMA_JOKES_PATH = 'yo_mama_jokes.json'

def printJoke():

    parser = ArgumentParser(prog='Yo Mama Jokes', description='Prints random "Yo Mama" jokes!', epilog='Need help?')
    parser.add_argument(nargs='*', dest="selection", type=str, help="Select joke types (keys in json)")
    args = parser.parse_args()

          # Open joke source .json file
    dict_jokes = JF.openFile(YO_MAMA_JOKES_PATH)

    # Find all jokes for selected types
    selection = JF.checkJokeTypes(dict_jokes, args.selection)

    # Print random joke in terminal
    print(JF.getRandomJoke(dict_jokes, selection))

    myLabel.config(text = JF.getRandomJoke(dict_jokes, selection))

# setup UI
root = TK.Tk(screenName="Yo Mama Jokes", baseName="Yo Mama")
root.geometry("400x400")
root.title('"Yo Mama" Jokes Generator')
myButton = TK.Button(root, text="Gimme a joke!",command=printJoke)
myButton.pack()
myLabel =TK.Label(root, text="")
myLabel.pack()

def main():

# main loop for UI
    root.mainloop()

if __name__ == '__main__':
    main()