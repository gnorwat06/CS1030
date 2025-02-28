#Description: Detecting wether an object is inside or outside another object

#Import turlte module
from turtle import *

#Prompt the user to enter circles coordinates and radius
x1 = float(input("Enter the x-coordinate of a circle: "))
y1 = float(input("Enter the y-coordinate of a circle: "))
radius = float(input("Enter the radius of a circle: "))

#Prompt the user to entere coordiates for the point
x2 = float(input("Enter a point x-coordinate: "))
y2 = float(input("Enter a point y-coordinate: "))

#Draw the circle
penup()
goto(x1,y1 - radius)
pendown()
circle(radius) #Draws the circle

#Draw the point using turtle function
penup()
goto(x2,y2)
pendown()
dot(10,"red")

#Display the status
penup()
goto(x1 - 70, y1 - radius -20)
pendown()

#Compute the distance
d = (pow(x2 - x1,2) + pow(y2 - y1,2)) ** 0.5

#Using a two-way display if we are in or out of the circle
if d <= radius:
    write("The point is inside the circle",font=("Times",14))
else:
    write("The point is outside the circle",font=("Times",14))

#HIde the turtle
hideturtle()
done()


