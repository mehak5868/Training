from tkinter import *
from Session19A import *
def pointsupdate():
    point=epoint.get()

window=Tk()

lpoint = Label(window,text="Points")
lpoint.pack()

epoint=Entry(window)
epoint.pack()

ldone=Button(window,text="Done",command=pointsupdate)
