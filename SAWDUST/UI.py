from Wordclouds import plotWordCloud
from tkinter import *
from tkinter import ttk

twitter_blue = "#1DA1F2"

class EntryWindow():
    
    def __init__(self):
        self.window = Tk()
        
        self.window.title("S.A.W.D.U.S.T. Cloud")
        self.window.geometry("300x300")
        self.window.config(background = twitter_blue)


        title1 = Label(self.window, text = 'S.A.W.D.U.S.T. Cloud', font = ("Arial", 18, "bold"), fg = "white", bg = twitter_blue)
        title1.pack()
        title2 = Label(self.window, text = '(Sentiment Analysis of Word Distribution\nUsing Searches of Twitter)', font = ("Arial", 12), fg = "white", bg = twitter_blue)
        title2.pack()
        
        separatorLine = ttk.Separator(self.window, orient = "horizontal")
        separatorLine.pack(fill="x")

        instruction1 = Label(self.window, text = 'Enter a word to analyse:', font = ("Arial", 12, "bold"), fg = "white", bg = twitter_blue)
        instruction1.place(x = 0, y = 80)
        
        self.text = Entry(self.window)
        self.text.place(x = 85, y = 105)
        
        instruction2 = Label(self.window, text = "Choose a colour scheme:", font = ("Arial", 12, "bold"), fg = "white", bg = twitter_blue)
        instruction2.place(x = 0, y = 125)

        #scheme1Image = PhotoImage(file = "./colourscheme1.GIF")
        #scheme1Label = Label(self.window, image = scheme1Image)
        #scheme1Label.place(x = 0, y = 150)
    
        self.generateButton = Button(self.window, text = "Generate Word Cloud!", command = self.attemptGeneration)
        self.generateButton.place(x = 0, y = 150)
    
    def getInputText(self):
        return self.text.get()
    
    def attemptGeneration(self):
        word = self.getInputText()
        if word == "":
            print("temp error message - no text")
        else:
            plotWorldCloud(word)
    
    def run(self):
        self.window.mainloop()

#btn = Button(windowOne, text='Push Me')
#btn.bind('<Button-1>', MyButtonClicked)

window1 = EntryWindow()
window1.run()