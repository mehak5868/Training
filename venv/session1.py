#single value container
#write operations
a=10
b=20

#read operations

print(a)

#update b
b=2.3
print(b)
#type operations
print(type(a))
print(type(b))

#hash code

d=10
print("hash code of a" , id(a))
print("hash code of d" , id(d))
print("hash code of a" , hex(id(a)))
print("hash code of a" ,oct(id(a)))
print("hash code of a" ,bin(id(a)))
print("hash code of b" ,id(b))

 #conversions

print("Binary of a :",bin(a))
print("Hexa of a :",hex(a))
print("Oct of a:",oct(a))

#string

hello = "how r u ??"
print(hello)
message = "Hello"\
          "how r u??"
print(message)
message= """this is awesome 
            u r really a good person"""
print(message)

businessname = 'john coffee cafe'
print(businessname)
message ='john\'s coffe cafe'
print(message)
businessname = r'john\'s coffe cafe'
print(businessname)

del a
del b

print(a)
print(b)