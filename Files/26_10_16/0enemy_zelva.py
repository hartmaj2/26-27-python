import turtle
import random

enemy = turtle.Turtle()
player = turtle.Turtle()

player.color("green")
enemy.color("red")

def turn_player_left():
    player.left(10)

def turn_player_right():
    player.right(10)

def show_distance():
    print(enemy.distance(player))
    if enemy.distance(player) < 30:
        enemy.left(180)

turtle.listen()

turtle.onkey(turn_player_left,"a")
turtle.onkey(turn_player_right,"d")
turtle.onkey(show_distance,"space")

player.speed(0)
enemy.speed(0)

enemy.teleport(100,100)
enemy.setheading(180)

while True:
    player.forward(3)
    enemy.forward(2)
    smer = random.randint(-10,10)
    enemy.left(smer)

    if enemy.xcor() > 350:
        enemy.setheading(180)
        enemy.forward(2)
    if enemy.xcor() < -350:
        enemy.setheading(0)
        enemy.forward(2)
   
    if enemy.ycor() > 350:
        enemy.setheading(270)
        enemy.forward(2)
    if enemy.ycor() < -350:
        enemy.setheading(90)
        enemy.forward(2)  
    
    # print(player.xcor())
    print(player.ycor())
