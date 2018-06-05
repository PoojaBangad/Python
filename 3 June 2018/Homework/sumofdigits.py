#Accept the number from user and print
#1.)sum of the digits
#2.)calculate sum of the number till single digit is sum
#3.)even digit and odd digit sum without arithematic operator


def evenoddsum(x):
    sumodd=0
    sumeven=0
    while x:
        r=x%10
        x/=10
        if r&1==1:
            sumodd+=r
        else:
            sumeven+=r
    print("Sum of odd digits = %d \n Sum of even digits =%d"%(sumodd,sumeven))
        
def singledigit(num):
    x=num
    while num>10:
        sum=0
        while num:
            r=num%10
            num/=10
            sum+=r
        num=sum
    print("Single digit sum of %d is %d "%(x,sum))

def sumdigit(x):
    sum=0
    num=x
    while x:
        r=x%10
        x/=10
        sum+=r
    print("Sum of digits of %d = %d "%(num,sum))
    if sum>=10:
        singledigit(sum)
    
if __name__=='__main__':
    x=input("Enter number")
    sumdigit(x)
    evenoddsum(x)
