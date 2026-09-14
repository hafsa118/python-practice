# Take principal, rate, and time as input and calculate simple interest.
Price = int(input("Enter price "))
rate = int(input("Enter rate "))
time = int(input("Enter time "))

SI = (Price * rate * time)/100
print("si is ",SI)