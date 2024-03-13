while True:
    print("===== MAIN MENU =====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Exit")
    a=input("Select an operation (1-3):")
    if a=="3":
        print("Bye!!!")
        break
    b,c=input("Enter two numbers:").split()
    b=int(b)
    c=int(c)
    if a=="1":
        print("%d+%d= %d" %(b,c,c+b))
    elif a=="2":
        print("%d-%d=" %(b,c),b-c)


