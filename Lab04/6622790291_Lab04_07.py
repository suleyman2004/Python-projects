a=int(input("Enter money you have:"))
b=int(input("Enter price of item:"))
c=int(input("Tax:"))
total_price=b+c
print("Total price",total_price)
if total_price<=a:
    print("yes you have enough money to buy")
elif total_price>a:
    print("You have shortfall of ",total_price-a,",you cannot buy")
else:
    print("error")
