from tkinter import *
from Session36A import *


def academicsWindow():
    def onClick():
        english = foe.get()
        maths = fom.get()
        hindi = foh.get()
        punjabi = fop.get()
        sst = foa.get()
        sci = fosc.get()
        sref = Student(0,int(english),int(maths),int(hindi),int(punjabi),int(sst),int(sci))
        db = Dbhelper()
        db.saveMarks(sref)


    window = Tk()
    clas =Label(window , text = "CLASS").grid(row = 1)
    eng=Label(window , text = "ENGLISH").grid(row = 1, column = 2)
    mat=Label(window , text = "MATHS").grid(row = 1, column = 3)
    hin=Label(window , text = "HINDI").grid(row = 1, column = 4)
    pun=Label(window , text = "PUNJABI").grid(row = 1, column = 5)
    ss =Label(window , text = "SST ").grid(row=1,column = 6)
    sc =Label(window , text = "Science ").grid(row=1,column = 7)


    four = Label(window , text = "FOURTH   :").grid(row = 5)
    five = Label(window , text = "FIFTH   :").grid(row = 6)
    six= Label(window , text = "SIXTH     :").grid(row = 7)
    seven =Label(window , text = "SEVENTH :").grid(row = 8)
    eight =Label(window , text = "EIGHTH   :").grid(row = 9)
    nine = Label(window , text = "NINTH :").grid(row=10)
    tenth = Label(window ,text = "TENTH").grid(row =11)



    foe =Entry(window).grid(row=5,column = 2) # fouth class
    fom =Entry(window).grid(row=5,column = 3)
    foh =Entry(window).grid(row=5,column = 4)
    fop =Entry(window).grid(row=5,column = 5)
    foa =Entry(window).grid(row=5,column = 6)
    fosc = Entry(window).grid(row=5,column = 7)

    fie =Entry(window).grid(row=6,column = 2) # fifth
    fim =Entry(window).grid(row=6,column = 3)
    fih =Entry(window).grid(row=6,column = 4)
    fip =Entry(window).grid(row=6,column = 5)
    fia =Entry(window).grid(row=6,column = 6)
    fisc = Entry(window).grid(row=6,column = 7)

    sie =Entry(window).grid(row=7,column = 2) #sixth
    sim =Entry(window).grid(row=7,column = 3)
    sih =Entry(window).grid(row=7,column = 4)
    sip =Entry(window).grid(row=7,column = 5)
    sia =Entry(window).grid(row=7,column = 6)
    sisc = Entry(window).grid(row=7,column = 7)

    see =Entry(window).grid(row=8,column = 2) # seventh
    sem =Entry(window).grid(row=8,column = 3)
    seh =Entry(window).grid(row=8,column = 4)
    sep =Entry(window).grid(row=8,column = 5)
    sea =Entry(window).grid(row=8,column = 6)
    sesc = Entry(window).grid(row=8,column = 7)

    eie =Entry(window).grid(row=9,column = 2) #eighth
    eim =Entry(window).grid(row=9,column = 3)
    eih =Entry(window).grid(row=9,column = 4)
    eip =Entry(window).grid(row=9,column = 5)
    eia =Entry(window).grid(row=9,column = 6)
    eisc = Entry(window).grid(row=9,column = 7)

    nie =Entry(window).grid(row=10,column = 2) # ninth
    nim =Entry(window).grid(row=10,column = 3)
    nih =Entry(window).grid(row=10,column = 4)
    nip =Entry(window).grid(row=10,column = 5)
    nia =Entry(window).grid(row=10,column = 6)
    nisc = Entry(window).grid(row=10,column = 7)

    tee =Entry(window).grid(row=11,column = 2) #tenth
    tem =Entry(window).grid(row=11,column = 3)
    teh =Entry(window).grid(row=11,column = 4)
    tep =Entry(window).grid(row=11,column = 5)
    tea =Entry(window).grid(row=11,column = 6)
    tesc = Entry(window).grid(row=11,column = 7)


    sub = Button(window,text="Submit",command =onClick).grid(row=12,column = 2)
    #fourth =Label(window , text = "Fourth:").grid(row = 4)
    window .mainloop()
academicsWindow()
def academicsPrimary ():

    window =Tk()
    clas = Label(window, text="CLASS").grid(row=1)
    eng = Label(window, text="ENGLISH").grid(row=1, column=2)
    mat = Label(window, text="MATHS").grid(row=1, column=3)
    hin = Label(window, text="HINDI").grid(row=1, column=4)
    pun = Label(window, text="PUNJABI").grid(row=1, column=5)

    one = Label(window, text="FIRST   :").grid(row=2)
    two = Label(window, text="SECOND  :").grid(row=3)
    three = Label(window, text="THIRD :").grid(row=4)

    fe = Entry(window).grid(row=2, column=2)  # first class
    fm = Entry(window).grid(row=2, column=3)
    fh = Entry(window).grid(row=2, column=4)
    fp = Entry(window).grid(row=2, column=5)
    #fs = Entry(window).grid(row=2, column=6)
    #fsc = Entry(window).grid(row=2, column=7)

    se = Entry(window).grid(row=3, column=2)  # second class
    sm = Entry(window).grid(row=3, column=3)
    sh = Entry(window).grid(row=3, column=4)
    sp = Entry(window).grid(row=3, column=5)
    #sa = Entry(window).grid(row=3, column=6)
    #ssc = Entry(window).grid(row=3, column=7)

    te = Entry(window).grid(row=4, column=2)  # third class
    tm = Entry(window).grid(row=4, column=3)
    th = Entry(window).grid(row=4, column=4)
    tp = Entry(window).grid(row=4, column=5)
    #ta = Entry(window).grid(row=4, column=6)
    #tsc = Entry(window).grid(row=4, column=7)

    sub = Button(window , text ="Submit").grid(row= 5 , column = 2)
    window.mainloop()

#academicsPrimary()