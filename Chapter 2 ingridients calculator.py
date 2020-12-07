sugar_gl = 1.5
butter_gl = 1
wheat_gl = 2.75
cakes = 48
sugar_1 = sugar_gl/cakes
butter_1 = butter_gl/cakes
wheat_1 = wheat_gl/cakes
need_cakes = float(input("Please put desired quantity of cakes: "))
sugar_need = need_cakes*sugar_1
butter_need = need_cakes*butter_1
wheat_need = need_cakes*wheat_1
print("For such quantity of cakes you need:", "\nSugar: ", round(sugar_need,2), "glasses", "\nButter: ", round(butter_need,2), "glasses", "\nWheat: ", round(wheat_need,2), "glasses")
