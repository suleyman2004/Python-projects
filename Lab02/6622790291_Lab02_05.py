number=int(input("Enter a four-digit integer:"))
a=number//100
b=number%100
print("The result of %d + %d = %d" %(a,b,a+b))
print("The result of %d - %d = %d" %(a,b,a-b))
print("The integer value of %d / %d = %d" %(a,b,a//b))
print("The remainder of %d / %d = %d" %(a,b,a%b))
