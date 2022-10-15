import Wordclouds
from tkinter import *
import tkinter as tk

twitterBlue = '#1DA1F2'

root = tk.Tk()
root.title('Sawdust cloud')

root.configure(background=twitterBlue)

window_width = 400
window_height = 700

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# create a grid
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

#add a label to the top of the window
tk.Label(mainframe, text="Sawdust Cloud").grid(row=0, column=0, sticky=W)

#add a text box with ephedefault text
text_box = Text(root, height=10, width=30, padx=15, pady=15, font="Ubuntu", bg="white", fg="black", wrap=WORD, borderwidth=2, relief="groove")
text_box.pack()

Colorblind = True
#add radio buttons and get which button is pressed
radio_var = IntVar()
radio_var.set(1)
radio1 = tk.Radiobutton(mainframe, text="Colorblind", variable=radio_var, value=1)
radio2 = tk.Radiobutton(mainframe, text="Colorful", variable=radio_var, value=2)
radio1.grid(row=1, column=0, sticky=W)
radio2.grid(row=2, column=0, sticky=W)
#get which radio button is selected





#add a button that runs Wordclouds.plotWordCloud when clicked using the text in the text box
button = Button(root, text="Generate Wordcloud", command=lambda: Wordclouds.plotWordCloud(text_box.get("1.0", "end-1c"),  radio_var.get() == 1))
button.pack()

#mainloop
root.mainloop()
