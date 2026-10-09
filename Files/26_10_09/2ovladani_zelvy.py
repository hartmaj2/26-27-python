import turtle

def nahoru():
    turtle.setheading(90)
    turtle.forward(100)

def dolu():
    turtle.setheading(270)
    turtle.forward(100)

def doleva():
    turtle.setheading(180)
    turtle.forward(100)

def doprava():
    turtle.setheading(0)
    turtle.forward(100)

turtle.listen()

turtle.onkey(doprava,"d")
turtle.onkey(doleva,"a")
turtle.onkey(dolu,"s")
turtle.onkey(nahoru,"w")

turtle.mainloop()

