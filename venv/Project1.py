import mysql.connector
import datetime
global phone
global reciever
global date

"""def dateTime():
    global date
    date = datetime.datetime.today()"""

class Wallet :
    def __init__(self,id,name,phone,address,age,amount):
        self.id =id
        self.name=name
        self.phone=phone
        self.address=address
        self.age=age
        self.amount=amount
    def details(self):
        print("======",self.id,"|",self.name,"======")
        print("Phone:",self.phone)
        print("Age:",self.age)
        print("Address:", self.address)
        print("Balance:",self.amount)
    def showdetails(self):
        print("======", self.id, "|", self.name, "======")
        print("Balance:", self.amount)

class DataBase:
    def saveDetails(self,wref):
        sql= "insert into wallet values( null,'{}','{}','{}','{}','{}') ".format(wref.name,wref.phone,wref.address,wref.age,wref.amount)
        con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Saved")

    def displayDetails(self,phone):
        sql="selct * from wallet where phone ='{}'".format(phone)
        con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor=con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        vref = Wallet(row[0], row[1], row[2], row[3], row[4],row[5])
        vref.details()

    def  updateAmount(self,amount,phone):
        sql = "update wallet set amount='{}' where phone ='{}'".format(amount,phone)
        con =mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Updated")

    def addtransaction(self,phone,amount,date):
        sql="insert into transactions values ('{}','{}','Deposits','{}')".format(phone,amount,date)
        con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()

    def withdrawtransaction(self,phone,amount,date):
        sql="insert into transactions values ('{}','{}','Withdraw','{}')".format(phone,amount,date)
        con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()

    def transferTranscation(self,phone,amount,date):
        sql="insert into transactions values ('{}','{}','Transfer','{}')".format(phone,amount,date)
        con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
        cursor=con.cursor()
        cursor.execute(sql)
        con.commit()

def selectMoney(phone):
    sql="select amount from wallet where phone='{}' ".format(phone)
    con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="wallet")
    cursor=con.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    #reply = input ("would u like to add ur money :")
    #if reply=="yes":
    a=int(input("how much money would u like to save in wallet:"))
    amount=row[0]+a
    print("Current Balance :",amount)

    db = DataBase()
    db.updateAmount(amount,phone)
    aaddtransaction(phone,amount)

def withdrawMoney(phone):
    sql = "select amount from wallet where phone='{}' ".format(phone)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    #reply = input("would u like to add ur money :")
    #if reply == "yes":
    a = int(input("how much money would u like to save in wallet:"))
    if a<row[0] and row[0]>1000:
        amount = row[0] - a
        print("Current Balance :", amount)
        db = DataBase()
        db.updateAmount(amount, phone)
        date = datetime.datetime.today()
        print(date)
        db.withdrawtransaction(phone,amount,date)
    else :
        print("Invalid Balance")
        Again()

def AddCustomer():
    name=input("Enter ur name :")
    phone =input("enter phone number :")
    address=input("Enter adress :")
    age=int(input("Enter age :"))
    amount=int(input("Enter amount :"))
    wref=Wallet(1,name,phone,address,age,amount)
    db=DataBase()
    db.saveDetails(wref)
    process()

def fetchamount(phone):
    sql = "select * from wallet where phone ='{}'".format(phone)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
    cursor = con.cursor()
    cursor.execute(sql)
    global row
    row = cursor.fetchone()

def tranferamount(reciever):
    sql = "select * from wallet where phone ='{}'".format(reciever)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
    cursor = con.cursor()
    cursor.execute(sql)
    global trow
    trow = cursor.fetchone()

def updateCustomerTransfer(amount,phone,reciever):
    balance = row[5] - amount
    balance2 = trow[5] + amount
    dbhelp = DataBase()
    dbhelp.updateAmount(balance, phone)
    dbhelp.updateAmount(balance2, reciever)


def transferMoney( phone):
    reciever=input("Phone Number :")
    amount=int(input("Amount:"))
    fetchamount(phone)
    if amount > row[5] & amount < 1000:
        tranferamount(reciever)

        updateCustomerTransfer(amount,phone,reciever)
        taddtransaction(phone,amount)
        """date = datetime.datetime.today()
        print(date)
        db=DataBase()
        db.transferTranscation(phone,amount,reciever,date)"""

    else :
        print("Check ur current Balance")
        Again()

def taddtransaction(phone,amount):
    date = datetime.datetime.today()
    print(date)
    db = DataBase()
    db.transferTranscation(phone, amount, date)

def aaddtransaction(phone,amount):
    date=datetime.datetime.today()
    db=DataBase()
    db.addtransaction(phone,amount,date)

def waddtransaction(phone,amount):
    date = datetime.datetime.today()
    db = DataBase()
    db.addtransaction(phone, amount, date)


def Again ():
    print("=========================")
    print("1.Add Money")
    print("2.Withdraw Money")
    print("3.Transfer Money")
    print("=========================")
    b = int(input("Enter ur choice :"))
    if b == 1:
        selectMoney(phone)
    elif b == 2:
        withdrawMoney(phone)
    elif b == 3:
        transferMoney(phone)


def process():
    global phone
    phone = int(input ("Enter ur phone number :"))
    sql="select * from wallet where phone='{}'".format(phone)
    con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database ="wallet")
    cursor=con.cursor()
    cursor.execute(sql)
    row =cursor.fetchone()
    if row is not None:
        wref=Wallet(row[0],row[1],row[2],row[3],row[4],row[5])
        wref.details()
        Again()
    else:
        print("doesnot exist or enter a valid phone number")
        AddCustomer()

process()

