
i=1
a=0
def fib():
    global i
    global a
    b= a+i
    print(b)
    a=i
    i=b

    if i<=20:

        fib()
fib()






"""i = 1
a=5
def fict():
    global i
    global a
    b=i*a
    print(b)
    a=b
    i=i+1
    if(i=>5):
        fict()

fict()
"""