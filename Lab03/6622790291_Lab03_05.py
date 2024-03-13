import math as m
d=float(input("Enter the sphere diameter:"))
r=d/2
V=(4/3)*m.pi*m.pow(r,3)
A=4*m.pi*m.pow(r,2)
print("The length of the sphere radius is %.4f" %(r))
print("The sphere volume and the surface area are %.4f and %.4f" %(V,A))
