# Take a number as input, convert it to float, then back to int, and print both id() values to observe memory changes
Number = int(input("Enter Num"))
print(Number)
print(id(Number))

float(Number)
print(Number)
print(id(Number))

int(Number)
print(Number)
print(id(Number))