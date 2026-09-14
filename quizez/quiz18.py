# Take a number as input and check if it is a multiple of both 3 and 5 using arithmetic operators only
Num = int(input("Enter a numbe:"))
rem3 = Num % 3
rem5 = Num % 5

if rem3 + rem5 == 0:
    print("its multiple of 3,5")
else:
    print("it not multiple of 3,5")