from tkinter import *
from Session36A import *

def academicsWindow():
    def onClick():
        st = "First"

        e11 = fe.get()

        m11 = fm.get()

        h11 = fh.get()

        p11 = fp.get()

        ev11 = fev.get()

        ref1 = prime(1,st, int(e11), int(m11), int(h11), int(p11), int(ev11))
        db = Dbhelper1()
        db.saveMarksPrimary(ref1)


        st2 = "Second"

        e22 = se.get()

        m22 = sm.get()

        h22 = sh.get()

        p22 = sp.get()

        ev22 = sev.get()

        ref2 = prime(2,st2, int(e22), int(m22), int(h22), int(p22), int(ev22))
        db = Dbhelper1()
        db.saveMarksPrimary(ref2)


        st3 = "Third"

        e33 = te.get()

        m33 = tm.get()

        h33 = th.get()

        p33 = tp.get()

        ev33 = tev.get()

        ref3 = prime(3,st3, int(e33), int(m33), int(h33), int(p33), int(ev33))
        db = Dbhelper1()
        db.saveMarksPrimary(ref3)

        file = open("StudentData.csv","a")
        file.write(ref1.detailsInCsv1())
        file.write(ref2.detailsInCsv1())
        file.write(ref3.detailsInCsv1())


        st4 = "Fourth"

        english = foe.get()

        maths = fom.get()

        hindi = foh.get()

        punjabi = fop.get()

        sst = foa.get()

        sci = fosc.get()

        sref = Students(4,st4,int(english),int(maths),int(hindi),int(punjabi),int(sst),int(sci))
        db = Dbhelper()
        db.saveMarks(sref)


        st5 ="Fifth"

        e1=fie.get()

        m1 = fim.get()

        h1 = fih.get()

        p1 = fip.get()

        ss1 = fia.get()

        s1 =fisc.get()

        sref1 = Students(5,st5,int(e1),int(m1),int(h1),int(p1),int(ss1),int(s1))
        db =Dbhelper()
        db.saveMarks(sref1)


        st6 ="Sixth"

        e2 = sie.get()

        m2 = sim.get()

        h2 = sih.get()

        p2 = sip.get()

        ss2= sia.get()

        s2 = sisc.get()

        sref2 = Students(6,st6,int(e2),int(m2),int(h2),int(p2),int(ss2),int(s2))
        db=Dbhelper()


        st7 ="Seventh"

        e3 = see.get()

        m3 = sem.get()

        h3 = seh.get()

        p3 = sep.get()

        ss3 = sea.get()

        s3 = sesc.get()

        sref3 =Students(7,st7,int(e3),int(m3),int(h3),int(p3),int(ss3),int(s3))
        db = Dbhelper()
        db.saveMarks(sref3)


        st8="Eighth"

        e4 = eie.get()

        m4 = eim.get()

        h4 = eih.get()

        p4 =eip.get()

        ss4 = eia .get()

        s4 =  eisc.get()

        sref4 = Students(8,st8,int(e4),int(m4),int(h4),int(p4),int(ss4),int(s4))
        db = Dbhelper()
        db.saveMarks(sref4)


        st9="Ninth"

        e5 = nie.get()

        m5 = nim.get()

        h5 = nih.get()

        p5 = nip.get()

        ss5 = nia.get()

        s5 = eisc.get()

        sref5 = Students(9,st9, int(e5), int(m5), int(h5), int(p5), int(ss5), int(s5))
        db = Dbhelper()
        db.saveMarks(sref5)


        st10= "Tenth"

        e6 = tee.get()

        m6 = tem.get()

        h6 = teh.get()

        p6 = tep.get()

        ss6= tea.get()

        s6 = tesc.get()

        sref6 = Students(10,st10, int(e6), int(m6), int(h6), int(p6), int(ss6), int(s6))
        db = Dbhelper()
        db.saveMarks(sref6)

        file1 = open("StudentDataSec.csv","a")
        file1.write(sref.detailsInCsv())
        file1.write(sref1.detailsInCsv())
        file1.write(sref2.detailsInCsv())
        file1.write(sref3.detailsInCsv())
        file1.write(sref4.detailsInCsv())
        file1.write(sref5.detailsInCsv())
        file1.write(sref6.detailsInCsv())

    window = Tk()
    head1 = Label(window,text = "Primary Class").grid(row=0,column = 3)
    clas = Label(window, text="CLASS").grid(row=1)
    eng = Label(window, text="ENGLISH").grid(row=1, column=2)
    mat = Label(window, text="MATHS").grid(row=1, column=3)
    hin = Label(window, text="HINDI").grid(row=1, column=4)
    pun = Label(window, text="PUNJABI").grid(row=1, column=5)
    evs = Label(window, text="EVS").grid(row=1, column=6)

    one = Label(window, text="FIRST   :").grid(row=2)
    two = Label(window, text="SECOND  :").grid(row=3)
    three = Label(window, text="THIRD :").grid(row=4)

    fe = Entry(window)
    fe.grid(row=2, column=2)  # first class
    fm = Entry(window)
    fm.grid(row=2, column=3)
    fh = Entry(window)
    fh.grid(row=2, column=4)
    fp = Entry(window)
    fp.grid(row=2, column=5)
    fev = Entry(window)
    fev.grid(row=2, column=6)

    se = Entry(window)
    se.grid(row=3, column=2)  # second class
    sm = Entry(window)
    sm.grid(row=3, column=3)
    sh = Entry(window)
    sh.grid(row=3, column=4)
    sp = Entry(window)
    sp.grid(row=3, column=5)
    sev = Entry(window)
    sev.grid(row=3, column=6)
    # sa = Entry(window).grid(row=3, column=6)
    # ssc = Entry(window).grid(row=3, column=7)

    te = Entry(window)
    te.grid(row=4, column=2)  # third class
    tm = Entry(window)
    tm.grid(row=4, column=3)
    th = Entry(window)
    th.grid(row=4, column=4)
    tp = Entry(window)
    tp.grid(row=4, column=5)
    tev = Entry(window)
    tev.grid(row=4, column=6)


