from Session19 import *
from Session18as import *
def points(phone):
    def fetch(phone):
        amount=eamount.get()
        sql = "select point from customer where phone ='{}'".format(phone)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        if amount >= 800:
            #reply = input("Would u like to use ur points :")
            choice()
            """q=eq.get()
            if eq == "yes":
                a = int(input("How much points would u like to use:"))
                b = amount - a
                print("Total Amount :", b)
                point = row[0] + (amount * (10 / 100)) - a
                print("Points :", point)
                dbhelper = Dbhelper()
                dbhelper.FetchAmount(point, phone)"""
        else:
            point = row[0] + (amount * (10 / 100))
            print("Points :", point)
            dbhelper = Dbhelper()
            dbhelper.FetchAmount(point, phone)

    window = Tk()

    lamount=Label(window,text="Amount:")
    lamount.pack()

    eamount=Entry(window)
    eamount.pack()

    lnext=Button(window,text="Next",command=fetch)
    lnext.pack()
    """q=Label(window,text="Would u like to use points :")
    q.pack()
    
    eq=Entry(window)
    eq.pack()"""

    window.mainloop()

def choice ():
    def yn():
        def pointsupdate():
            point = epoint.get()

        window = Tk()

        lpoint = Label(window, text="Points")
        lpoint.pack()

        epoint = Entry(window)
        epoint.pack()

        ldone = Button(window, text="Done", command=pointsupdate)
        ldone.pack()
        window.mainloop()

    window =Tk()
    q=Label(window,text="Would u like to use points :")
    q.pack()

    eq=Button(window,text="yes",command=yn)
    eq.pack()

    eq = Button(window, text="no" )
    eq.pack()

    window.mainloop()