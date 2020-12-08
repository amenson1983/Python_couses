quantity = int(input("Please put number of packages bought: "))
sum = float(quantity*99)
discount = 0
if quantity<10:
    discount = 0
elif quantity>=10 and quantity<=19:
    discount = sum*0.1
elif quantity>=20 and quantity<=49:
    discount = sum*0.2
elif quantity>=50 and quantity<=99:
    discount = sum*0.3
elif quantity>=100:
    discount = sum*0.4
to_pay = sum-discount
print("Your discount is: ", discount)
print("Amount to pay (discount has been applied): ", to_pay)
