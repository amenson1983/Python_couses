veget = input("Будет ли на ужине вегетарианец?")
vegan = input("Будет ли на ужине веганец?")
non_glut = input("Будет ли на ужине приверженец безглютеновой диеты?")
yes = "да"
rest1 = "Изысканные гамбургеры от Джо"
rest2 = "Центральная пиццерия"
rest3 = "Кафе за углом"
rest4 = "Блюда от итальянской мамы"
rest5 = "Кухня шеф-повара"
if veget <= yes and vegan <= yes and non_glut <= yes: #all present
    print("Ваши варианты ресторанов: ")
    print(rest3)
    print(rest5)
elif veget > yes and vegan > yes and non_glut > yes: #none present
    print("Ваши варианты ресторанов: ")
    print(rest1)
    print(rest2)
    print(rest3)
    print(rest4)
    print(rest5)
elif veget <= yes and vegan > yes and non_glut > yes: #vegetarian present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest2)
    print(rest3)
    print(rest4)
    print(rest5)
elif veget > yes and vegan <= yes and non_glut > yes: #vegan present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest3)
    print(rest4)
    print(rest5)
elif veget > yes and vegan > yes and non_glut <= yes: #non gluten present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest2)
    print(rest3)
    print(rest5)
elif veget <= yes and vegan <= yes and non_glut > yes: #vegetarian present, vegan present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest3)
    print(rest5)
elif veget <= yes and vegan > yes and non_glut <= yes: #vegetarian present, non gluten present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest2)
    print(rest3)
    print(rest5)
elif veget > yes and vegan <= yes and non_glut <= yes: #vegan present, non gluten present, rest none
    print("Ваши варианты ресторанов: ")
    print(rest3)
    print(rest5)
else: print("Что-то не понятное...")