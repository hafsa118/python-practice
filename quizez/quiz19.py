# Take a string and an integer n as input, and print the string repeated n times using memory id() before and after concatenation.
text = input("Enter a string ")
n = int(input("Enter a num"))

#before result
print(id(text))
result = text * n
print(result)
# after result
print(id(result))