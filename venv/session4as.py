
def compare(i):
    sumEven = 0
    sumOdd = 0

    for a in range(1,i):
        if  a%2 != 0 :
            sumOdd = sumOdd + a
        else:
           sumEven = sumEven +a


    print("Sum of odd :", sumOdd)
    print("Sum of even :", sumEven)
    if sumEven > sumOdd:
        print("Sum of even is greater than Sum of odd ")
    else:
        print ("Sum of odd is greater than Sum of even" )

compare(i=int(input("enter the value:")))
"""
def compare(i):
    sumEven = 0
    sumOdd = 0
    whoisgreater=0
    for a in range(1, i):
        if a % 2!=0:
            sumOdd = sumOdd + a

        else:
            sumEven = sumEven + a
    print("Sum of odd :",sumOdd)
    print("Sum of even :",sumEven)
    if sumOdd > sumEven is False :
        whoisgreater = 1
    else:
        whoisgreater = 2
    return whoisgreater

result=compare(i=int(input("enter the value:")))
if result is  1:
    print("Sum of even is greater than Sum of odd")
else:
    print("Sum of odd is greater than Sum of even ")
"""

