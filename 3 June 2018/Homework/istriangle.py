#Accept 3 numbers from user and print wheter it forms a triangle
#Hint: sum of 2 sides > third

def istriangle(x,y,z):
    if (x+y)>z or (x+z)>y or (y+z)>x:
        return 1
    else:
        return 0

def type(x,y,z):
    if x==y==z:
        print("equilateral")
    elif x==y or y==z or x==z:
        print("Isoceles Triangle")
    else
        print("Scalene Triangle")

if __name__=='__main__':
    x,y,z=input("Enter three sides of triangle")
    result=istriangle(x=x,y=y,z=z)
    if result==1:
        print("The sides with lenghts %d %d %d  form a triangle "%(x,y,z))
        type(x,y,x)
    else:
        print("The sides with lenghts %d %d %d does not form a triangle "%(x,y,z))
