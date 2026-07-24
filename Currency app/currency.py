n=float(input("Enter your amount in INR: "))
def convert_currency(n):
    usd =print( "DOLLAR: $" + str(n * 0.011))
    eur =print( "EUR: " + str(n * 0.0093))
    riyal =print( "RIYAL: " + str(n * 0.040))
    dong =print( "DONG: " + str(n * 278.72))
    return usd, eur, riyal, dong
x=input("Enter your choice: usd, eur, riyal, dong: ")
if x=="usd":    
    print(convert_currency(n)[0])
elif x=="eur":
    print(convert_currency(n)[1])
elif x=="riyal":
    print(convert_currency(n)[2])
elif x=="dong":
    print(convert_currency(n)[3])
