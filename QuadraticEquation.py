#learnig about the quadratic equations

#what is the quadratic equation

# a equation with the degree 2 is called quadratic equation

import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print("the roots are :" , r1,r2)


#calaulate the radius of the speare

# take surface area from the user
S = float(input("Enter the surface area of the sphere: "))

# calculate radius
r = math.sqrt(S / (4 * math.pi))

# calculate volume
volume = (4/3) * math.pi * (r ** 3)

print("The radius of the sphere is:", r)
print("The volume of the sphere is:", volume)

