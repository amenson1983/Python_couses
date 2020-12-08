mass_kg = float(input("Введите вес в кг: "))
mass_nt = mass_kg*9.8
if mass_nt<100:
    print("Тело слишком легкое")
elif mass_nt>500:
    print("Тело слишком тяжелое")
else: print(round(mass_nt,2))