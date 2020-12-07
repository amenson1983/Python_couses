item_1 = float(input("Please put the price for item 1:"))
item_2 = float(input("Please put the price for item 2:"))
item_3 = float(input("Please put the price for item 3:"))
item_4 = float(input("Please put the price for item 4:"))
item_5 = float(input("Please put the price for item 5:"))
sales_tax = float(7/100)
total_amount = item_1+item_2+item_3+item_4+item_5
total_tax = total_amount*sales_tax
total_to_pay = total_amount+total_tax
print("Your goods cost: ", round(total_amount, 2), "\nThe sales tax is: ", round(total_tax,2), "\nTotal amount to pay: ", round(total_to_pay,2))