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

temp =0
for s in students:
    s.showStudent()
show = []
"""
def abc():
    global roll
    for b in len(students) :
        if students[b][Student(roll)] > students[b+1][Student(roll)] :
            temp = students[b][Student(roll)]
            students[b][Student(roll)]=students[b+1][Student(roll)]
            students[b + 1][Student(roll)]=temp
            show.append(students[b])

    print(show)


def hgf():
    global std
    for b in len(students):
        for c in range(b+1, c+b):
            if students[b][std] > students[c][std]:
                temp = students[b][std]
                students[b][std] = students[c][std]
                students[c][std] = temp
                show.append(students[b])
"""

a = input("Show details in ascending order of roll no. or std (rolln/std):")
if a == "rolln":

    def takefirst(elem):
        return elem[0]

    b=0
    for s in students:
        b=s.showStudent()
        b.sort(key=takefirst)
    print( b )
else:
    def takefirst(elem):
        return elem[ ]
    students.sort(key=takefirst( ))
    print( )