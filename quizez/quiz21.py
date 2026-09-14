# Take a number as input and extract its last digit and first digit using arithmetic operations only.
Number = int(input("Enter num"))
#last letter
last = Number % 10
First =Number //100
print("last is", last)
print("First is", First)