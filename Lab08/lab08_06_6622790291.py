from operator import itemgetter
students={}
id={}


while True:
    user=input("Input(Done=exit):")
    if user.upper()=="DONE":
        break
    else:
        id,score=user.split()
        if not id.isnumeric() or not int(id)>0 or not score.isnumeric() or not int(score)>0:
            print("Invalid input")
        else:
            score=int(score)
            students[id]=score
print("output:")
di=dict(sorted(students.items(),key=itemgetter(1),reverse=True))
for key,val in di.items():
    print(key,val)