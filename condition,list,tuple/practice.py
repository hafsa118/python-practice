# ===================== CONDITIONS =====================
age = 18
print(age > 18)  # False

# Eg 1: if-elif-else for multiple condition
marks = 90
if marks >= 90:
    print("your grade is A")
elif marks >= 80:
    print("your grade is B")
else:
    print("your grade is C")

# write a python program that take number and print whether it positive
# negative zero
no = int(input("Enter your number:"))
if no > 0:
    print("number is positive")
elif no < 0:
    print("number is negative")
else:
    print("number equal to zero")


# ===================== LISTS (Mutable) =====================
Marks = [97, 98, 99]
print(Marks)

foods = ["samosa", "piza", "Burger"]
print(foods)

# can change/mutable
foods[0] = "Biryani"
print( foods[0])

student = ["Maryam", "Hafsa", "Fiza"]
print(student)

# indexing
print("Food at 0 index is:", foods[0])
print("student at 2 index is:", student[2])


# list slicing
list_1 = [70, 80, 90, 20, 10]
print(list_1[:3])
print(list_1[:])
print(list_1[2:])


# Function
# len(list), max(list), min(list)
Marks = [60, 70, 80, 100, 90]
print("length of list is:", len(Marks))
print("Max of list is:", max(Marks))
print("Min of list is:", min(Marks))

# append, insert, remove, pop, sort, reverse
print(Marks.append(98))
print(Marks.insert(1, 100))
print(Marks.remove(80))
print(Marks.pop(0))
print(Marks.sort())
print( Marks.reverse())

# write a program that takes name of food and make list and print length
s1 = input("Enter 1st string:")
s2 = input("Enter 2nd string:")
s3 = input("Enter 3rd string:")

My_list = [s1, s2, s3]
print(My_list)
print(len(My_list))


# ===================== TUPLE =====================
# like list but immutable
tup = (87, 64, 33, 33, 25, 76)
print(tup[0])  # 87

empty_tuple = ()
print(type(empty_tuple))

single_tuple = (1,)
print(type(single_tuple))

print(tup.index(3))
print(tup.count(33))

# make tuple of fruit and print total number and index of one
tuple = ("apple", "bannana", "mango")
print(len(tuple))
print(tuple.index(0))