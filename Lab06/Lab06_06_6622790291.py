a=input("Enter dd/mm/yyyy:")

if len(a)<8: 
    print("Please enter 8 digits11")
else:
    date=int(a[:2])
    month=int(a[2:4])
    year=int(a[4:])
    if month>12:
        print("Error! There are 12 months")
    else:
        print("Date:%d\nMonth:%d\nYear:%d" %(date,month,year))