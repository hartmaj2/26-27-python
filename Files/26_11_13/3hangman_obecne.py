# Jak bude vypadat obecne ten program

def novy_stav(tajne,stav,pismenko) -> str:
    ...

def vytiskni_obrazek(chyby) -> None:
    ...

tajne = ...
stav = ...
chyby = ...

while True:
    
    pismenko = ...
    vytiskni_obrazek(...)
    print(stav)

    if ... : # pismenko je ve slove
        stav = novy_stav(tajne,stav,pismenko)
    else:
        chyby = ...

    if ... : # je konec
        break
    