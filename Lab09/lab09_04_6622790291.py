def UserInput():
    w=float(input("Input your weight(kilogram):"))
    h=float(input("input your height(meter):"))
    FindBMI(h,w)
def FindBMI(hh, ww):
    bmi=ww/(hh*hh)
    ShowBMI(bmi)
def ShowBMI(MyBMI):
    print("The user BMI is %.2f" %MyBMI)
UserInput()