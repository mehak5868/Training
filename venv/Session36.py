from tkinter import *

window = Tk()
clas =Label(window , text = "CLASS").grid(row = 1)
eng=Label(window , text = "ENGLISH").grid(row = 1, column = 2)
mat=Label(window , text = "MATHS").grid(row = 1, column = 3)
hin=Label(window , text = "HINDI").grid(row = 1, column = 4)
pun=Label(window , text = "PUNJABI").grid(row = 1, column = 5)
add =Label(window , text = "ADDITIONAL ").grid(row=1,column = 6)
lkg = Label(window , text = "LKG     :").grid(row = 2)
ukg = Label(window , text = "UKG    :").grid(row = 3)
first = Label(window , text = "First     :").grid(row = 4)
second =Label(window , text = "Second :").grid(row = 5)
third =Label(window , text = "Third    :").grid(row = 6)

le =Entry(window).grid(row=2,column = 2)
lm =Entry(window).grid(row=2,column = 3)
lh =Entry(window).grid(row=2,column = 4)
lp =Entry(window).grid(row=2,column = 5)
la =Entry(window).grid(row=2,column = 6)

ue =Entry(window).grid(row=3,column = 2)
um =Entry(window).grid(row=3,column = 3)
uh =Entry(window).grid(row=3,column = 4)
up =Entry(window).grid(row=3,column = 5)
ua =Entry(window).grid(row=3,column = 6)

fe =Entry(window).grid(row=4,column = 2)
fm =Entry(window).grid(row=4,column = 3)
fh =Entry(window).grid(row=4,column = 4)
fp =Entry(window).grid(row=4,column = 5)
fa =Entry(window).grid(row=4,column = 6)

se =Entry(window).grid(row=5,column = 2)
sm =Entry(window).grid(row=5,column = 3)
sh =Entry(window).grid(row=5,column = 4)
sp =Entry(window).grid(row=5,column = 5)
sa =Entry(window).grid(row=5,column = 6)

te =Entry(window).grid(row=6,column = 2)
tm =Entry(window).grid(row=6,column = 3)
th =Entry(window).grid(row=6,column = 4)
tp =Entry(window).grid(row=6,column = 5)
ta =Entry(window).grid(row=6,column = 6)


#fourth =Label(window , text = "Fourth:").grid(row = 4)
window .mainloop()
