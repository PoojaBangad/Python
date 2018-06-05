#Accept heterogenous variable number of arguments  and return sum of digits in it

def sumofint(*args):
    sum=0
    for x in args:
        if isinstance(x,int):
            sum+=x
        
    print("Sum of all the digits in given tupple is %d"%(sum))


if __name__=='__main__':
    sumofint(1,2,"Hello",7,9,"bye")
