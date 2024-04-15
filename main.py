import src.JokeFinder as JF
import src.Jokes as JKS
import tkinter as TK


def jokeBtn_pressed():
 
    # Get all selected joke types
    selected_joke_types=[]
    for checkbutton, joke_type in zip(CheckbuttonsValues, joke_types):
        if checkbutton.get()==1:
            selected_joke_types.append(joke_type)

    # Show a random joke
        jokeLbl.config(text = JF.getRandomJoke(dict_jokes, selected_joke_types))

# Setup UI
# Entry Widget
root = TK.Tk(screenName="Yo Mama Jokes", baseName="Yo Mama")
root.geometry("600x500")
root.title('"Yo Mama" Jokes Generator')
# Button to generate joke
jokeBtn = TK.Button(root, text="Gimme a joke!",command=jokeBtn_pressed)
jokeBtn.pack()
# Label to print the joke
jokeLbl =TK.Label(root, text="")
jokeLbl.pack()

#get jokes from Jokes.py file
dict_jokes=JKS.yo_mama_jokes

# create checkbutton for every joke type
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