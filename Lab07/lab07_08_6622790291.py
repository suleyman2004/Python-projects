even=0
odd=0
while True:
    a=float(input("Enter an integer (0 to exit):"))
    if a==0:
        break
    elif a%2==0:
        even+=1
    elif a%2==1:
        odd+=1
print("The number of even integers is ",even)
print("The number of odd integers is ",odd)