#Description: Dsiplaying the 5 different rings

#import the turtle module
from turtle import *

#increase the pensize
pensize(8)

#change the shape of the pointer
shape("turtle")

#create the blue ring
color("blue")
penup() #pulls the pen/pointer off of the canvas
goto(-110, -25) #goes to the exact location
pendown() #puts the pen/pointer onto the canvas
circle(45) #circle function takes in the radius

#create the black ring
color("black")
penup() #pulls the pen/pointer off of the canvas
goto(0, -25) #goes to the exact location
pendown() #puts the pen/pointer onto the canvas
circle(45) #circle function takes in the radius

#create the red ring
color("red")
penup() #pulls the pen/pointer off of the canvas
goto(110, -25) #goes to the exact location
pendown() #puts the pen/pointer onto the canvas
circle(45) #circle function takes in the radius

#create the yellow ring
color("yellow")
penup() #pulls the pen/pointer off of the canvas
goto(-55, -75) #goes to the exact location
pendown() #puts the pen/pointer onto the canvas
circle(45) #circle function takes in the radius

#create the green ring
color("green")
penup() #pulls the pen/pointer off of the canvas
goto(55, -75) #goes to the exact location
pendown() #puts the pen/pointer onto the canvas
circle(45) #circle function takes in the radius

#hide the turlte pointer
hideturtle()

#waits for the user to close the program
done()
