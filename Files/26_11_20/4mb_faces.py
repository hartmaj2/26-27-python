from microbit import *

neutral = Image(
    '00000:'
    '09090:'
    '00000:'
    '99999:'
    '00000'
)

wow = Image(
    '00000:'
    '09090:'
    '09990:'
    '90009:'
    '09990'
)


while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(neutral)
        sleep(100)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif pin_logo.is_touched():
        display.show(wow)
    elif button_b.is_pressed():
        display.show(Image.SAD)
        