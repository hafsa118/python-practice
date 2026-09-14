# Take the price of a coffee and the number of cups bought as input, then print the total cost including 15% service tax.
Price = int(input("Enter price!"))
Num = int(input("Enter number of cup:"))
# calcule 15% sale tax
total_price = Num * Price
print(total_price)

sale_tax = (total_price * 15) / 100

print("sale tax is", sale_tax)
bill = sale_tax + total_price
print("you have to Pay", bill, "-/PKR")
