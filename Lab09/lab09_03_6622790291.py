def SumOut(x=list):
    print("summation is ",sum(x))
def MaxOut(x=list):
    print("maximum is ",max(x))
def MinOut(x=list):
    print("minimum is ",min(x))
    
def UserInput():
    while True:
        a=input("Enter an input:")
        if a.upper()=="DONE":
            break
        elif a>"0":
            a=int(a)
            list1.append(a)
        else:
            print("Error")       
list1=[]
UserInput()
SumOut(list1)
MaxOut(list1)
MinOut(list1)