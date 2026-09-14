# Take a car's speed in km/h as input and convert it to meters per second
# speend in km/h → convert m/s
speed_k = float(input("Enter a speed:"))
speed_m = (speed_k * (10**3)) / 3600
print("speed in meter is:", speed_m)