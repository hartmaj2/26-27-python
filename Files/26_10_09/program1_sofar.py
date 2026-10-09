import turtle
import math

turtle.shape("turtle")
turtle.color("violet")

velikost = 100

def domecek_jednim_tahem_bejby():
    turtle.forward(velikost)
    turtle.left(135)
    turtle.forward(velikost*math.sqrt(2))
    turtle.right(75)
    turtle.forward(velikost)
    turtle.right(120)
    turtle.forward(velikost)
    turtle.right(120)
    turtle.forward(velikost)
    turtle.left(90)
    turtle.forward(velikost)
    turtle.left(90)

def domecek():
    for i in range(4):
        turtle.forward(velikost)
        turtle.right(90)

    for i in range(3):
        turtle.forward(velikost)
        turtle.left(120)

domecek_jednim_tahem_bejby()

turtle.mainloop()