#import the turtle module
from turtle import *

#Change pensize
pensize(4)

#Change the shape of turtle
shape("turtle")

#Draw a triangle and fill it with color
penup()
goto(-170,-25)
pendown()
begin_fill()
color("red")
circle(30,steps = 3)
end_fill() #fills the object with color

#Draw a square and fill it with color
penup()
goto(-85,-25)
pendown()
begin_fill()
color("orange")
circle(30,steps = 4)
end_fill()

#Draw a pentagon and fill it with color
penup()
goto(0,-25)
pendown()
begin_fill()
color("yellow")
circle(30,steps = 5)
end_fill()

#Draw a hexagon and fill it with color
penup()
goto(85,-25)
pendown()
begin_fill()
color("green")
circle(30,steps = 6)
end_fill()

#Draw a hexagon and fill it with color
penup()
goto(170,-25)
pendown()
begin_fill()
color("blue")
circle(30)
end_fill()

#Title of the shapes canvas
color("purple")
penup()
goto(-100,50)
pendown()
write("Cool Colorful Shapes", font=("Times",18,"bold"))
hideturtle()
done()

