import json
from argparse import ArgumentParser
from src.JokeFinder import JokeFinder

YO_MAMA_PATH = 'yo_mama_jokes.json'

def main():

    # Open joke source .json file
    try:
        with open(YO_MAMA_PATH) as json_file:
            dict_jokes = json.load(json_file)
    except:
        print("Source file for jokes not found!")
        exit()

    parser = ArgumentParser(prog='Yo Mama Jokes', description='Prints random "Yo Mama" jokes!', epilog='Need help?')
    parser.add_argument(nargs='*', dest="selection", type=str, help="Select joke types (keys in json)")
    args = parser.parse_args()

    # Find all jokes for selected types
    selection = JokeFinder.checkJokeTypes(dict_jokes, args.selection)

    # Print random joke in terminal
    print(JokeFinder.getRandomJoke(dict_jokes , selection))

if __name__ == '__main__':
    main()