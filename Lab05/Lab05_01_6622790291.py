b=0
c=0
for i in range(5):
    a=int(input("enter a number:"))
    if a%2==0:
        b=b+1
    elif a%2==1:
        c=c+1
print("there were ",b," even number")
print("there were ",c," odd number")
