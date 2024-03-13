purchase=0
item=0
while True:
    a=input("Enter item price or -1 when finished:")
    if a=="-1":
        break
    else:
        purchase+=float(a)
        item+=1
print("Your total amount purchase is",purchase)
payment=float(input("Your payment:"))
print("You bought %d items today" %item)
print("Your change is %.2f baht" %(payment-purchase))



