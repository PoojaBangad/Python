#understanding function arguments

#def fun(x,y=3,lb,ub,x=1): doesnt work default arguments must be trailing
def fun (x,y,lb,ub,z=1):
    print("x=%d,y=%d,lb=%d,ub=%d,z=%d"%(x,y,lb,ub,z))

if __name__=="__main__":
 #   fun(1,2,lb=2,ub=4,100)  Not allowed nonkeyword after keyword
    fun(1,2,ub=6,lb=7,z=7)#keyword matching it picks up
    fun(1,2,lb=3,ub=4,z=9)
    fun(1,2,3,4)#default arguments
   # fun(1,lb=2,ub=3)  cannot work
