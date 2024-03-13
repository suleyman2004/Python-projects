list=[]
for i in range(0,6):
    a=int(input("Input#%d:" %i))
    list.append(a)
a=int(input("Select the option: 1) Summary, 2) average, 3) min, 4) max ...."))
if a==1:
    print("Your result is ",sum(list))
elif a==2:
    print("Your result is ",sum(list)/len(list))
elif a==3:
    print("Your result is ",min(list))
elif a==4:
    print("Your result is ",max(list))
