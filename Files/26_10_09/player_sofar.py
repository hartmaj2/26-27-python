import turtle

je_dole = True

def doleva():
    turtle.left(10)

def doprava():
    turtle.right(10)

def propiska():
    je_dole = False
    turtle.penup()
    

turtle.listen()

turtle.onkey(doleva,"a")
turtle.onkey(doprava,"d")
turtle.onkey(propiska,"space")

while True:
    turtle.forward(1)