from tkinter import *
from Session36A import *

def academicsWindow():
    def onClick():
        #st = 'First'

        eng1 = firstEng.get()

        math1 = firstMath.get()

        hindi1 = firstHindi.get()

        punjabi1 = firstPunjabi.get()

        evs1 = firstEvs.get()

        ref1 = prime(1, int(eng1), int(math1), int(hindi1), int(punjabi1), int(evs1))
        db = Dbhelper1()
        db.saveMarksPrimary(ref1)


        st2 = "Second"

        eng2 = secondEng.get()

        math2 = secondMath.get()

        hindi2 = secondHindi.get()

        punjabi2 = secondPunjabi.get()

        evs2 = secondEvs.get()

        ref2 = prime(2, int(eng2), int(math2), int(hindi2), int(punjabi2), int(evs2))
        db = Dbhelper1()
        db.saveMarksPrimary(ref2)


        st3 = "Third"

        eng3 = thirdEng.get()

        math3 = thirdMath.get()

        hindi3 = thirdHindi.get()

        punjabi3 = thirdPunjabi.get()

        evs3 = thirdEvs.get()

        ref3 = prime(3, int(eng3), int(math3), int(hindi3), int(punjabi3), int(evs3))
        db = Dbhelper1()
        db.saveMarksPrimary(ref3)
        a=prime("Stanard", "English" , "Maths" , "Hindi" ,"Punjabi","EVS")
        file = open("StudentData.csv","a")
        file.write(a.detailsInCsv1())
        file.write(ref1.detailsInCsv1())
        file.write(ref2.detailsInCsv1())
        file.write(ref3.detailsInCsv1())


        st4 = "Fourth"

        english4 = fourEng.get()

        maths4 = fourMath.get()

        hindi4 = fourHindi.get()

        punjabi4 = fourPunjabi.get()

        sst4 = fourSST.get()

        sci4 = fourSci.get()

        sref = Students(4,int(english4),int(maths4),int(hindi4),int(punjabi4),int(sst4),int(sci4))
        db = Dbhelper()
        db.saveMarks(sref)


        st5 ="Fifth"

        eng5 = fiveEng.get()

        math5 = fiveMath.get()

        hindi5 = fiveHindi.get()

        punjabi5 = fivePunjabi.get()

        sst5 = fivePunjabi.get()

        sci5 = fiveSci.get()

        sref1 = Students(5,int(eng5),int(math5),int(hindi5),int(punjabi5),int(sst5),int(sci5))
        db =Dbhelper()
        db.saveMarks(sref1)


        st6 ="Sixth"

        eng6 = sixEng.get()

        math6 = sixHindi.get()

        hindi6 = sixPunjabi.get()

        punjabi6 = sixPunjabi.get()

        sst6= sixSST.get()

        sci6 = sixSci.get()

        sref2 = Students(6,int(eng6),int(math6),int(hindi6),int(punjabi6),int(sst6),int(sci6))
        db=Dbhelper()
        db.saveMarks(sref2)


        st7 ="Seventh"

        eng7 = sevenEnglish.get()

        math7 = sevenMath.get()

        hindi7 = sevenHindi.get()

        punjabi7 = sevenPunjabi.get()

        sst7 = sevenSST.get()

        sci7 = sevenSci.get()

        sref3 =Students(7,int(eng7),int(math7),int(hindi7),int(punjabi7),int(sst7),int(sci7))
        db = Dbhelper()
        db.saveMarks(sref3)


        st8="Eighth"

        eng8 = eightEng.get()

        math8 = eightMath.get()

        hindi8 = eightHindi.get()

        punjabi8 =eightPunjabi.get()

        sst8 = eightSST .get()

        sci8 =  eightSci.get()

        sref4 = Students(8,int(eng8),int(math8),int(hindi8),int(punjabi8),int(sst8),int(sci8))
        db = Dbhelper()
        db.saveMarks(sref4)


        st9="Ninth"

        eng9 = nineEng.get()

        math9 = nineMath.get()

        hindi9 = nineHindi.get()

        punjabi9 = ninePunjabi.get()

        sst9 = nineSST.get()

        sci9 = nineSci.get()

        sref5 = Students(9, int(eng9), int(math9), int(hindi9), int(punjabi9), int(sst9), int(sci9))
        db = Dbhelper()
        db.saveMarks(sref5)


        st10= "Tenth"

        eng10 = tenEng.get()

        math10 = tenMath.get()

        hindi10 = tenHindi.get()

        punjabi10 = tenPunjabi.get()

        sst10= tenSST.get()

        sci10 = tenSci.get()

        sref6 = Students(10, int(eng10), int(math10), int(hindi10), int(punjabi10), int(sst10), int(sci10))
        db = Dbhelper()
        db.saveMarks(sref6)

        b = Students("Stanard", "English" , "Maths" , "Hindi" ,"Punjabi","SSt","Science" )
        file1 = open("StudentDataSec.csv","a")
        file1.write( b.detailsInCsv())
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

    firstEng = Entry(window)
    firstEng.grid(row=2, column=2)  # first class
    firstMath = Entry(window)
    firstMath.grid(row=2, column=3)
    firstHindi = Entry(window)
    firstHindi.grid(row=2, column=4)
    firstPunjabi = Entry(window)
    firstPunjabi.grid(row=2, column=5)
    firstEvs = Entry(window)
    firstEvs.grid(row=2, column=6)

    secondEng = Entry(window)
    secondEng.grid(row=3, column=2)  # second class
    secondMath = Entry(window)
    secondMath.grid(row=3, column=3)
    secondHindi = Entry(window)
    secondHindi.grid(row=3, column=4)
    secondPunjabi = Entry(window)
    secondPunjabi.grid(row=3, column=5)
    secondEvs = Entry(window)
    secondEvs.grid(row=3, column=6)
    # sa = Entry(window).grid(row=3, column=6)
    # ssc = Entry(window).grid(row=3, column=7)

    thirdEng = Entry(window)
    thirdEng.grid(row=4, column=2)  # third class
    thirdMath = Entry(window)
    thirdMath.grid(row=4, column=3)
    thirdHindi = Entry(window)
    thirdHindi.grid(row=4, column=4)
    thirdPunjabi = Entry(window)
    thirdPunjabi.grid(row=4, column=5)
    thirdEvs = Entry(window)
    thirdEvs.grid(row=4, column=6)


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



    fourEng =Entry(window)
    fourEng .grid(row=8,column = 2)# fouth class
    fourMath =Entry(window)
    fourMath.grid(row=8,column = 3)
    fourHindi =Entry(window)
    fourHindi.grid(row=8,column = 4)
    fourPunjabi =Entry(window)
    fourPunjabi.grid(row=8,column = 5)
    fourSST =Entry(window)
    fourSST.grid(row=8,column = 6)
    fourSci = Entry(window)
    fourSci.grid(row=8,column = 7)

    fiveEng =Entry(window)
    fiveEng.grid(row=9,column = 2) # fifth
    fiveMath =Entry(window)
    fiveMath.grid(row=9,column = 3)
    fiveHindi =Entry(window)
    fiveHindi.grid(row=9,column = 4)
    fivePunjabi =Entry(window)
    fivePunjabi.grid(row=9,column = 5)
    fiveSST =Entry(window)
    fiveSST   .grid(row=9,column = 6)
    fiveSci = Entry(window)
    fiveSci.grid(row=9,column = 7)

    sixEng =Entry(window)
    sixEng.grid(row=10,column = 2) #sixth
    sixMath =Entry(window)
    sixMath.grid(row=10,column = 3)
    sixHindi =Entry(window)
    sixHindi   .grid(row=10,column = 4)
    sixPunjabi =Entry(window)
    sixPunjabi.grid(row=10,column = 5)
    sixSST =Entry(window)
    sixSST.grid(row=10,column = 6)
    sixSci = Entry(window)
    sixSci.grid(row=10,column = 7)

    sevenEnglish =Entry(window)
    sevenEnglish.grid(row=11,column = 2)# seventh
    sevenMath =Entry(window)
    sevenMath.grid(row=11,column = 3)
    sevenHindi =Entry(window)
    sevenHindi.grid(row=11,column = 4)
    sevenPunjabi =Entry(window)
    sevenPunjabi.grid(row=11,column = 5)
    sevenSST =Entry(window)
    sevenSST.grid(row=11,column = 6)
    sevenSci = Entry(window)
    sevenSci.grid(row=11,column = 7)


    eightEng =Entry(window)
    eightEng.grid(row=12,column = 2) #eighth
    eightMath =Entry(window)
    eightMath.grid(row=12,column = 3)
    eightHindi =Entry(window)
    eightHindi.grid(row=12,column = 4)
    eightPunjabi =Entry(window)
    eightPunjabi.grid(row=12,column = 5)
    eightSST =Entry(window)
    eightSST.grid(row=12,column = 6)
    eightSci = Entry(window)
    eightSci.grid(row=12,column = 7)

    nineEng =Entry(window)
    nineEng.grid(row=13,column = 2) # ninth
    nineMath =Entry(window)
    nineMath   .grid(row=13,column = 3)
    nineHindi =Entry(window)
    nineHindi.grid(row=13,column = 4)
    ninePunjabi =Entry(window)
    ninePunjabi.grid(row=13,column = 5)
    nineSST =Entry(window)
    nineSST.grid(row=13,column = 6)
    nineSci = Entry(window)
    nineSci.grid(row=13,column = 7)

    tenEng =Entry(window)
    tenEng.grid(row=14,column = 2)   #tenth
    tenMath =Entry(window)
    tenMath.grid(row=14,column = 3)
    tenHindi =Entry(window)
    tenHindi.grid(row=14,column = 4)
    tenPunjabi =Entry(window)
    tenPunjabi.grid(row=14,column = 5)
    tenSST =Entry(window)
    tenSST.grid(row=14,column = 6)
    tenSci = Entry(window)
    tenSci.grid(row=14,column = 7)


    sub = Button(window,text="Submit",command =onClick).grid(row=15,column = 2)
    #fourth =Label(window , text = "Fourth:").grid(row = 4)
    window .mainloop()
