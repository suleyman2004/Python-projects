a=int(input("enter no. of lines:"))

if a>1:
    if a%2==0:
        for i in range(a//2):
            print("-"*(i+1))
            print("*"*(i+2))
    elif a%2==1:
        for i in range((a-1)//2):
            print("-"*(i+1))
            print("*"*(i+2))
        print("-"*a)
else:
    print("Error")
        
