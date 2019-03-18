#multi value container
#tuple
b=10,20,30,40 # homogeneous
d=10,20,30,40
print(b)
print(d)
print("hash code of b" , id(b))
print(" type of b" , type(b))
print("hash code of d" , id(d))
print("type of d" , type(d))

c=10 ,'helloo',2.3,5 #homogeneous
print(c ,type(c))
#list
b=[10,20,30,40]
print(b)
print(" type of b" , type(b))
print("hash code of b" , id(b))

#set
b={10,20,30,40}
print(b)
print(" type of b" , type(b))
print("hash code of b" , id(b))

#dictionary
students = {101:"john",102:"olive",103:"Alice"}
print(students)
print(type(students))
print(id(students))


