#Shayan Memon
#2/23/2025
#P2LAB1
#Math expression

import math

#Get radius from user
radius = float(input("Enter the radius: "))

#Calculate the circumference, diameter, and area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")