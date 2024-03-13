sum=0
number=0
while True:
    a=float(input("Enter an integer (-1 to exit):"))
    if a==-1:
        break
    else:
        number+=1
        sum+=int(a)
# This total witout use -1.
print("The sum of %d number(s) is %d." %(number,sum))
# This total with use -1.
print("The sum of %d number(s) is %d." %(number,sum-1))