
#check whether the number is armstrong number

def isspecial(x):
    sum=0
    while x:
        r=x%10
        x/=10
        sum+=(r**3)
    return sum



if __name__=='__main__':
    x=input("Enter the number: ")
    result=isspecial(x)
    if result==x:
        print("Number %d is speacial number"%(x))
    else:
        print("Number %d is not a speacial number"%(x))

