import numpy as np
def calculate(num1,num2):
    return np.sqrt(np.sum((num1-num2)**2))
x1,y1,z1=input("Input coordinate of P1: ").split()
x2,y2,z2=input("Input coordinate of P2: ").split()
x3,y3,z3=input("Input coordinate of P3: ").split()
x1,y1,z1=float(x1),float(y1),float(z1)
x2,y2,z2=float(x2),float(y2),float(z2)
x3,y3,z3=float(x3),float(y3),float(z3)
p1=np.array([x1,y1,z1])
p2=np.array([x2,y2,z2])
p3=np.array([x3,y3,z3])

dp1p2=calculate(p1,p2)
dp2p3=calculate(p2,p3)
dp3p1=calculate(p3,p1)
array=[dp1p2,dp2p3,dp3p1]
print("The longest distance= %.2f" %(max(array)))