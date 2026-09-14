# Take the radius of a circle as input and print its area and circumferenc
from math import pi
radius = int(input("Radius of circle is:"))
# Area = 2 π r^2
Area = 2 *pi*(radius*2)
print("Area is", Area)

Circumference = 2*pi*radius
print("circumference is",Circumference)