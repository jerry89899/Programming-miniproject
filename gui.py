import tkinter

top = tkinter.Tk()

def vertrektrijden():
    print('test')

B = tkinter.Button(top, text ="Actuele vertrektijden", command = vertrektrijden)

B.pack()
top.mainloop()