#academicsWindow()

def Activity():
    def onClick():
        activity1 = activityEntry1.get()

        gold1 = goldEntry1 .get()

        silver1 = silverEntry1 .get()

        bronze1 = bronzeEntry1 .get()

        aref = activity (activity1,int(gold1),int(silver1),int(bronze1))
        db = Dbhelper2()
        db.saveActivity(aref)

        activity2 = activityEntry2.get()

        gold2 = goldEntry2.get()

        silver2 = silverEntry2.get()

        bronze2 = bronzeEntry2.get()

        aref1 = activity(activity2,int( gold2),int( silver2),int (bronze2))
        db = Dbhelper2()
        db.saveActivity(aref1)

        activity3 = activityEntry3.get()

        gold3 = goldEntry3.get()

        silver3 = silverEntry3.get()

        bronze3 = bronzeEntry3.get()

        aref3 = activity(activity3,int (gold3), int(silver3),int (bronze3))
        db = Dbhelper2()
        db.saveActivity(aref3)

        activity4 = activityEntry4.get()

        gold4 = goldEntry4.get()

        silver4 = silverEntry4.get()

        bronze4 = bronzeEntry4.get()

        aref4 = activity(activity4, int(gold4), int(silver4), int(bronze4))
        db = Dbhelper2()
        db.saveActivity(aref4)

        activity5 = activityEntry5.get()

        gold5 = goldEntry5.get()

        silver5 = silverEntry5.get()

        bronze5 = bronzeEntry5.get()

        aref5 = activity(activity5, int(gold5), int(silver5), int(bronze5))
        db = Dbhelper2()
        db.saveActivity(aref5)
        a = activity("Activity", "Gold", "Silver", "Bronze")
        file2 = open("sports.csv","a")
        file2.write(a.detailsInCsv2())
        file2.write(aref.detailsInCsv2())
        file2.write(aref1.detailsInCsv2())
        file2.write(aref3.detailsInCsv2())
        file2.write(aref4.detailsInCsv2())
        file2.write(aref5.detailsInCsv2())


    window =Tk()
    act = Label(window , text ="Activity")
    act.grid(row=6)

    gold = Label(window,text="Gold")
    gold.grid(row=6,column=2)

    silver = Label(window,text ="Silver")
    silver.grid(row=6,column=3)

    bronze = Label(window,text="Bronze")
    bronze.grid(row=6,column=4)

    activityEntry1 = Entry(window)
    activityEntry1.grid(row=7)

    goldEntry1 = Entry(window)
    goldEntry1.grid(row=7,column=2)

    silverEntry1 =Entry(window)
    silverEntry1.grid(row=7,column=3)

    bronzeEntry1 =Entry(window)
    bronzeEntry1.grid(row=7,column=4)

    activityEntry2 = Entry(window)
    activityEntry2.grid(row=8)

    goldEntry2 = Entry(window)
    goldEntry2.grid(row=8, column=2)

    silverEntry2 = Entry(window)
    silverEntry2.grid(row=8, column=3)

    bronzeEntry2 = Entry(window)
    bronzeEntry2.grid(row=8, column=4)

    activityEntry3 = Entry(window)
    activityEntry3.grid(row=9)

    goldEntry3 = Entry(window)
    goldEntry3.grid(row=9, column=2)

    silverEntry3 = Entry(window)
    silverEntry3.grid(row=9, column=3)

    bronzeEntry3 = Entry(window)
    bronzeEntry3.grid(row=9, column=4)

    activityEntry4 = Entry(window)
    activityEntry4.grid(row=10)

    goldEntry4 = Entry(window)
    goldEntry4.grid(row=10, column=2)

    silverEntry4 = Entry(window)
    silverEntry4.grid(row=10, column=3)

    bronzeEntry4 = Entry(window)
    bronzeEntry4.grid(row=10, column=4)

    activityEntry5 = Entry(window)
    activityEntry5.grid(row=11)

    goldEntry5 = Entry(window)
    goldEntry5.grid(row=11, column=2)

    silverEntry5 = Entry(window)
    silverEntry5.grid(row=11, column=3)

    bronzeEntry5 = Entry(window)
    bronzeEntry5.grid(row=11, column=4)

    sub= Button (window,text = "Submit",command=onClick)
    sub.grid(row = 12,column =2)


    window.mainloop()
