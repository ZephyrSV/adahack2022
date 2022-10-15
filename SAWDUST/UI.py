from tkinter import *

window = Tk()
window.title('S.A.W.D.U.S.T. Cloud')

btn=Button(window, text="Generate Word Cloud!", bg='blue')
btn.place(x=70, y=400)

lbl=Label(window, text="S.A.W.D.U.S.T. Cloud\n(Sentiment Analysis of Word Distribution\nUsing Searches of Twitter)", fg='blue', font=("Helvetica", 16))
lbl.place(x=20, y=0)

lbl=Label(window, text="Word to Analyze", fg='blue', font=("Helvetica", 14))
lbl.place(x=50, y=140)

txtfld=Entry(window, bd=5)
txtfld.place(x=60, y=170)

window.geometry("300x500")
window.mainloop()



