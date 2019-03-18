import mysql.connector
#from Session19 import *
global phone
global amount
class Customer:
    def __init__(self, cid, name, phone, age, address,point):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address
        self.point=point

    def showDetails(self):
        print("===",self.cid ,"|",self.name,"====")
        print("Name :",self.name)
        print("phone :", self.phone)
        print("age :", self.age)
        print("address :" , self.address)
        print("Point:",self.point)

class Dbhelper:
    def saveCustomerDetails(self,cref):
        sql = "insert into Customer values (null,'{}','{}','{}','{}',10)".format(cref.name,cref.phone,cref.age,cref.address )
        con = mysql.connector.connect(user = "root",password ="" , host ="127.0.0.1" , database ="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Saved")

    def FetchDetails(self):
        phone=input("Enter the phone number")
        sql = "select * from customer where phone ='{}' ".format(phone )
        con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        cref = Customer(row[0], row[1], row[2], row[3], row[4],row[5])
        cref.showDetails()



    def FetchAmount(self ,point , phone):
        sql = "update customer set point='{}'where phone='{}'".format(point, phone)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Thank u for Shopping:)")

def FetchPoints(phone):
    #amount = int(input("Enter the amount :"))
    sql = "select point from customer where phone ='{}'".format(phone)
    con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
    cursor = con.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()

    if amount >=800:
        reply = input("Would u like to use ur points :")
        if reply == "yes":
            a = int(input("How much points would u like to use:"))
            b=amount-a
            print("Total Amount :",b)
            point = row[0] + (amount * (10 / 100))-a
            print("Points :", point)
            dbhelper = Dbhelper()
            dbhelper.FetchAmount(point ,phone)
    else :
        point = row[0] + (amount * (10 / 100))
        print("Points :", point)
        dbhelper= Dbhelper()
        dbhelper.FetchAmount(point,phone)


def addCustomer():
    print("=====Plz enter ur details :=====")
    name = input("Enter the name :")
    phone = input("enter the phone :")
    age = int(input("enter the age :"))
    address = input("enter the adress:")
    c = Customer(1, name, phone, age, address, 10)
    dbhelper = Dbhelper()
    dbhelper.saveCustomerDetails(c)




def process(phone) :
    #phone=input("Enter the phone number")
    sql = "select * from customer where phone ='{}' ".format(phone )
    con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pylearning")
    cursor = con.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()
    if row is not None :
        cref = Customer(row[0], row[1], row[2], row[3], row[4],row[5])
        cref.showDetails()
        FetchPoints(phone)

    else :
        addCustomer()

















