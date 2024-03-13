def RightRotate(z=list):
    for i in range(x-1):
        y=z.pop(0)
        z.append(y)
    return z
def LeftRotate(z=list):
    for i in range(x+1):
        y=z.pop(4)
        z.insert(0,y)
    return z
# def LeftRotate(x=list)
list1=input("enter 5 inputs:").split()
if len(list1)==5:
    x=float(input("enter integer number of rotations (0-4)"))
    if x==int(x) and x>0 and x<4:
        x=int(x)
        print("Right rotated list: ",RightRotate(list1))
        print("Left rotated list",LeftRotate(list1))
    else:
        print("Error")
else:
    print("Error")