###########################################################
    head2 =Label(window , text = "Secondary Class")
    head2.grid(row = 6,column = 3)
    eng=Label(window , text = "ENGLISH")
    eng.grid(row = 7, column = 2)
    mat=Label(window , text = "MATHS")
    mat.grid(row = 7, column = 3)
    hin=Label(window , text = "HINDI").grid(row = 7, column = 4)
    pun=Label(window , text = "PUNJABI").grid(row = 7, column = 5)
    ss =Label(window , text = "SST ").grid(row=7,column = 6)
    sc =Label(window , text = "Science ").grid(row=7,column = 7)



    four = Label(window , text = "FOURTH   :").grid(row = 8)
    five = Label(window , text = "FIFTH   :").grid(row = 9)
    six= Label(window , text = "SIXTH     :").grid(row = 10)
    seven =Label(window , text = "SEVENTH :").grid(row = 11)
    eight =Label(window , text = "EIGHTH   :").grid(row = 12)
    nine = Label(window , text = "NINTH :").grid(row=13)
    tenth = Label(window ,text = "TENTH").grid(row =14)



    foe =Entry(window)
    foe .grid(row=8,column = 2)# fouth class
    fom =Entry(window)
    fom.grid(row=8,column = 3)
    foh =Entry(window)
    foh.grid(row=8,column = 4)
    fop =Entry(window)
    fop.grid(row=8,column = 5)
    foa =Entry(window)
    foa.grid(row=8,column = 6)
    fosc = Entry(window)
    fosc.grid(row=8,column = 7)

    fie =Entry(window)
    fie.grid(row=9,column = 2) # fifth
    fim =Entry(window)
    fim.grid(row=9,column = 3)
    fih =Entry(window)
    fih.grid(row=9,column = 4)
    fip =Entry(window)
    fip.grid(row=9,column = 5)
    fia =Entry(window)
    fia   .grid(row=9,column = 6)
    fisc = Entry(window)
    fisc.grid(row=9,column = 7)

    sie =Entry(window)
    sie.grid(row=10,column = 2) #sixth
    sim =Entry(window)
    sim.grid(row=10,column = 3)
    sih =Entry(window)
    sih   .grid(row=10,column = 4)
    sip =Entry(window)
    sip.grid(row=10,column = 5)
    sia =Entry(window)
    sia.grid(row=10,column = 6)
    sisc = Entry(window)
    sisc.grid(row=10,column = 7)

    see =Entry(window)
    see.grid(row=11,column = 2)# seventh
    sem =Entry(window)
    sem.grid(row=11,column = 3)
    seh =Entry(window)
    seh.grid(row=11,column = 4)
    sep =Entry(window)
    sep.grid(row=11,column = 5)
    sea =Entry(window)
    sea.grid(row=11,column = 6)
    sesc = Entry(window)
    sesc.grid(row=11,column = 7)

    eie =Entry(window)
    eie.grid(row=12,column = 2) #eighth
    eim =Entry(window)
    eim.grid(row=12,column = 3)
    eih =Entry(window)
    eih.grid(row=12,column = 4)
    eip =Entry(window)
    eip.grid(row=12,column = 5)
    eia =Entry(window)
    eia.grid(row=12,column = 6)
    eisc = Entry(window)
    eisc.grid(row=12,column = 7)

    nie =Entry(window)
    nie.grid(row=13,column = 2) # ninth
    nim =Entry(window)
    nim   .grid(row=13,column = 3)
    nih =Entry(window)
    nih.grid(row=13,column = 4)
    nip =Entry(window)
    nip.grid(row=13,column = 5)
    nia =Entry(window)
    nia.grid(row=13,column = 6)
    nisc = Entry(window)
    nisc.grid(row=13,column = 7)

    tee =Entry(window)
    tee.grid(row=14,column = 2) #tenth
    tem =Entry(window)
    tem.grid(row=14,column = 3)
    teh =Entry(window)
    teh.grid(row=14,column = 4)
    tep =Entry(window)
    tep.grid(row=14,column = 5)
    tea =Entry(window)
    tea.grid(row=14,column = 6)
    tesc = Entry(window)
    tesc.grid(row=14,column = 7)


    sub = Button(window,text="Submit",command =onClick).grid(row=15,column = 2)
    #fourth =Label(window , text = "Fourth:").grid(row = 4)
    window .mainloop()
