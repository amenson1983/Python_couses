n5 = int(input("Put 5 kop coins quantity: "))
n10 = int(input("Put 10 kop coins quantity: "))
n50 = int(input("Put 50 kop coins quantity: "))
coin_5 = 5*n5
coin_10 =10*n10
coin_50 = 50*n50
rub = 100
mix = coin_5+coin_10+coin_50
if mix==rub:
    print("Congratulations! You won!")
elif mix>rub:
    print("Перелёт")
elif mix<rub:
    print("Недолёт")