import random
list=[]
for i in range(4):
    a=input("Enter string#%s:" %i+1)
    list.append(a)
random.shuffle(list)
print("Random order sentences:",end=" ")
for i in list:
    print(i,end=" ")
