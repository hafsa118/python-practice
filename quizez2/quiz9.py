# Take an electricity meter's previous and current readings as input, along with the rate per unit, and calculate the total bill
rate_of_unit = float(input("Enter price of unit:"))
previous_reading = float(input("Enter previous reading of meter"))
current_reading = float(input("Enter current reading of meter"))

Previous_bill = previous_reading * rate_of_unit
print("Previous bill is:", Previous_bill)
current_bill = current_reading * rate_of_unit
print("current bill is:", current_bill)

total_bill = Previous_bill + current_bill
print("total bill is:", total_bill)