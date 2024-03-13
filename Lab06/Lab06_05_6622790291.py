listA=[]
listB=[]
listC=[]
a=int(input("How many persons in a group:"))
print("Please enter grade from group A")
for i in range(a):
    b=float(input("Enter grade"))
    listA.append(b)
print("Please enter grade from group B")
for i in range(a):
    b=float(input("Enter grade"))
    listB.append(b)
print("Please enter grade from group C")
for i in range(a):
    b=float(input("Enter grade"))
    listC.append(b)
print("Highest grade of group A is %.1f" %max(listA))
print("Highest grade of group B is %.1f"  %max(listB))
print("Highest grade of group C is %.1f" %max(listC))
