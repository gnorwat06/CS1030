#Description: testing each function in the custom turtle module

#Import UsefulTurtleFunctions
from UsefulTurtleFunctions import *
from turtle import *

#adjust the speed
speed(3)

#Change shape
shape("turtle")

#Change the pensize
pensize(2)

#Invoke the drawline function
drawLine(-50,-50,50,50)

#Invoke the writetext function
writeText("Testing Useful Turtle Functions",-50,-60)

#Invoke the drawpoint function
drawPoint(0,0)

#invoke the circle function
drawCircle(0,0,80)

#Invoke the drawRectangle function
drawRectangle(0,0,60,40)

hideturtle()
done()
