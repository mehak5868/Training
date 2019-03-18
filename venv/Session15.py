lm = lambda a =1 : a*a
print ("Result :",lm(45))

#==================================

l = [ 1,2,3,4,5,6]
lm1 =lambda a : a*a
result = map(lm1 , l)
print("Result 1:",list(result) )

#=====================================

l1=[11,22,33,44,55,66,77,88,99 ]
l2 =[10,20,30,40,50,60,70,80,90,100]
lm2= lambda x,y : x+y
result = map(lm2 , l1 , l2)
print("Result 2:", list(result))

#========================================

lm3 = lambda n : n%2 == 0
result = map(lm3, l2 )
print("Result 3:", list (result))
result = map(lm3, l1 )
print("Result 4:", list (result))
result = filter(lm3 , l2)
print("Result 5:", list (result))
result = filter(lm3, l1 )
print("Result 6:", list (result))

#===========================================

lm4 = lambda c , d : c+d
from functools import reduce
result = reduce(lm4, l2)
print("Result 7:",result)


l1 = [{"id":101, "name": "Alice" , "salary":10000},
      {"id":102, "name": "Alice" , "salary":20000},
      {"id":103, "name": "Alice" , "salary":30000},
      ]
lm5 = lambda em : em ["id"]
result = map(lm5 , l1)
print("Result 8:",list(result))


l3 = [10,11,12]
lm6 = lambda em , n : em["salary"] + (em["salary"] * (n/100))
result = map(lm6 , l1 , l3)
print("Result 9:",list(result))


lm6 = lambda em , n  : em["salary"] + (em["salary"] * (n/100))
result = map(lm6 , l1 , l3)
print("Result 10:",list(result))

