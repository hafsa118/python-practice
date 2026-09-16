# Write a program take your favorite food name as input and print
# the middle 3 character
# last two character.

food = input("Enter your favorite meal:")
last_2 = food[-2:]
print(last_2)

Middle_3 = food[len(food)//2 - 1:len(food)//2 + 2]
print(Middle_3)