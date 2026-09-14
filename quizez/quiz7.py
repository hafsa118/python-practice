# Take a number as input and print whether it is even or odd using the modulo operator.
Number = int(input("Enter a number:"))
R = Number % 2
if R==0:
    print("even")
else:
    print("odd")