import mysql.connector
#from Session36 import *
class Students:
    def __init__(self,id,standard,english,maths,hindi,punjabi,sst,sci):
        self.id=id
        self.standard=standard
        self.english=english
        self.maths=maths
        self.hindi=hindi
        self.punjabi=punjabi
        self.sst=sst
        self.sci=sci
    def detailsInCsv (self):
        return "null,{},{},{},{},{},{},{},\n".format(self.id,self.standard,self.english,self.maths,self.hindi,self.punjabi,self.sst,self.sci)

class Dbhelper:
    def saveMarks(self,sref):
        sql="insert into Academics values (null,{},{},{},{},{},{},{})".format(sref.id,sref.standard,sref.english,sref.maths,sref.hindi,sref.punjabi,sref.sst,sref.sci)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

class prime:
    def __init__(self,id,standard,english,maths,hindi,punjabi,evs):
        self.id =id
        self.standard=standard
        self.english=english
        self.maths=maths
        self.hindi=hindi
        self.punjabi=punjabi
        self.evs=evs
    def detailsInCsv1 (self):
        return "{},{},{},{},{},{},\n".format(self.id,self.standard,self.english,self.maths,self.hindi,self.punjabi)
class Dbhelper1():
    def saveMarksPrimary(self,sref):
        sql = "insert into primacademics  values (null,{},{},{},{},{},{})".format(sref.id,sref.standard, sref.english, sref.maths,sref.hindi, sref.punjabi, sref.evs)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
class activity:
    def __init__(self,id,activity , gold , silver , bronze):
        self.id=id
        self.activity=activity
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    def detailsInCsv2 (self):
        return "{},{},{},{},\n".format(self.id,self.activity,self.gold,self.silver,self.bronze)

class  Dbhelper2():
    def saveActivity(self,cref):
        sql = "insert into activity values (null,{},{},{},{})".format(cref.id,cref.activity, cref.gold, cref.silver,cref.bronze)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
