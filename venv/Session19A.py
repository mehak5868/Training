from tkinter import *
from Session18as import *
from Session19 import *
from Session19B import *

def checkPhone ():
  phone = enumber.get()
  sql = "select * from customer where phone ='{}' ".format(phone)
  con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
  cursor = con.cursor()
  cursor.execute(sql)

  row = cursor.fetchone()
  if row is not None:
    cref = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
    cref.showDetails()
    #points(phone)
    def fetch():
      amount = int(eamount.get())
      sql = "select point from customer where phone ='{}'".format(phone)
      con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
      cursor = con.cursor()
      cursor.execute(sql)
      row = cursor.fetchone()
      print(row)

      def incr():
          point = row[0] + (amount * (10 / 100))
          print("Points :", point)
          dbhelper = Dbhelper()
          dbhelper.FetchAmount(point, phone)
      if amount >= 800:
          # reply = input("Would u like to use ur points :")
          def yn():
              def pointsupdate():
                  point = int(epoint.get())
                  b=amount-point
                  print(b)
                  point = row[0] + (amount * (10 / 100)) - point
                  print("Points :", point)
                  dbhelper = Dbhelper()
                  dbhelper.FetchAmount(point, phone)



              window = Tk()

              lpoint = Label(window, text="Points")
              lpoint.pack()

              epoint = Entry(window)
              epoint.pack()

              ldone = Button(window, text="Done", command=pointsupdate)
              ldone.pack()
              window.mainloop()

          window = Tk()
          q = Label(window, text="Would u like to use points :")
          q.pack()

          eq = Button(window, text="yes", command=yn)
          eq.pack()

          eq = Button(window, text="no",command=incr)
          eq.pack()

          window.mainloop()
      else :
          incr()

    window = Tk()

    lamount = Label(window, text="Amount:")
    lamount.pack()

    eamount = Entry(window)
    eamount.pack()

    lnext = Button(window, text="Next", command=fetch)
    lnext.pack()
    """q=Label(window,text="Would u like to use points :")
    q.pack()
  
    eq=Entry(window)
    eq.pack()"""

    window.mainloop()
  else:
    saveCustomer()


window =Tk()
plabel = Label(window , text = "Phone :",)
plabel.pack()

enumber=Entry(window)
enumber.pack()

btcheck=Button(window ,text="Check",command=checkPhone)
btcheck.pack()

window.mainloop()

