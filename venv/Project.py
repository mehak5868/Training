import mysql.connector
#from Project1 import *
global phone
global reciever
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
        print("Name:",self.name)
        print("Phone:",self.phone)
        print("Address:",self.address)

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
        #row = cursor.fetchone()
        #vref = Wallet(row[0], row[1], row[2], row[3], row[4], row[5])
        #vref.details()


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

def withdrawMoney(phone):
    sql = "select amount from wallet where phone='{}' ".format(phone)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    #reply = input("would u like to add ur money :")
    #if reply == "yes":
    a = int(input("how much money would u like to save in wallet:"))
    amount = row[0] - a
    print("Current Balance :", amount)
    db = DataBase()
    db.updateAmount(amount, phone)

def AddCustomer():
    name=input("Enter ur name :")
    phone =input("enter phone number :")
    address=input("Enter adress :")
    age=int(input("Enter age :"))
    amount=int(input("Enter amount :"))
    wref=Wallet(1,name,phone,address,age,amount)
    db=DataBase()
    db.saveDetails(wref)

def transferMoney( reciever):
    reciever=int(input("Reciever's Phone number :"))
    #a = int(input("How much would u like to transfer :"))
    #sql ="select * from wallet "
    sql1 ="select * from wallet where phone='{}'".format(reciever)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
    cursor = con.connect()
    cursor.execute(sql1)
    global transferRow
    transferRow = cursor.fetchone()
    vref = Wallet(transferRow[0], transferRow[1], transferRow[2], transferRow[3], transferRow[4], transferRow[5])
    vref.details()

    """if reciever is not None:
        sql2="select amount from wallet where phone='{}'".format(reciever)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="wallet")
        cursor = con.connect()
        cursor.execute(sql2)
        row = cursor.fetchone()
        amount = row[0] + a
        print("Current Balance :", amount)
        db = DataBase()
        db.updateAmount(amount, reciever)

    else :
        print("This phone Number is not found !!! ")
        Again()"""

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
        transferMoney( reciever)


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
        print("doesnot exist")
        AddCustomer()

process()



