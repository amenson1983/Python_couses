reg_tax = 0.025
fed_tax = 0.05
goods_amount = float(input("Please type the amount of goods bought: "))
reg_tax_am = reg_tax*goods_amount
fed_tax_am = fed_tax*goods_amount
tax = reg_tax_am+fed_tax_am
total_sum = tax+goods_amount
print("Goods cost: ", goods_amount,"\nRegional taxes amount: ", reg_tax_am, "\nFederal tax amount", fed_tax_am, "\nTotal tax amount: ", tax,"\nTotal amount to be paid: ", total_sum)