#academicsWindow()

def Activity():
    def onClick():
        a1 = act1.get()

        go1 = g1 .get()

        si1 = s1 .get()

        br1 = b1 .get()

        aref = activity (1,a1,int(go1),int(si1),int(br1))
        db = Dbhelper2()
        db.saveActivity(aref)

        a2 = act2.get()

        go2 = g2.get()

        si2 = s2.get()

        br2 = b2.get()

        aref1 = activity(2,a2,int( go2),int( si2),int (br2))
        db = Dbhelper2()
        db.saveActivity(aref1)

        a3 = act3.get()

        go3 = g3.get()

        si3 = s3.get()

        br3 = b3.get()

        aref3 = activity(3,a3,int (go3), int(si3),int (br3))
        db = Dbhelper2()
        db.saveActivity(aref3)

        a4 = act4.get()

        go4 = g4.get()

        si4 = s4.get()

        br4 = b4.get()

        aref4 = activity(4,a4, int(go4), int(si4), int(br4))
        db = Dbhelper2()
        db.saveActivity(aref4)

        a5 = act5.get()

        go5 = g5.get()

        si5 = s5.get()

        br5 = b5.get()

        aref5 = activity(5,a5, int(go5), int(si5), int(br5))
        db = Dbhelper2()
        db.saveActivity(aref5)
        file2 = open("sports.csv","a")
        file2.write(aref.detailsInCsv2())
        file2.write(aref1.detailsInCsv2())
        file2.write(aref3.detailsInCsv2())
        file2.write(aref4.detailsInCsv2())
        file2.write(aref5.detailsInCsv2())

        pass

    window =Tk()
    act = Label(window , text ="Activity")
    act.grid(row=6)

    gold = Label(window,text="Gold")
    gold.grid(row=6,column=2)

    silver = Label(window,text ="Silver")
    silver.grid(row=6,column=3)

    bronze = Label(window,text="Bronze")
    bronze.grid(row=6,column=4)

    act1 = Entry(window)
    act1.grid(row=7)

    g1 = Entry(window)
    g1.grid(row=7,column=2)

    s1 =Entry(window)
    s1.grid(row=7,column=3)

    b1 =Entry(window)
    b1.grid(row=7,column=4)

    act2 = Entry(window)
    act2.grid(row=8)

    g2 = Entry(window)
    g2.grid(row=8, column=2)

    s2 = Entry(window)
    s2.grid(row=8, column=3)

    b2 = Entry(window)
    b2.grid(row=8, column=4)

    act3 = Entry(window)
    act3.grid(row=9)

    g3 = Entry(window)
    g3.grid(row=9, column=2)

    s3 = Entry(window)
    s3.grid(row=9, column=3)

    b3 = Entry(window)
    b3.grid(row=9, column=4)

    act4 = Entry(window)
    act4.grid(row=10)

    g4 = Entry(window)
    g4.grid(row=10, column=2)

    s4 = Entry(window)
    s4.grid(row=10, column=3)

    b4 = Entry(window)
    b4.grid(row=10, column=4)

    act5 = Entry(window)
    act5.grid(row=11)

    g5 = Entry(window)
    g5.grid(row=11, column=2)

    s5 = Entry(window)
    s5.grid(row=11, column=3)

    b5 = Entry(window)
    b5.grid(row=11, column=4)

    sub= Button (window,text = "Submit",command=onClick)
    sub.grid(row = 12,column =2)


    window.mainloop()
