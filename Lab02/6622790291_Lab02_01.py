melted_chocolate=float(input("Enter amount of melted chocolate to be poured into the cup (ml)"))
milk=float(input("Enter amount of milk to be milk be poured into the cup(ml)"))
total_ml=melted_chocolate + milk
total_oz=total_ml*0.0338
print("Now Emmy\'s cup is filled with %d ml (or about %.2f oz) of chocolate milk." %(total_ml,total_oz))

