import mysql.connector

class Customer:
    def __init__(self, cid, name, phone, age, address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showDetails(self):
        print("===",self.cid ,"|",self.name,"====")
        print("Name :",self.name)
        print("phone :", self.phone)
        print("age :", self.age)
        print("address :" , self.address)

class DBHelper :
    def saveCustomerDetails(self , cref):
        sql = "insert into Customer values (null,'{}','{}','{}','{}')".format(cref.name,cref.phone,cref.age,cref.address)
        con = mysql.connector.connect(user = "root",password ="" , host ="127.0.0.1" , database ="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Saved")

    def UpdateCustomerDetails(self,cref):
        sql = "update Customer set name ='{}',phone ='{}',age ='{}',address='{}' where cid ='{}'".format(cref.name, cref.phone, cref.age,
                                                                              cref.address ,cref.cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>UPDATED")

    def DeleteCustomerDetails(self,cid):
        sql = "delete from Customer where cid ={}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Deleted")

    def FetchCustomerDetails(self):
        sql = "select * from Customer "
        con = mysql.connector.connect(user="root" ,password ="",host ="127.0.0.1", database="pylearning")
        cursor = con.cursor()
        cursor.execute(sql)

        #row = cursor.fetchone()
        #print(">>row :",row)

        row = cursor .fetchone()
        #print(">>row :", rows)
        #for row in rows :
            #print(row)
        cref = Customer (row[0],row[1],row[2],row[3],row[4])
        cref.showDetails()
        row = cursor.fetchone()
        cref = Customer(row[0], row[1], row[2], row[3], row[4])
        cref.showDetails()



cref = Customer(1,"john" , "+91 99999 88888" , 20 , "Redwood Shores")
cref1 = Customer(2,"Alice Watson " , "+91 978786 88887" , 21 , "Redwood Shores South")
cref2 = Customer (3,"Kim","9874564120",22,"Civil Lines")
#cref.showDetails()
#cref1.showDetails()
#cref.saveCustomerDetails()
#cref1.saveCustomerDetails()


dbhelper = DBHelper()

#dbhelper.saveCustomerDetails(cref2)
#dbhelper.UpdateCustomerDetails(cref1)
#dbhelper.DeleteCustomerDetails(3)
dbhelper.FetchCustomerDetails()

