#understanding Dictionary kwargs and args together


def demo(a,b,*args,**kwargs):
    print(type(a))
    print(type(b))
    print(type(args))
    print(type(kwargs))

    print("printing args")
    for x in args:
          print(x)
    print("printing dict")         
    for x in kwargs:
          print(x,kwargs[x]) #key value pair . x is key kwargs[x] is value of that x in dictionary


if __name__=='__main__':
    demo(1,2,3,4,5,name='pooja',hobby='drawing',stay='pune',number=2)
    demo(1,2)#possible as args and kwargs are like default
