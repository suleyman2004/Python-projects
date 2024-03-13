total=0
Heart=0
Sad=0
Like=0
for i in range(10):
    a=input("Feeling Like (\"L\"), Sad (\"S\"), and Heart(\"H\")?")
    if a=="L":
        tot=total+1
        Like=Like+1
    elif a=="H":
        total=total+1
        Heart=Heart+1
    elif a=="S":
        total=total+1
        Sad=Sad+1
    else:
        print("Invalid input, accepts only (L/S/H).")
if Like==0:
    Like_total=0
else:
    Like_total=Like/total*100
if Heart==0:
    Heart_total=0
else:
    Heart_total=Heart/total*100
if Sad==0:
    Sad_total=0
else:
    Sad_total=Sad/total*100
print("=======")
print("Total is ",total)
print("=======")
print("Like: %d (%.2f)%%" %(Like,Like_total))
print("Heart: %d (%.2f)%%" %(Heart,Heart_total))
print("Sad: %d (%.2f)%%" %(Sad,Sad_total))
    
