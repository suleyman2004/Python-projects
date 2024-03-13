import math as m
x1=float(input("Enter coordinate X for P1:"))
x2=float(input("Enter coordinate X for P2:"))
y1=float(input("Enter coordinate Y for P1:"))
y2=float(input("Enter coordinate Y for P2:"))

D=m.sqrt(m.pow(x1-x2,2)+m.pow(y1-y2,2))
C=D*m.pi
A=m.pow(D/2,2)*m.pi
print("The length of the circle diameter is %.4f" %(D))
print("The circle area and circumference are %.4f and %.4f" %(A,C))
