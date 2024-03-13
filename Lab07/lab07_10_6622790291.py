while True:
    num=input("Enter an integer value (\"X\" to exit):")
    if num.isdigit():
        num=int(num)
        for row in range(num):
            for col in range(num):
                if row==col or row+col==num-1:
                    print("X",end=" ")
                else:
                    print(".",end=" ")
            print()
    else:
        break