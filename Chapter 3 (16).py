year = int(input("Put the year: "))
year_100 = year%100
year_400 = year%400
year_100_4 = year%4
if year_100 == 0 and year_400 == 0:
    print("Год високосный, \nВ феврале этого года 29 дней")
elif year_100 != 0 and year_100_4 == 0:
    print("Год високосный, \nВ феврале этого года 29 дней")
else: print("Год не високосный")