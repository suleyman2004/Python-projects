import math as m
d=float(input("Enter the distance to the building:"))
a=float(input("Enter the elevation angle in degree:"))
h=d*m.tan(m.radians(a))
print("The building height is %.4f" %(h))
