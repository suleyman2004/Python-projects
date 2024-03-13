d=int(input("Input number of days:"))
h=int(input("Input number of hours:"))
print("1-to calculate the total number of seconds or")
print("2-to calculate the total number of minutes:")
c=int(input("Enter your selected choice:"))
if c==1:
    total=d*24*60*60+h*60*60
    print("-------------")
    print("The total number of seconds are ",total)
elif c==2:
    total=d*24*60+h*60
    print("-------------")
    print("The total number of minutes are ",total)
else:
    print("error")

