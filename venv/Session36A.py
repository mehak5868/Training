import mysql.connector
#from Session36 import *
class Students:
    def __init__(self,standard,english,maths,hindi,punjabi,sst,sci):
        self.standard=standard
        self.english=english
        self.maths=maths
        self.hindi=hindi
        self.punjabi=punjabi
        self.sst=sst
        self.sci=sci
class Dbhelper:
    def saveMarks(self,sref):
        sql="insert into Academics values ({},{},{},{},{},{},{})".format(sref.standard,sref.english,sref.maths,sref.hindi,sref.punjabi,sref.sst,sref.sci)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

class prime:
    def __init__(self,standard,english,maths,hindi,punjabi,evs):
        self.standard=standard
        self.english=english
        self.maths=maths
        self.hindi=hindi
        self.punjabi=punjabi
        self.evs=evs

class Dbhelper1():
    def saveMarksPrimary(self,sref):
        sql = "insert into primacademics  values ({},{},{},{},{},{})".format(sref.standard, sref.english, sref.maths,sref.hindi, sref.punjabi, sref.evs)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