#Activity()

def Sports():
    def onClick():
        activity1 = activityEntry1.get()

        gold1 = goldEntry1.get()

        silver1 = silverEntry1.get()

        bronze1 = bronzeEntry1.get()

        aref = activity(str(activity1), int(gold1), int(silver1), int(bronze1))
        db = Dbhelper2()
        db.saveActivity(aref)

        activity2 = activityEntry2.get()

        gold2 = goldEntry2.get()

        silver2 = silverEntry2.get()

        bronze2 = bronzeEntry2.get()

        aref1 = activity(str(activity2), int(gold2), int(silver2), int(bronze2))
        db = Dbhelper2()
        db.saveActivity(aref1)

        activity3 = activityEntry3.get()

        gold3 = goldEntry3.get()

        silver3 = silverEntry3.get()

        bronze3 = bronzeEntry3.get()

        aref3 = activity(str(activity3), int(gold3), int(silver3), int(bronze3))
        db = Dbhelper2()
        db.saveActivity(aref3)

        activity4 = activityEntry4.get()

        gold4 = goldEntry4.get()

        silver4 = silverEntry4.get()

        bronze4 = bronzeEntry4.get()

        aref4 = activity(str(activity4), int(gold4), int(silver4), int(bronze4))
        db = Dbhelper2()
        db.saveActivity(aref4)

        activity5 = activityEntry5.get()

        gold5 = goldEntry5.get()

        silver5 = silverEntry5.get()

        bronze5 = bronzeEntry5.get()

        aref5 = activity(str(activity5), int(gold5), int(silver5), int(bronze5))
        db = Dbhelper2()
        db.saveActivity(aref5)

        a = activity ("Sports","Gold","Silver","Bronze")
        file3 =open("activity.csv","a")
        file3 .write(a.detailsInCsv2())
        file3.write(aref.detailsInCsv2())
        file3.write(aref1.detailsInCsv2())
        file3.write(aref3.detailsInCsv2())
        file3.write(aref4.detailsInCsv2())
        file3.write(aref5.detailsInCsv2())
        file3.close()

    window=Tk()

    act = Label(window, text="Sports")
    act.grid(row=6)

    gold = Label(window, text="Gold")
    gold.grid(row=6, column=2)

    silver = Label(window, text="Silver")
    silver.grid(row=6, column=3)

    bronze = Label(window, text="Bronze")
    bronze.grid(row=6, column=4)

    activityEntry1 = Entry(window)
    activityEntry1.grid(row=7)

    goldEntry1 = Entry(window)
    goldEntry1.grid(row=7, column=2)

    silverEntry1 = Entry(window)
    silverEntry1.grid(row=7, column=3)

    bronzeEntry1 = Entry(window)
    bronzeEntry1.grid(row=7, column=4)

    activityEntry2 = Entry(window)
    activityEntry2.grid(row=8)

    goldEntry2 = Entry(window)
    goldEntry2.grid(row=8, column=2)

    silverEntry2 = Entry(window)
    silverEntry2.grid(row=8, column=3)

    bronzeEntry2 = Entry(window)
    bronzeEntry2.grid(row=8, column=4)

    activityEntry3 = Entry(window)
    activityEntry3.grid(row=9)

    goldEntry3 = Entry(window)
    goldEntry3.grid(row=9, column=2)

    silverEntry3 = Entry(window)
    silverEntry3.grid(row=9, column=3)

    bronzeEntry3 = Entry(window)
    bronzeEntry3.grid(row=9, column=4)

    activityEntry4 = Entry(window)
    activityEntry4.grid(row=10)

    goldEntry4 = Entry(window)
    goldEntry4.grid(row=10, column=2)

    silverEntry4 = Entry(window)
    silverEntry4.grid(row=10, column=3)

    bronzeEntry4 = Entry(window)
    bronzeEntry4.grid(row=10, column=4)

    activityEntry5 = Entry(window)
    activityEntry5.grid(row=11)

    goldEntry5 = Entry(window)
    goldEntry5.grid(row=11, column=2)

    silverEntry5 = Entry(window)
    silverEntry5.grid(row=11, column=3)

    bronzeEntry5 = Entry(window)
    bronzeEntry5.grid(row=11, column=4)

    BUTTON= Button(window, text = "Submit", command = onClick)
    BUTTON.grid(row = 12 , column = 3)

    window.mainloop()

#Sports()
academicsWindow()

