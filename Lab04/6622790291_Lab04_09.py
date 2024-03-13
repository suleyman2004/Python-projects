a=int(input("Input parking time (in minutes):"))
price=a//60*20
if a%60>15:
    price=price+1*20
print("The charge is ",price," baht")
