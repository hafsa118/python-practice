# Take the price of an item and a discount percentage as input and print the final price
Price = float(input())
Discount = float(input())
amount = Price-(Price * Discount/100)
print(amount)