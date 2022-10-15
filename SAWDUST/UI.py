import Wordclouds
from tkinter import *
from tkinter import ttk

twitter_blue = "#1DA1F2"
green = "#00FF00"
red = "#FF0000"
magenta = "#FF007F"
scale = 2

class EntryWindow():
    
    def __init__(self):
        self.window = Tk()
        
        self.window.title("S.A.W.D.U.S.T. Cloud")
        self.window.geometry(f"{300*scale}x{275*scale}")
        self.window.config(background = twitter_blue)


        title1 = Label(self.window, text = 'S.A.W.D.U.S.T. Cloud', font = ("Arial", 18*scale, "bold"), fg = "white", bg = twitter_blue)
        title1.pack()
        title2 = Label(self.window, text = '(Sentiment Analysis of Word Distribution\nUsing Searches of Twitter)', font = ("Arial", 12*scale), fg = "white", bg = twitter_blue)
        title2.pack()
        
        separatorLine = ttk.Separator(self.window, orient = "horizontal")
        separatorLine.pack(fill="x")

        instruction1 = Label(self.window, text = 'Enter a word to analyse:', font = ("Arial", 12*scale, "bold"), fg = "white", bg = twitter_blue)
        instruction1.place(x = 0*scale, y = 80*scale)
        
        self.text = Entry(self.window, width = 15, font = ("Arial", 12*scale))
        self.text.place(x = 85*scale, y = 105*scale)
        
        instruction2 = Label(self.window, text = "Choose a colour scheme:", font = ("Arial", 12*scale, "bold"), fg = "white", bg = twitter_blue)
        instruction2.place(x = 0*scale, y = 125*scale)
        
        self.radio_var = IntVar()
        self.radio_var.set(1)
        radio1 = Radiobutton(self.window, bg = twitter_blue, text = "Standard", font = ("Arial", 12*scale, "bold"), variable = self.radio_var,  value = 1, indicatoron=0)
        radio1.place(x = 25*scale, y = 150*scale)
        radio2 = Radiobutton(self.window, bg = twitter_blue, text = "Colourblind", font = ("Arial", 12*scale, "bold"), variable = self.radio_var, value = 2, indicatoron=0)
        radio2.place(x = 25*scale, y = 175*scale)
        
        scheme1Positive = Label(self.window, text = "Positive", font = ("Helvetica", 12*scale), fg = "black", bg = green)
        scheme1Positive.place(x = 155*scale, y = 150*scale)
        scheme1Negative = Label(self.window, text = "Negative", font = ("Helvetica", 12*scale), fg = "black", bg = red)
        scheme1Negative.place(x = 225*scale, y = 150*scale)
        
        scheme2Positive = Label(self.window, text = "Positive", font = ("Helvetica", 12*scale), fg = "black", bg = green)
        scheme2Positive.place(x = 155*scale, y = 180*scale)
        scheme2Negative = Label(self.window, text = "Negative", font = ("Helvetica", 12*scale), fg = "black", bg = magenta)
        scheme2Negative.place(x = 225*scale, y = 180*scale)

        self.generateButton = Button(self.window, text = "Generate Word Cloud!", font = ("Arial", 10*scale), command = self.attemptGeneration, fg = twitter_blue, activeforeground = twitter_blue, bg = "white")
        self.generateButton.place(x = 77*scale, y = 213*scale)
        
        self.errorLabel = Label(self.window, text = "", font = ("Arial", 12*scale, "bold"), fg = red, bg = twitter_blue)
        self.errorLabel.place(x = 0*scale, y = 245*scale)
    
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
            Wordclouds.plotWordCloud(word, self.radio_var.get() != 1)
    
    def run(self):
        self.window.mainloop()

window = EntryWindow()
window.run()