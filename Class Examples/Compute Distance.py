#Description: Find the distance between two points

#import the turtle module
from turtle import *

#Prompt the user for inputting the x,y coordinate for point 1
x1 = float(input("Enter the x coordinate for point 1: "))
y1 = float(input("Enter the y coordinate for point 1: "))

#Prompt the user for inputting the x,y coordinate for point 2
x2 = float(input("Enter the x coordinate for point 2: "))
y2 = float(input("Enter the y coordinate for point 2: "))

#Compute the distance
distance = ((x2 - x1) **2 + (y2-y1) ** 2) ** 00.5

#Display two points and the connecting line
penup()
goto(x1,y1) #First point loacation
pendown()
dot(10,"red")
write("Point 1",font=("Times",15))
goto(x2,y2) #drawing a line from point 1 to point 2
dot(10,"red")
write("Point 2",font=("Times",15))

#Move to the center point of the line and display the distance
penup()
goto((x1 + x2) / 2, (y1 + y2) /2)
write(distance,font=("Times",15))
done()

