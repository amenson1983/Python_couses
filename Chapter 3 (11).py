book = int(input("How many books bought? :"))
score = 0
if book<=0:
    score = 0
elif book>0 and book<2:
    score = 0
elif book>=2 and book<4:
    score = 5
elif book>=4 and book<6:
    score = 15
elif book>=6 and book<8:
    score = 30
elif book>=8:
    score = 60
print("Your score is: ", score, "points.")