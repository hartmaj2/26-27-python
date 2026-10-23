import time

for a in range(6,100):
    print("Pokus pro a =",a)
    time.sleep(0.1)
    while True:
        time.sleep(0.1)
        if a == 1:
            print(a)
            break
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 7
        print(a)

    