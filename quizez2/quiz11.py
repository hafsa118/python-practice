# Take a year as input and check whether it is a leap year using only arithmetic operators (no if-else), printing True or False.
year = int(input("Enter year:"))
is_leap_year = (year % 4 == 0 and year % 100 != 0)or(year % 400 == 0)
print(year, is_leap_year)