
i=0
for i in range(6):
    list=["Satawat","Pisit","Thanaphong","Pished","Nut","Amon"]
    a=input("Please enter a student\'s name that you want to delete (q=exit):")
    if a=="q":
        print("result is",list)
        break
    else:
        list.remove(a)
        print(list)
