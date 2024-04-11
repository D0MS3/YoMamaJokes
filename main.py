import src.JokeFinder as JF
import tkinter as TK

YO_MAMA_JOKES_PATH = 'yo_mama_jokes.json'

def button_pressed():
 
    # Get all selected joke types
    selected_joke_types=[]
    for checkbutton, joke_type in zip(CheckbuttonsValues, joke_types):
        if checkbutton.get()==1:
            selected_joke_types.append(joke_type)

    # Show a random joke
        myLabel.config(text = JF.getRandomJoke(dict_jokes, selected_joke_types))

# setup UI
root = TK.Tk(screenName="Yo Mama Jokes", baseName="Yo Mama")
root.geometry("600x500")
root.title('"Yo Mama" Jokes Generator')
myButton = TK.Button(root, text="Gimme a joke!",command=button_pressed)
myButton.pack()
myLabel =TK.Label(root, text="")
myLabel.pack()
myLabel2 =TK.Label(root, text="ugly")
myLabel2.pack()

#open joke json file to dictionary
dict_jokes = JF.openDict(YO_MAMA_JOKES_PATH)

#create checkbutton for every joke type
joke_types = list(dict_jokes.keys())
Checkbuttons=[]
CheckbuttonsValues=[]
for i in joke_types:
    var=TK.IntVar()
    newCheckbutton=TK.Checkbutton(root, text=i, variable=var)
    CheckbuttonsValues.append(var)
    Checkbuttons.append(newCheckbutton)
    newCheckbutton.pack()

# main loop for UI
root.mainloop()