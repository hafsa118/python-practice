# Take two numbers as input and print the larger one using arithmetic (no if-else).
A = float(input("Enter a number:"))  
B = float(input("Enter b number:"))  
large=((A+B) + abs(A-B))/2
print(large)