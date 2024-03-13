print("Fever Symptoms Advisor Program")
a=float(input("Check your body temperature in F="))
if a>=100.4:
    print("You got fever")
    b=int(input("Choose your treatment: 1 =medication 2 = no medication >>>"))
    if b==1:
        print("Take Tylenol every 4 hours as needed")
    elif b==2:
        print("Taking a bath in lukewarm water or get the cool packs")
    else:
        print("You choose wrong choice")
elif a<100.4:
    print("You are fine")
