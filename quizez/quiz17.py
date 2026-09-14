# Take two numbers as input and check if they are equal without using the "==" comparison result printed directly (use subtraction logic)
A = int(input("Enter A:"))
B = int(input("Enter B:"))

# subtraction logic    No ==
# check if they are equal
diff=A-B
if diff==0:
    print("They are equal")
else:
    print("They are not equal")