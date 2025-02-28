#Description: Given three sides of a triangle, compute the angles

#Import the math module and turtle
import math
from turtle import *

#Prompt the user for the three points
x1 = float(input("Enter the x-coordinate for Point 1: "))
y1 = float(input("Enter the y-coordinate for Point 1: "))
x2 = float(input("Enter the x-coordinate for Point 2: "))
y2 = float(input("Enter the y-coordinate for Point 2: "))
x3 = float(input("Enter the x-coordinate for Point 3: "))
y3 = float(input("Enter the y-coordinate for Point 3: "))

#compute the distance between the points
#math.hypot (Hypotenuse of a right-angle triangle
a = math.hypot(x2 - x3,y2 - y3)
b = math.hypot(x1 - x3,y1 - y3)
c = math.hypot(x1 - x2,y1 - y2)

#Compute the angles with the given formula
A = math.degrees(math.acos((a * a - b * b - c * c)/(-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c)/(-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a)/(-2 * a * b)))

#Display the results
print("The three angles are:",round(A,2),round(B,2),round(C,2))

####Creating the Triangle and display the angles using turtle

#Goto the first point
penup()
goto(x1,y1)
pendown()
dot(10,"red")

#Goto second point
goto(x2,y2)
write(round(B,2))
dot(10,"red")

#Goto the third point
goto(x3,y3)
write(round(C,2))
dot(10,"red")

#Goto point 1
goto(x1,y1)
write(round(A,2))

#Hide the turtle
hideturtle()
done()

