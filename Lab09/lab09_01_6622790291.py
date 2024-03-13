import math
def CirArea(x):
    circle_area=math.pi*x*x
    return circle_area
def Sqarea(x):
    square_area=x*x
    return square_area
x=input("Input a positive number:")
if x.isnumeric:
    x=int(x)
    if  x>0:
        print("The area of the circle is %.2f" %CirArea(x))
        print("The area of the square is %.2f" %Sqarea(x))
    else:
        print("Wrong input")
else:
    print("Wrong input")

    
    