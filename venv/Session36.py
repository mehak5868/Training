from tkinter import *
from Session36A import *
c1 =[]
c2=[]
c3=[]
c4 =[]
c5=[]
c6=[]
c7=[]
c8 =[]
c9 =[]
c10 =[]
def academicsWindow():
    def onClick():
        st = "First"
        c1.append(st)
        e11 = fe.get()
        c1.append(e11)
        m11 = fm.get()
        c1.append(m11)
        h11 = fh.get()
        c1.append(h11)
        p11 = fp.get()
        c1.append(p11)
        ev11 = fev.get()
        c1.append(ev11)
        ref1 = prime(0, int(e11), int(m11), int(h11), int(p11), int(ev11))
        db = Dbhelper1()
        db.saveMarksPrimary(ref1)
        print(c1)

        st2 = "Second"
        c2.append(st2)
        e22 = se.get()
        c2.append(e22)
        m22 = sm.get()
        c2.append(m22)
        h22 = sh.get()
        c2.append(h22)
        p22 = sp.get()
        c2.append(p22)
        ev22 = sev.get()
        c2.append(ev22)
        ref2 = prime(0, int(e22), int(m22), int(h22), int(p22), int(ev22))
        db = Dbhelper1()
        db.saveMarksPrimary(ref2)
        print(c2)

        st3 = "Third"
        c3.append(st3)
        e33 = te.get()
        c3.append(e33)
        m33 = tm.get()
        c3.append(m33)
        h33 = th.get()
        c3.append(h33)
        p33 = tp.get()
        c3.append(p33)
        ev33 = tev.get()
        c3.append(ev33)
        ref3 = prime(0, int(e33), int(m33), int(h33), int(p33), int(ev33))
        db = Dbhelper1()
        db.saveMarksPrimary(ref3)
        print(c3)

        st4 = "Fifth"
        c4.append(st4)
        english = foe.get()
        c4.append(english)
        maths = fom.get()
        c4.append(maths)
        hindi = foh.get()
        c4.append(hindi)
        punjabi = fop.get()
        c4.append(punjabi)
        sst = foa.get()
        c4.append(sst)
        sci = fosc.get()
        c4.append(sci)
        sref = Students(0,int(english),int(maths),int(hindi),int(punjabi),int(sst),int(sci))
        db = Dbhelper()
        db.saveMarks(sref)
        print(c4)

        st5 ="Sixth"
        c5.append(st5)
        e1=fie.get()
        c5.append(e1)
        m1 = fim.get()
        c5.append(m1)
        h1 = fih.get()
        c5.append(h1)
        p1 = fip.get()
        c5.append(p1)
        ss1 = fia.get()
        c5.append(ss1)
        s1 =fisc.get()
        c5.append(s1)
        sref1 = Students(0,int(e1),int(m1),int(h1),int(p1),int(ss1),int(s1))
        db =Dbhelper()
        db.saveMarks(sref1)
        print(c5)

        st6 ="Sixth"
        c6.append(st6)
        e2 = sie.get()
        c6.append(e2)
        m2 = sim.get()
        c6.append(m2)
        h2 = sih.get()
        c6.append(h2)
        p2 = sip.get()
        c6.append(p2)
        ss2= sia.get()
        c6.append(ss2)
        s2 = sisc.get()
        c6.append(s2)
        sref2 = Students(0,int(e2),int(m2),int(h2),int(p2),int(ss2),int(s2))
        db=Dbhelper()
        db.saveMarks(sref2)
        print(c6)

        st7 ="Seventh"
        c7.append(st7)
        e3 = see.get()
        c7.append(e3)
        m3 = sem.get()
        c7.append(m3)
        h3 = seh.get()
        c7.append(h3)
        p3 = sep.get()
        c7.append(p3)
        ss3 = sea.get()
        c7.append(ss3)
        s3 = sesc.get()
        c7.append(s3)
        sref3 =Students(0,int(e3),int(m3),int(h3),int(p3),int(ss3),int(s3))
        db = Dbhelper()
        db.saveMarks(sref3)
        print(c7)

        st8="Eighth"
        c8.append(st8)
        e4 = eie.get()
        c8.append(e4)
        m4 = eim.get()
        c8.append(m4)
        h4 = eih.get()
        c8.append(h4)
        p4 =eip.get()
        c8.append(p4)
        ss4 = eia .get()
        c8.append(ss4)
        s4 =  eisc.get()
        c8.append(s4)
        sref4 = Students(0,int(e4),int(m4),int(h4),int(p4),int(ss4),int(s4))
        db = Dbhelper()
        db.saveMarks(sref4)
        print(c8)

        st9="Ninth"
        c9.append(st9)
        e5 = nie.get()
        c9.append(e5)
        m5 = nim.get()
        c9.append(m5)
        h5 = nih.get()
        c9.append(h5)
        p5 = nip.get()
        c9.append(p5)
        ss5 = nia.get()
        c9.append(ss5)
        s5 = eisc.get()
        c9.append(s5)
        sref5 = Students(0, int(e5), int(m5), int(h5), int(p5), int(ss5), int(s5))
        db = Dbhelper()
        db.saveMarks(sref5)
        print(c9)

        st10= "Tenth"
        c10.append(st10)
        e6 = tee.get()
        c10.append(e6)
        m6 = tem.get()
        c10.append(m6)
        h6 = teh.get()
        c10.append(h6)
        p6 = tep.get()
        c10.append(p6)
        ss6= tea.get()
        c10.append(ss6)
        s6 = tesc.get()
        c10.append(s6)
        sref6 = Students(0, int(e6), int(m6), int(h6), int(p6), int(ss6), int(s6))
        db = Dbhelper()
        db.saveMarks(sref6)
        print(c10)

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
l1 =[]
l2 =[]
l3=[]
l4 =[]
l5=[]
def Activity():
    def onClick():
        a1 = act1.get()
        l1.append(a1)
        go1 = g1 .get()
        l1.append(go1)
        si1 = s1 .get()
        l1.append(si1)
        br1 = b1 .get()
        l1.append(br1)
        aref = activity (a1,go1,si1,br1)
        db = Dbhelper2()
        db.saveActivity(aref)

        a2 = act2.get()
        l2.append(a2)
        go2 = g2.get()
        l2.append(go2)
        si2 = s2.get()
        l2.append(si2)
        br2 = b2.get()
        l2.append(br2)
        aref1 = activity(a2, go2, si2, br2)
        db = Dbhelper2()
        db.saveActivity(aref1)

        a3 = act3.get()
        l3.append(a3)
        go3 = g3.get()
        l3.append(go3)
        si3 = s3.get()
        l3.append(si3)
        br3 = b3.get()
        l3.append(br3)
        aref3 = activity(a3, go3, si3, br3)
        db = Dbhelper2()
        db.saveActivity(aref3)

        a4 = act4.get()
        l4.append(a4)
        go4 = g4.get()
        l4.append(go4)
        si4 = s4.get()
        l4.append(si4)
        br4 = b4.get()
        l4.append(br4)
        aref4 = activity(a4, go4, si4, br4)
        db = Dbhelper2()
        db.saveActivity(aref4)

        a5 = act5.get()
        l5.append(a5)
        go5 = g5.get()
        l5.append(go5)
        si5 = s5.get()
        l5.append(si5)
        br5 = b5.get()
        l5.append(br5)
        aref5 = activity(a5, go5, si5, br5)
        db = Dbhelper2()
        db.saveActivity(aref5)


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
Activity()


