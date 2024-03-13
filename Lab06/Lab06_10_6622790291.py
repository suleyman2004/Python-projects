list=[]
for i in range(6):
    list.append(input("Write fruit:"))
for i in list:
    if len(i)<6:
        print(i,"is %d long" %len(i))
    elif len(i)>=6:
        print(i,"%d characters or more" %len(i))