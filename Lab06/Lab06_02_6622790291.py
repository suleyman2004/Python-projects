list2=input("Enter a comma-separeted list:").split(",")
for i in list2:
    for j in list2:
        for k in list2:
            if i!=j and i!=k and j!=k and i<j and i<k and j<k:
                print(i,j,k)
