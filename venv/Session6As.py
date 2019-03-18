a=1
b=0
def brick(num):
    global a
    if a<=num:
        for i in range (1,num):
            b=b+i

            if b <= num :
                for c in range (2*i , i):
                    b=c



brick(13)




