print("==========Welcome to hi!! Car Wash====")
services=input("choose your services:W=Wash C=Wash+Vacuum>>>")
if services.lower()=="w" or services.lower()=="c":
    size=input("Enter your car size:\"S\",\"M\",\"L\:")
    if size.upper()=="S" or size.upper()=="M" or size.upper()=="L":
        if services.lower()=="w" and size.upper()=="S":
            print("Price=100baht")
        elif services.lower()=="w" and size.upper()=="M":
            print("Price=120baht")
        elif services.lower()=="w" and size.upper()=="L":
            print("Price=140baht")
        elif services.lower()=="c" and size.upper()=="S":
            print("Price=120baht")
        elif services.lower()=="c" and size.upper()=="M":
            print("Price=140baht")
        elif services.lower()=="c" and size.upper()=="L":
            print("Price=160baht")
    else:
        print("You enter the wrong car size")
else:
    print("Please Choose your services")
