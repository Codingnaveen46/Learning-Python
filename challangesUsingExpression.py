# calculation area of tringle
from day1 import flotvalue

#this is the first method

height = int(input("Enter height: "))
based =  int(input("Enter base: "))

area = 1/2 * height*2*based
print(area)

# this is the second method
based = int(input("Enter base: "))
height = int(input("Enter height: "))


area1 = (based*height)/2
print('area1 of the triangle is :',area1)


#calculate the area of trapzium

a1 = int(input("Enter height: "))
b1 = int(input("Enter base: "))
height1 = int(input("Enter height: "))

area2 = 0.5 * (a1 + b1) * height1

print('area2 of the trapzium is :',area2)


#calcualte the area of circle
import math
circle1 = int(input("Enter radius: "))

calculate = 3.14159 * circle1 * circle1

print("the area of the circle is :",calculate)

#this is the second method which is prefered


circle1 = int(input("Enter radius: "))

calculate = math.pi * circle1 * circle1

print("the area of the circle is :",calculate)


# converting km to miles


firstkm = int(input("Enter first KM: "))

miles =  0.62137 *firstkm

print("the converted miles are  :",miles)



#calculating the displacement


v1 = float(input("Enter first : "))
u2 = float(input("Enter second : "))
a1 = float(input("Enter first : "))

d = (v1*v1 - u2*u2)/ (2*a1)

print("the calcualtion of the displacement is :",d)
