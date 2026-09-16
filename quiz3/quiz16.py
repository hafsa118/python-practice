# taking a sentence as input and without using replace() more than once, swap
# the first and last character of the string using slicing and concatenation.

str = input("Enter your sentence")
swap = str[-1] + str[1:-1] + str[0]
print(swap)