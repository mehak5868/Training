a =[12,43,23,67,34,10]
a.sort()
print(a)

def takesecond(elem):
    return elem[1]
b =[(2,2),(3,4),(7,1)]
print(b)
for c in b:
    print(c)
b.sort(key=takesecond)
print(b)


class Student:

    def __init__(self, roll, name, phone, email, std):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.email = email
        self.std = std

    def showStudent(self):
        print("===",self.roll,"===")
        print(self.name,self.phone,self.email,self.std)
        print("=============")




students = []
reply = "yes"

while reply == "yes":

    print("==========Add Student Details ============")
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    std = int(input("Enter Standard: "))

    s = Student(roll,name,phone,email,std)

    students.append(s)

    reply = input("Would You like to add another Student ?")

for s in students:
    s.showStudent()

a = input("Show details in ascending order of roll no. or std (rolln/std):")
if a == "rolln":

