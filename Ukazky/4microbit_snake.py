# USE WITH: https://python.microbit.org/v/3

from microbit import *
from random import randint

snake = [(2, 2)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction = 0
food = (4, 4)

while True:
    if button_a.was_pressed():
        direction = (direction - 1) % 4
    if button_b.was_pressed():
        direction = (direction + 1) % 4

    dx, dy = directions[direction]
    x = (snake[0][0] + dx) % 5
    y = (snake[0][1] + dy) % 5
    head = (x, y)

    eating = head == food

    if head in (snake if eating else snake[:-1]):
        display.scroll("GAME OVER")
        break

    snake.insert(0, head)

    if eating:
        if len(snake) == 25:
            display.scroll("WIN")
            break

        while food in snake:
            food = (randint(0, 4), randint(0, 4))
    else:
        snake.pop()

    display.clear()
    for x, y in snake:
        display.set_pixel(x, y, 5)

    display.set_pixel(food[0], food[1], 9)
    display.set_pixel(head[0], head[1], 9)

    sleep(500)
