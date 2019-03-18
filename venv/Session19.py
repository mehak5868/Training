from tkinter import *
from Session18as import *

def saveCustomer():
    def onClick():
        name = ename.get()
        phone = ePhone.get()
        age = eAge.get()
        address = eAddress.get()

        cref = Customer(0, name, phone, int(age), address, 10)
        dbhelper = Dbhelper()
        dbhelper.saveCustomerDetails(cref)

    window = Tk()

    lbTitle = Label(window,text="Add Customer Details :")
    lbTitle.pack()

    lbname = Label(window,text="Customer's Name :")
    lbname.pack()

    ename = Entry(window)
    ename.pack()

    lbPhone = Label(window,text="Phone Number :")
    lbPhone.pack()

    ePhone = Entry(window)
    ePhone.pack()

    lbage = Label(window ,text="Age :")
    lbage.pack()

    eAge = Entry(window)
    eAge.pack()

    laddress = Label(window , text="Address :")
    laddress.pack()

    eAddress= Entry(window)
    eAddress.pack()

    btAddCustomer = Button(window,text = "Add" ,command = onClick )
    btAddCustomer.pack()

    window.mainloop()