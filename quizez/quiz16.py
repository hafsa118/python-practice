# Take a number of seconds as input and convert it into hours, minutes, and remaining seconds
second = int(input())
hours = second//3600
print("hours", hours)
Minute = (second%3600)//60
print("minutes",Minute)
Second = second % 60
print("seconds",second)