str1='Hello, World!'
str2="python is fun"
str3='''Python is a programming language that lets you work quickly'''
print(str1)
print(str2)
print(str3)

# string concatenation
str4 = "hello"
str5 = "world"
final_str = str4 + " " + str5
print(final_str)
final_str2 = str4 +str5 + "!"
print(final_str2)

# length of string
str6 = "im going to university"
print(len(str6))

# indexing
str7 = "hafsa"
print(str7[0])  # prints 'h'
print(str7[1])  # prints 'a'
print(str7[2])  # prints 'f'
print(str7[3])  # prints 's'
print(str7[4])  # prints 'a'
print(str7[-1])  # prints 'a'
print(str7[-2])  # prints 's'
print(str7[-3]) # prints 'f'
print(str7[-4])  # prints 'a'
print(str7[-5])  # prints 'h'


# string are immutable

# slicing 
str8 = "python programming done by hafsa"
print(str8[0:6])  # prints 'python'
print(str8[7:18])  # prints 'programming'
print(str8[19:25])  # prints 'done by'
print(str8[25:30])  # prints '

# negative slicing
str9 = "python programming done by maryam"
print(str9[-5:-1])  # prints 'arya'
print(str9[-6:-1])  # prints 'marya'
print(str9[-7:-1])  # prints 'maryam'
print(str9[-8:-1])  # prints 'maryam'

# functions
print(str9.upper())  # prints 'PYTHON PROGRAMMING DONE BY MARYAM'
print(str9.lower())  # prints 'python programming done by maryam'
print(str9.title())  # prints 'Python Programming Done By Maryam'
print(str9.find("d"))  # prints 18
print(str9.replace("maryam", "hafsa"))  # prints 'python programming done by hafsa'
print(str9.split())  # prints ['python', 'programming', 'done', 'by', 'maryam']
print(str9.strip())  # prints 'python programming done by maryam'
print(str9.count("m"))  # prints 4


# formatted string
name="hafsa azhar"
age=18
print(f"my name is {name} and my age id {age} yrear old")


# repitition
# print yummy ten time 
ans =" yummy "*10
print(ans)


# member ship
str="bnana"
"a" in str
"z" in "bnana"




# escape sequence
print("hello\nworld")
print("hello\tworld")
print("its\'hafsa")
print("i said \"hi")