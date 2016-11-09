gifdir = "./"
import tkinter
from tkinter import *
top = tkinter.Tk()
frame = Frame(width=768, height=576, bg="#ffd61e", colormap="new")
frame.pack(side = LEFT, fill=BOTH)
def vertrektrijden():
    print('test')
ditstation = PhotoImage(file=gifdir+"dit-station.gif")
anstation = PhotoImage(file=gifdir+"ander-station.gif")
B = tkinter.Button(frame, text ="Dit station", command = vertrektrijden, padx = 20, image=ditstation)
A = tkinter.Button(frame, text ="Ander station", command = vertrektrijden, padx = 20, image=anstation)
A.pack(pady = 20, padx = 20, side=RIGHT)
B.pack(pady = 20, padx = 20 , side=LEFT)
top.mainloop()
