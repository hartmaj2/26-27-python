import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def koch(delka, hloubka):
    if hloubka == 0:
        t.forward(delka)
    else:
        delka /= 3
        koch(delka, hloubka - 1)
        t.left(60)
        koch(delka, hloubka - 1)
        t.right(120)
        koch(delka, hloubka - 1)
        t.left(60)
        koch(delka, hloubka - 1)

def kochova_vlocka(delka, hloubka):
    for _ in range(3):
        koch(delka, hloubka)
        t.right(120)

# posunutí na hezčí pozici
t.penup()
t.goto(-200, 100)
t.pendown()

kochova_vlocka(400, 4)

turtle.done()