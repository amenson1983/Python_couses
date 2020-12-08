mass = int(input("Please point the weight of your parcel (grams): "))
rate = 0
if mass<=200:
    rate = 150
elif mass>200 and mass<=600:
    rate = 300
elif mass>600 and mass<=1000:
    rate = 400
elif mass>1000:
    rate = 475
cost = rate*float(mass/100)
print("Amount to pay: ", cost)