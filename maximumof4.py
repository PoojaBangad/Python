#!usr/bin/python

def maximum (x,y,z,p):
    if x>y and x>z and x>p :
        return x
    elif y>z and y>p :
        return y
    elif z>p :
        return z
    else :
        return p


if (__name__=='__main__') :

    no1,no2,no3,no4=input("Enter four numbers")
    result=maximum(no1,no2,no3,no4)
    print(result)
