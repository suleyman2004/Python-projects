a=int(input("Enter an integer number (n>0):"))
total_fac=1
total_sum=0
if a>0:
    print("(1) Factorial of n (n!)")
    print("(2) Summation of n integers")
    b=int(input("Select opreation:"))
    if b==1:
        for i in range(0,a-1,1):
            total_fac=total_fac*(a-i)
        print(total_fac)
    elif b==2:
        for i in range(a+1):
            total_sum=total_sum+i
        print(total_sum)
else:
    print("N/A operation!")
        
