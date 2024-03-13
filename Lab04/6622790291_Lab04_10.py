print("Welcome to Income Tax Computation Program")
a=int(input("Please enter your income(THb):"))
tax=0
if (a<=15000) and (a>0):
    tax=0
    print("Tax exponse=",tax)
    total=a-tax
    print("Your net income after tax= ",total)
elif (a<=50000) and (a>0):
    tax=(a-15000)*0.05
    print("Tax exponse=",tax)
    total=a-tax
    print("Your net income after tax= ",total)
elif (a<=100000) and (a>0):
    tax=35000*0.05+(a-50000)*0.075
    print("Tax exponse=",tax)
    total=a-tax
    print("Your net income after tax= ",total)
elif (a>100000) and (a>0):
    tax=35000*0.05+50000*0.075+(a-100000)*0.1
    print("Tax exponse=",tax)
    total=a-tax
    print("Your net income after tax= ",total)
elif a<0:
    print("You are in debt")
else:
    print("error")

    
