#Descripton: Custom functions for common turtle tasks

#import turtle module
from turtle import *

#Draw a line from point 1 to point 2
def drawLine(x1,y1,x2,y2):
    penup()
    goto(x1,y1)
    dot(10,"Blue")
    pendown()
    goto(x2,y2)
    dot(10,"Blue")

#write a text at the specified location
def writeText(s,x,y):
    penup()
    goto(x,y)
    pendown()
    write(s,font="Times,18,Bold")

#Draw a point at our specified location
def drawPoint(x,y):
    penup()
    goto(x,y)
    pendown()
    dot(14,"red")

#Draw a circle centered at x,y
def drawCircle(x,y,radius):
    penup()
    goto(x,y - radius)
    pendown()
    circle(radius)

#Draw a rectangle
def drawRectangle(x,y,width,height):
    penup()
    goto(x + width / 2, y + height / 2)
    pendown()
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
