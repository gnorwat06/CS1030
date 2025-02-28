#Description: Turtle is randomly walking through a garden of flowers.
#16 by 16 lattice

#Import the turtle and random module
from turtle import *
from random import randint

#Screensize
screensize(canvwidth = 400, canvheight = 300, bg = "light blue")
setup(200,200) #Adjust the size of the canvas
speed(10) #set turtle speed to medium
shape("turtle")

#Draw 16 by 16 lattice
color("gray")
x = -80
#Create 16 horizontal lines
for y in range(-80,81,10):
    penup()
    goto(x,y)
    pendown()
    forward(160)

y = 80
right(90)
#Drawing 16 vertical lines
for x in range(-80,81,10):
    penup()
    goto(x,y)
    pendown()
    forward(160)

#Start at your default position
speed(3)
pensize(3)
color("red")
penup()
goto(0,0)
pendown()

#current pen location at the cener of lattice
x = y = 0
while abs(x) < 80 and abs(y) < 80:

    #Generate a random value 0 - 3
    r = randint(0,3)

    #matchcase to find directin
    match r:
        case 0: #walk east
            x += 10
            color("blue")
            setheading(0)
            forward(10)
        case 1: #walk sourth
            y -= 10
            color("purple")
            setheading(270)
            forward(10)
        case 2: #walk west
            x -= 10
            color("green")
            setheading(180)
            forward(10)
        case 3: #Walk north
            y += 10
            color("red")
            setheading(90)
            forward(10)
#Close turtle
done()
            
