import WordClouds
from tkinter import *
from tkinter import ttk

twitter_blue = "#1DA1F2"
green = "#00FF00"
red = "#FF0000"
magenta = "#FF007F"

class EntryWindow():
    
    def __init__(self):
        self.window = Tk()
        
        self.window.title("S.A.W.D.U.S.T. Cloud")
        self.window.geometry("300x275")
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
        
        self.radio_var = IntVar()
        self.radio_var.set(1)
        radio1 = Radiobutton(self.window, bg = twitter_blue, text = "Standard", font = ("Arial", 12, "bold"), variable = self.radio_var,  value = 1)
        radio1.place(x = 25, y = 150)
        radio2 = Radiobutton(self.window, bg = twitter_blue, text = "Colourblind", font = ("Arial", 12, "bold"), variable = self.radio_var, value = 2)
        radio2.place(x = 25, y = 175)
        
        scheme1Positive = Label(self.window, text = "Positive", font = ("Helvetica", 12), fg = "black", bg = green)
        scheme1Positive.place(x = 155, y = 150)
        scheme1Negative = Label(self.window, text = "Negative", font = ("Helvetica", 12), fg = "black", bg = red)
        scheme1Negative.place(x = 225, y = 150)
        
        scheme2Positive = Label(self.window, text = "Positive", font = ("Helvetica", 12), fg = "black", bg = green)
        scheme2Positive.place(x = 155, y = 180)
        scheme2Negative = Label(self.window, text = "Negative", font = ("Helvetica", 12), fg = "black", bg = magenta)
        scheme2Negative.place(x = 225, y = 180)

        self.generateButton = Button(self.window, text = "Generate Word Cloud!", command = self.attemptGeneration)
        self.generateButton.place(x = 85, y = 215)
        
        self.errorLabel = Label(self.window, text = "", font = ("Arial", 12, "bold"), fg = red, bg = twitter_blue)
        self.errorLabel.place(x = 0, y = 245)
    
    def getInputText(self):
        return self.text.get()
    
    def updateErrorLabel(self, error):
        self.errorLabel.config(text = error)
    
    def attemptGeneration(self):
        word = self.getInputText()
        if word == "":
            self.updateErrorLabel("Error - no word has been entered")
        else:
            self.updateErrorLabel("") # resets error label
            Wordclouds.plotWordCloud(word, self.radio_var.get() == 1)
    
    def run(self):
        self.window.mainloop()

window = EntryWindow()
window.run()