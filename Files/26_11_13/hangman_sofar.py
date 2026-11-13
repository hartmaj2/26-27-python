def novy_stav(tajne,stav,pis):
    novy_stav = ""
    for i in range(len(tajne)):
        if tajne[i] == pis:
            novy_stav += pis
        else:
            novy_stav += stav[i]
    return novy_stav

tajne = "banana"
stav = "______"
pokusy = 5

while True:

    print("Máš",pokusy,"pokusů")
    print("Stav:",stav)
    pis = input("Zadej písmenko chlapče: ")
    if pis in tajne:
        stav = novy_stav(tajne,stav,pis)
    else:
        pokusy -= 1

    if pokusy == 0:
        print("You stupid")
        break

    if stav == tajne:
        print("You smart")
        break