print("Multiplication table:")
a=int(input("Please eter a number between 1 to 25:"))
print("Multiplication table",a)
if (a>0) and (a<=25):
    for i in range(12):
        print("%d * %d=%d" %(a,(i+1),(a*(i+1))))
else:
    print("You entered invalid number")
