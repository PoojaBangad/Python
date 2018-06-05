#default arguments multiplication

def multiply (no1,no2,no3=1,no4=1,no5=1):
    print("multiplication is : %d "%(no1*no2*no3*no4*no5))
def add (no1,no2,no3=0,no4=0,no5=0):
    print("Addition of %d %d %d %d %d : %d "%(no1,no2,no3,no4,no5,no1+no2+no3+no4+no5))



if __name__=='__main__':
 #   multiply(2,3)
#    multiply(2,3,4)
#    multiply(2,3,4,5)
#    multiply(2,3,4,5,6)
#    add(2,3)
#    add(2,3,4)
#    add(2,3,4,5)
#    add(2,3,4,5,6)
    add(no2=4,no1=2)
    add(1,2,no4=3,no3=5)  #default and keyword together
