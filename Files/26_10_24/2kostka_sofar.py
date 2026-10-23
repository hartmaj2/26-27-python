import random
import time

money = 100
delka = 0

print("Cau, jdeme gamblit")

while True:

    delka += 1
    time.sleep(0.001)

    kostka = random.randint(1,6)

    if kostka in [4,5,6]:
        money += 10
    else:
        money -= 10

    print(money)
    
    if money <= 0:
        print("jseš broke kámo")
        print("přežil jsi",delka,"tahů")
        break