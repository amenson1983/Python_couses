amount = float(input("Please put amount: "))
sales_tax = amount*0.07
tips = amount*0.18
total = round((amount+sales_tax+tips),2)
print("Amount of goods bought: ", amount, "\nSales tax amount: ", round(sales_tax,2), "\nTips amount: ", tips, "\nTotal amount: ", total)
