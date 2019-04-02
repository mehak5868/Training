from tkinter import *
from Session36A import *
def HigherClass () :
    def OnClick():
        sub1 =subject1.get()

        e1 =elvensubject1.get()

        t1 =twelvesubject1.get()

        href = higherClass(sub1 , int(e1), int(t1))
        db= Dbhelper3()
        db.saveMarks(href)


        sub2 =subject2.get()

        e2 = elvensubject2.get()

        t2 = twelvesubject2.get()
        href2 = higherClass(sub2, int(e2), int(t2))
        db = Dbhelper3()
        db.saveMarks(href2)

        sub3 = subject3.get()

        e3 = elvensubject3.get()

        t3 = twelvesubject3.get()
        href3 = higherClass(sub3, int(e3),int  (t3))
        db = Dbhelper3()
        db.saveMarks(href3)

        sub4 = subject4.get()

        e4 = elvensubject4.get()

        t4 = twelvesubject4.get()
        href4 = higherClass(sub4,int(e4),int(t4))
        db =Dbhelper3()
        db .saveMarks(href4)


        sub5 = subject5.get()

        e5 = elvensubject5.get()

        t5 = twelvesubject5.get()
        href5 = higherClass(sub5,int(e5),int(t5))
        db = Dbhelper3()
        db . saveMarks(href5)



    window = Tk()
    Standard1 = Label(window , text = "Class")
    Standard1.grid(row=6)

    eleven = Label(window ,text ="+1")
    eleven.grid(row=7)

    twelve = Label(window , text ="+2")
    twelve.grid(row=8)

    subject1 = Entry (window)
    subject1.grid(row=6,column = 2)

    subject2 = Entry(window)
    subject2.grid(row=6, column=3)

    subject3 = Entry(window)
    subject3.grid(row=6, column=4)

    subject4 = Entry(window)
    subject4.grid(row=6, column=5)

    subject5 = Entry(window)
    subject5.grid(row=6, column=6)

    elvensubject1 = Entry(window)
    elvensubject1.grid(row=7,column = 2)

    elvensubject2= Entry(window)
    elvensubject2.grid(row=7,column=3)

    elvensubject3 = Entry(window)
    elvensubject3.grid(row=7, column=4)

    elvensubject4 = Entry(window)
    elvensubject4.grid(row=7, column=5)

    elvensubject5 = Entry(window)
    elvensubject5.grid(row=7, column=6)

    twelvesubject1 = Entry(window)
    twelvesubject1.grid(row=8, column=2)

    twelvesubject2 = Entry(window)
    twelvesubject2.grid(row=8, column=3)

    twelvesubject3 = Entry(window)
    twelvesubject3.grid(row=8, column=4)

    twelvesubject4 = Entry(window)
    twelvesubject4.grid(row=8, column=5)

    twelvesubject5 = Entry(window)
    twelvesubject5.grid(row=8, column=6)

    sub = Button(window ,text ="Submit",command =  OnClick )
    sub.grid(row = 9 , column =2)

    window.mainloop()
HigherClass()
