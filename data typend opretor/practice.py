# data type .py 
food ="pizza" # string
print(type(food))
age = 21 # integer
print(type(age))
area= 3.14 # float
print(type(area))
name="hafsa" # string
print(type(name))
a=int(input("enter a number a:")) 
b=int(input("enter a number b:"))
sum=a+b
print("sum of a and b is:",sum)


# implicit type conversion
x=5 # int
y=2.5 # float
z=x+y # python convert int to float 
print(z)
print(type(z))


# explicit conversion
x="10"
y=int(x)
print(y+5)

# assignment 1 
# a number as input and convert to float print both form
a=int(input("enter a number a "))
print(a)
print(type(a))
y=float(a)
print(y)
print(type(y))

# arthmatic opretor
x=5
y=5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

# comprison opretor 
print(x==y)
print(x>=y)
print(x<y)

# logical opretor
print(x>y and x<y)  #both t t true
print(x==y or x>y)  #if one

# assignment opretor
x=x+6
x+=6

# input in celsius and out put in kelvin and feran hite
tempC=float(input("enter a temp "))
fern=(tempC*1.8)+32
print(fern)
kel=tempC+273.5
print(kel)

# bill split caculator
total_bill=float(input("enter a bill "))
frnd=int(input("number of frnd "))
bill= total_bill/frnd
print(bill)


