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
    def detailsInCsv (self):
        return "{},{},{},{},{},{},{},\n".format(self.standard,self.english,self.maths,self.hindi,self.punjabi,self.sst,self.sci)

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
    def detailsInCsv1 (self):
        return "{},{},{},{},{},\n".format(self.standard,self.english,self.maths,self.hindi,self.punjabi)
class Dbhelper1():
    def saveMarksPrimary(self,sref):
        sql = "insert into primacademics  values ({},{},{},{},{},{})".format(sref.standard, sref.english, sref.maths,sref.hindi, sref.punjabi, sref.evs)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
class activity:
    def __init__(self, activity, gold, silver, bronze):

        self.activity = activity
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    def detailsInCsv2 (self):
        return "{},{},{},{},\n".format(self.activity, self.gold, self.silver, self.bronze)

class  Dbhelper2():
    def saveActivity(self,cref):
        sql = "insert into activity values ('{}',{},{},{})".format(cref.activity, cref.gold, cref.silver, cref.bronze)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

class higherClass  :
    def __init__(self,subjects,eleven,twelve):
        self.subjects = subjects
        self.eleven = eleven
        self.twelve=twelve

class Dbhelper3():
    def saveMarks(self,href):
        sql = "insert into higherClass values ('{}',{},{})".format(href.subjects, href.eleven, href.twelve)
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="student")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

class higherClass1 :
    def __init__(self,standard,subject1,subject2,subject3,subject4,subject5):
        self.standard = standard
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4
        self.subject5 = subject5
    def detailsInCsv3 (self):
        return"{},{},{},{},{}".format(self.standard,self.subject1,self.subject2,self.subject3,self.subject4,self.subject5)




