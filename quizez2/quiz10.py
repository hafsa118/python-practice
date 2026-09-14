# Take a number as input and check, using arithmetic and comparison operators only, whether it is a perfect square (hint: compare with int(number ** 0.5) squared)
num = int(input("Enter number:"))
root = num**0.5
print("root of number is:",root)


if root*root==num:
    print("it is a perfect square")
else:
    print("it is not a perfect square")