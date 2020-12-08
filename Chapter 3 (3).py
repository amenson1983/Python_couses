age = int(input("Введите возраст (количество полных лет): "))
category = "unknown"
if age >0 and age<1:
    category = "Младенец"
elif age>=1 and age<13:
    category = "Ребенок"
elif age>=13 and age<20:
    category = "Подросток"
elif age>=20:
    category = "Взрослый"
else:
    print("This is impossible!")
print(category)