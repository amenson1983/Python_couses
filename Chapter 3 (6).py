date = int(input("Введите день из даты: "))
month = int(input("Введите месяц из даты: "))
year = int(input("Введите последние две цифры года из даты: "))
intermed = date*month
if intermed==year:
    print("Волшебная дата!")
else: print("Не волшебная дата")