#Activity()

def Sports():
    def onClick():
        a1 = SpName.get()

        Go1 = g1.get()

        S1 = s1.get()

        B1 = b1.get()

        aref = activity(1,a1, int(Go1), int(S1), int(B1))
        db = Dbhelper2()
        db.saveActivity(aref)

        a2 = SpName1.get()

        Go2 = g2.get()

        S2 = s2.get()

        B2 = b2.get()

        aref2 = activity(2,a2,int (Go2),int (S2),int (B2))
        db = Dbhelper2()
        db.saveActivity(aref2)

        a3 = SpName2.get()

        Go3 = g3.get()

        S3 = s3.get()

        B3 = b3.get()

        aref3 = activity(3,a3, int(Go3), int(S3), int(B3))
        db = Dbhelper2()
        db.saveActivity(aref3)

        a4 = SpName3.get()
        Go4 = g4.get()
        S4 = s4.get()

        B4 = b4.get()

        aref4 = activity(4,a4, int(Go4), int(S4), int(B4))
        db = Dbhelper2()
        db.saveActivity(aref4)

        a5 = SpName4.get()

        Go5 = g5.get()

        S5 = s5.get()

        B5 = b5.get()

        aref5 = activity(5,a5, int(Go5),int (S5), int(B5))
        db = Dbhelper2()
        db.saveActivity(aref5)

        file3 =open("activity.csv","a")
        file3.write(aref.detailsInCsv2())
        file3.write(aref2.detailsInCsv2())
        file3.write(aref3.detailsInCsv2())
        file3.write(aref4.detailsInCsv2())
        file3.write(aref5.detailsInCsv2())
        file3.close()

    window=Tk()

    Spo = Label(window , text = "sports ")
    Spo.grid(row = 5 , column= 3)

    sport = Label(window , text ="SPORTS NAME")
    sport.grid(row = 6 , column = 2)

    gold = Label(window , text = "GOLD")
    gold.grid(row = 6 , column = 3)

    Silver = Label(window , text = "SILVER ")
    Silver.grid(row = 6 , column = 4)

    Bronze = Label(window , text = "BRONZE")
    Bronze.grid(row = 6, column = 5)

    SpName= Entry(window)
    SpName.grid(row = 7, column = 2)

    g1 = Entry(window)
    g1.grid(row=7 , column = 3)

    s1 = Entry(window)
    s1.grid(row=7, column = 4)

    b1 = Entry(window)
    b1.grid(row=7 , column = 5)

    SpName1 = Entry(window)
    SpName1.grid(row=8, column=2)

    g2 = Entry(window)
    g2.grid(row=8, column=3)

    s2 = Entry(window)
    s2.grid(row=8, column=4)

    b2 = Entry(window)
    b2.grid(row=8, column=5)

    SpName2 = Entry(window)
    SpName2.grid(row=9, column=2)

    g3 = Entry(window)
    g3.grid(row=9, column=3)

    s3 = Entry(window)
    s3.grid(row=9, column=4)

    b3 = Entry(window)
    b3.grid(row=9, column=5)

    SpName3 = Entry(window)
    SpName3.grid(row=10, column=2)

    g4 = Entry(window)
    g4.grid(row=10, column=3)

    s4 = Entry(window)
    s4.grid(row=10, column=4)

    b4 = Entry(window)
    b4.grid(row=10, column=5)

    SpName4= Entry(window)
    SpName4.grid(row=11, column=2)

    g5 = Entry(window)
    g5.grid(row=11, column=3)

    s5 = Entry(window)
    s5.grid(row=11, column=4)

    b5 = Entry(window)
    b5.grid(row=11, column=5)


    BUTTON= Button(window, text = "Submit", command = onClick)
    BUTTON.grid(row = 12 , column = 3)

    window.mainloop()

Sports()