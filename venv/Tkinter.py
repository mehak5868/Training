from tkinter import *

window = Tk()
window.title("Form")
m = Menu(window)
window.config(menu = m)
filemenu = Menu(m)
m.add_cascade(label ='File',menu =filemenu)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit",command = window.quit)
helpmenu = Menu (m)
m.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label='About')

name1 = Label (window , text = "First Name:").grid(row = 0)

name2 = Label (window , text = "Last Name:").grid(row = 1)

n1=Entry(window)

n2=Entry(window)

n1.grid(row=0,column=1)
n2.grid(row=1,column=1)
lb = Listbox(window)
lb.insert(1,'Python')#.grid(row = 2)
lb.insert(2,'Java')#.grid(row=3)
lb.insert(3,'C++')#.grid(row=4)
lb.grid(row=2)
window.mainloop()



