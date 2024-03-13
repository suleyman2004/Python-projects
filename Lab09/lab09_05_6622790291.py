def SeatType():
    while True:
       a=input("Select the seat type (P or D or H)")
       if a=="P" or a=="D" or a=="H":
           MovieType(a)
           break
       else:
           print("Wrong seat type! Please select again")
def MovieType(a):
    while True:
        b=input("select the movie type(1 or 2)")
        if b=="1" or b=="2":
           TicketPrice(a,b)
           break
        else:
           print("Wrong movie type! Please select again")
def TicketPrice(a,b):
    if b=="1":
        if a=="P":
            p=100
        elif a=="D":
            p=140
        elif a=="H":
            p=400
    elif b=="2":
        if a=="P":
            p=120
        elif a=="D":
            p=200
        elif a=="H":
            p=500        
    print("The ticket price is",p)
SeatType()