n = int(input("Please input a figure from 1 to 7"))
if n >= 1 and n <= 7:
    n_ch = True
else: print("Not correct")
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
elif n==7:
    print("Sunday")
else:
    print("Not appropriate value!")