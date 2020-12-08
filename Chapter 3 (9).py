pocket = int(input("Put number of pocket: "))
ch_nech = pocket%2
if ch_nech == 0:
    ch_nech = 0
else: ch_nech = 1
if pocket == 0:
    print("Green")
elif pocket >=1 and pocket <=10 and ch_nech==0:
    print("Black")
elif pocket >=1 and pocket <=10 and ch_nech==1:
    print("Red")
elif pocket >=11 and pocket <=18 and ch_nech==0:
    print("Red")
elif pocket >=11 and pocket <=18 and ch_nech==1:
    print("Black")
elif pocket >=19 and pocket <=28 and ch_nech==0:
    print("Black")
elif pocket >=19 and pocket <=28 and ch_nech==1:
    print("Red")
elif pocket >=29 and pocket <=36 and ch_nech==0:
    print("Red")
elif pocket >=29 and pocket <=36 and ch_nech==1:
    print("Black")
else: print("Not correct value")