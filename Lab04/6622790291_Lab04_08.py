print("welcome to pizza online ordering.")
print("please input \"y\" if you want to order, otherwise input \"n\"")
a=input("pizza? (price_359):")
total=0
if a=="y":
    total=total+359
a=input("chicken? (price_3 pieces for 199):")
if a=="y":
    total=total+199
a=input("pasta? (price_99)")
if a=="y":
    total=total+99
a=input("salad? (price_99):")
if a=="y":
    total=total+99
a=input("coke? (price_550ml for 25):")
if a=="y":
    total=total+25
print("total price is",total)
print("thanks")
