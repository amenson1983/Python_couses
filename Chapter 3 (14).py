mass = float(input("Please put your mass, kg: "))
height = float(input("Please point your height, m: "))
index = mass/(height**2)
if index<18.5:
    print("Your index is less than optimal - ", round(index,2))
elif index>=18.5 and index<=25:
    print("Your index is optimal -", round(index,2))
elif index>25:
    print("Your index is more than optimal. Perhaps you need to eat half less hehe ) - ", round(index,2))