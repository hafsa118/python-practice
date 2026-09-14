# Take a person's monthly salary as input and calculate their yearly salary along with a 5% annual increment applied to it
Monthly_salary = float(input("Enter amount:"))
yearly_salary = Monthly_salary * 12
# 5% increement anually
increase = (yearly_salary * 5)/100

print("Final income of whole year is:",yearly_salary + increase)