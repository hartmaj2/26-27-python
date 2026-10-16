import turtle
import random

karel = turtle.Turtle()
pepa = turtle.Turtle()

karel.color("green")

while True:
    karel.forward(3)
    pepa.forward(1)
    uhel = random.randint(-10,10)
    karel.left(uhel)
    print(karel.xcor())

    if karel.xcor() > 100 or karel.ycor() > 100 or karel.xcor() < -100 or karel.ycor() < -100:
        uhel = karel.towards(0,0)