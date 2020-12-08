p_main_sum = float(input("Please put the main amount here: ")) #Основная сумма
ann_rate = float(input("Please input annual rate: "))/100 #Годовая ставка
years = float(input("Put quantity of years: ")) #Количество лет
freq_per = float(input("Put here how many times percentages are being applied for amount per year:"))
result = p_main_sum*((1+(ann_rate/freq_per))**(freq_per*years))
print("Total amount: ", round(result,2))
