import turtle
import random

turtle.speed(2)

kolik_uhlu = 5

otoceni =  360 / kolik_uhlu

while True:
    turtle.forward(100)
    turtle.left(otoceni)
    turtle.clear()

turtle.mainloop()