def CelsiusToFahrenheit(c):
    f=(c*(9/5)+32)
    return f
c=float(input("Input temperature in degree celsius:"))
print("The degree is farenheit is %.2f " %CelsiusToFahrenheit(c))
