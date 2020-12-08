num = int(input("Введите целое число от 1 до 10: "))
if num>0 and num<=10:
    num_ch = True
else: num_ch = False
if num_ch==True and num==1:
    num_ch = "I"
elif  num_ch==True and num==2:
    num_ch = "II"
elif  num_ch==True and num==3:
    num_ch = "III"
elif  num_ch==True and num==4:
    num_ch = "IV"
elif  num_ch==True and num==5:
    num_ch = "V"
elif  num_ch==True and num==6:
    num_ch = "VI"
elif  num_ch==True and num==7:
    num_ch = "VII"
elif  num_ch==True and num==8:
    num_ch = "VIII"
elif  num_ch==True and num==9:
    num_ch = "IX"
elif  num_ch==True and num==10:
    num_ch = "X"
else: num_ch = "Inapropriate!"
print(num_ch)