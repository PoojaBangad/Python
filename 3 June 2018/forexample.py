import math

def example1():
    for x in range (1,100):
        print(x)
        if x % 11==0:
            pass
    else :
        print("In else")

def example2():
    for x in range (1,100):
        print(x)
        if x % 11==0:
            break
    else :/Users/tejaskulkarni/Documents/pooja/variablefunction.py
        print("In else")

def prime(no):
    flag=0
    if no%2!=0:
        for x in range(3,int(no//2),2):
            if no%x==0:
                break
        else :
            flag=1

    return flag

def primesqrt(no):
    flag=0
    if no==2:
        flag=1
    elif no%2!=0:
        for x in range(3,sqrt(no),2):
            if no%x==0:
                break
        else :
            flag=1

    return flag

def notfive():
    for x in range(1,100):
        if x%5==0:
            continue
        print(x)



if (__name__=='__main__'):

    result=prime(2)
    print(result)
 #   notfive()
    
