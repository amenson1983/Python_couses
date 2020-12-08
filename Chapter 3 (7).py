red = "Красный"
blue = "Синий"
yellow = "Желтый"
violet = red+blue
orange = red+yellow
green = blue+yellow
chosen_col_1 = input("Color 1:")
chosen_col_2 = input("Color 2:")
mix = chosen_col_1+chosen_col_2
mix2 = chosen_col_2+chosen_col_1
if mix==violet or mix2==violet:
    print("VIOLET")
elif mix==orange or mix2==orange:
    print("ORANGE")
elif mix==green or mix2==green:
    print("GREEN")
else: print("It seems to be a MISTAKE")