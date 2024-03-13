from operator import itemgetter
d={}
while True:
    in_str=input("Input (Done=exit): ")
    if in_str.upper()=="DONE":
        break
    else:
        id,score=in_str.split()
        if id.isalpha():
            print("Invalid input")
        elif id in d.keys():
            print("Duplicated ID")
        else:
            d[id]=score
di=dict(sorted(d.items(),key=itemgetter(1),reverse=True))
for key,val in di.items():
    print(key,val)