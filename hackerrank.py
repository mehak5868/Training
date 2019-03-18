""""
n = int(input("Enter the value:"))
if n%2 !=0 or n in range(6,21) :
    print("Weird")
else:
    print("Not Weird")


a = int(input())
b = int(input())
c=a//b
d=a/b
print(c)
print(d)

n = int(input())
for i in range(0,n):
    print(i ** 2)"""

"""
def is_leap(year):
    leap = False
    if year % 400 == 0:
       return True
    elif year %100==0:
        return False
    elif year %400==0:
        return True
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap


year = int(input())
print(is_leap(year))"""
"""
var = 1
var1 = 2
var2= 3
b =[var,var1,var2]
for a in b :
    print(a,end="")"""
"""

a=int(input())
for i in range (1 , a+1) :
    print(i, end="")

name = input("Enter Your Name: ")
print(name)
data = "\u0905 {} is {} years old and lives in {} and earns \u20b9 30000".format(name, 30, "Redwood Shores")
print(data)



def print_full_name(a, b):
    c = "Hello  {} {} ! You just delved into python.". format(a , b)
    print(c)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


string = "abracadabra"
print(string)
l = list(string)
l[5] = 'k'
string = ''.join(l)
print (string)

string = string[:5] + "k" + string[6:]
print (string)"""


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)