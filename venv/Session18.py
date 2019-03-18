import mysql.connector



class Customer():
    def __init__(self, cid, name,phone, age, address,point):
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
        print("Points:",self.point)

class Buyer():
    def __init__(self,phone,amount):
        self.phone = phone
        self.amount=amount

    def ShowBuyersDetails(self):
        print("Amount:",self.amount)
        print("Phone:",self.phone)

class DBHelper:
    def saveCustomerDetails(self,cref):
        sql = "insert into Customer values (null,'{}','{}','{}','{}',10)".format(cref.name,cref.phone,cref.age,cref.address )
        con = mysql.connector.connect(user = "root",password ="" , host ="127.0.0.1" , database ="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Saved")

    """
     def FetchCustomerdetails(self):
        sql = "select * from customer where phone ='{}' ".format(phone )
        con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows :
            cref = Customer (row [0],row[1],row[2],row[3],row[4],row[5])
            cref.showDetails()

phone = input ("Enter the phone number :")
price = input("Enter the shopping amount :")

#c=Buyer(phone,price)
#c.ShowBuyersDetails()

#c=Customer(101,"alice",984216336,20,"redwoodshore",10)
#c.showDetails()

name = input("Enter the name :")
phone = input("enter the phone :")
age = int(input("enter the age :"))
address = input("enter the adress:")
c = Customer(1,name,phone,age,address,10)

dbhelper = DBHelper()
dbhelper.FetchCustomerdetails()
"""
phone = input("enter the phone :")
sql = "select * from customer where phone ='{}'".format(phone)
con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pylearning")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()
cref = Customer (row[0],row[1],row[2],row[3],row[4],row[5])
cref.showDetails()

sql1="select point from customer where phone ='{}'".format(phone)
con = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="pylearning")
cursor = con.cursor()
cursor.execute(sql)
row = cursor.fetchone()



"""def inc(amount):
    point = +(amount*5/100)
    print(point)

a = int(input("enter amount"))
inc(a)"""





