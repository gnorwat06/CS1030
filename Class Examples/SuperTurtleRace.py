#Import turtle and random module
from turtle import *
from random import *

#Setup the screen
screen = Screen()
screen.bgcolor("lightyellow")

#Create a list of colors and a empty list for turtles
colors = ["red", "blue", "green", "purple", "orange", "pink"]
turtles = []

#Create turtles with random starting positions
for i, color in enumerate(colors):
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-200, 100 - i * 30)
    turtles.append(t)

#Draw the finish line
fline = Turtle()
fline.penup()
fline.goto(200,150)
fline.pendown()
fline.setheading(270)
fline.pensize(5)
fline.color("black")
fline.forward(300)
fline.hideturtle()

#funcion to move the turtles forward
def moveTurtle(t):
    t.forward(randint(1,10))


#race the turtles
while all(t.xcor() < 200 for t in turtles):
    for t in turtles:
        moveTurtle(t) #invoke the move turtle function

#determine the winner
winner = max(turtles, key = lambda t: t.xcor())
print(f"The winner is {winner.pencolor()} Turtle!")

#close turtle
done()
