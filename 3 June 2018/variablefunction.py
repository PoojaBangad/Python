#variable functions Pass n number of arguments anytime, function should understand
#sum of any numbers passed
def add (*args):
    sum=0
    print(type(args)) #tuple is immutable container/array means whose content cannot be changed
    print("\nsum of ")
    for x in args :
        sum=sum+x
        print("%d "%(x))
        
    return sum


if __name__=='__main__':
    result=add(1,7,14,20,108,130)
    print(result)
    result=add(1)
    print(result)
