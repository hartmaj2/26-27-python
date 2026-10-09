# Zopakujeme: import, zakladni prikazy zelvy, opakovani, promenne
# Novy koncept: funkce (definice a volani)

import turtle

delka = 50

def domecek():
    for i in range(4):
        turtle.forward(delka)
        turtle.left(90)

    turtle.left(90)
    turtle.forward(delka)
    turtle.right(90)

    for i in range(3):
        turtle.forward(delka)
        turtle.left(120)

domecek()

turtle.backward(200)

domecek()

turtle.mainloop()