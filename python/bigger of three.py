mark1=int(input("enter mark 1: "))
mark2=int(input("enter mark 2: "))
mark3=int(input("enter mark 3: "))
if (mark1>mark2 and mark1>mark3):
    if(mark2>mark3):
        print("m1 and m2 is bigger")
        print("the avg of both",(mark1+mark2)/2)
    else:
        print("m1 and m3 is bigger")
        print("the avg of both",(mark1+mark3)/2)
        
elif (mark2>mark3 and mark2>mark1):
    if(mark1>mark3):
        print("m2 and m1 is bigger")
        print("the avg of both",(mark2+mark1)/2)
    else:
        print("m2 nad m3 is bigger")
        print("the avg of both",(mark2+mark3)/2)
else:
    if(mark1>mark2):
        print("m3 and m1 is bigger")
        print("the avg of both",(mark3+mark1)/2)
    else:
        print("m3 and m2 is bigger")
        print("the avg of both",(mark3+mark2)/2)
