# Take a train's departure time (hours and minutes) and journey duration (in minutes) as input, and calculate the arrival time in hours and minutes.
Train_dep_time_hour = float(input("Enter a time in hour"))
Time_dep_min = Train_dep_time_hour * 60

print("departure time in minutes", Time_dep_min)

Journey_duration = int(input("Enter a duration:"))

Arriving_time = Time_dep_min + Journey_duration
Arriving_time_in_hours = Arriving_time / 60
print("Arriving time in hours:", Arriving_time_in_hours)