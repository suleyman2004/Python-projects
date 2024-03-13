a=int(input("Please specify amount of money you would like to withdraw:"))
print("we may give you")
five_h=a//500
hundred=a%500//100
fifty=a%500%100//50
two=a%500%100%50//2
one=a%500%100%50%2//1
print(five_h," bill(s) of 500baht")
print(hundred," bill(s) of 100baht")
print(fifty," bill(s) of 50baht")
print(two," bill(s) of 2baht")
print(one," bill(s) of 1baht")
