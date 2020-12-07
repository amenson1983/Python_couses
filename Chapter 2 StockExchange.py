b_stock = 2000 #Bought stock quantity
b_sum = float(40*b_stock) #Bought stock amount
b_br_rew = 0.03*b_sum #Bought stock broker reward
s_stock = 2000 #Sold stock quantity
s_sum = float(42.75*s_stock) #Sold stock amount
s_br_rew = 0.03*s_sum #Sold stock broker reward
profit = (s_sum)-(b_sum+b_br_rew+s_br_rew)
print("Bought stock quantity: ", b_stock, "\nSold stock quantity: ", s_stock, "\nBroker purchase reward: ", b_br_rew, "\nBroker sell reward: ", s_br_rew, "\nIncome amount: ", s_sum, "\nProfit amount: ", profit)
if profit>0:
    print("OK, Joe got profit in amount: ", profit)
else: print("Oh no, loses consist: ", profit)

