import random

penize = 10

hodminci = random.randint(1,2)

if hodminci == 1:
    penize = penize + 1
    print("Vyhráváš zlatého bludišťáka")
else:
    penize = penize - 1
    print("Prohrál jsi lamáku")

print("Ted máš",penize,"peněž")