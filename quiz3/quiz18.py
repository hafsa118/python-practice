# take a name as input and print first and last initial

Name = input("Enter your name:")
space = Name.find(" ")
print("First initial is:", Name[0])
print("last initial is", Name[space+1])