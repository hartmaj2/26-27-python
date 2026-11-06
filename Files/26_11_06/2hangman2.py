
# ukol: dostaneme slovo a pismenko, nasim ukolem je vytvorit vysledek tvaru __x_x_x
# kde x je na pozicich, kde se nachazi pismenko

STAVY = [
"""
+-----+
|     |
|     |
|     |
+-----+
""",
"""
  -|-
   |
+-----+
|     |
|     |
|     |
+-----+
""",
"""
  -|-
   |
+-----+
|  R  |
|     |
|     |
+-----+
""",
"""
  -|-
   |
+-----+
|  R  |
|  I  |
|     |
+-----+
""",
"""
  -|-
   |
+-----+
|  R  |
|  I  |
|  P  |
+-----+
""",
]

def uprav_aktualni(tajne : str, aktualni : str, pismenko : str) -> str:
    vysledek = ""
    for i in range(len(tajne)):
        if pismenko == tajne[i]:
            vysledek = vysledek + pismenko
        else:
            vysledek = vysledek + aktualni[i]
    return vysledek

def vytiskni_obrazek(chyby : int):
    print(STAVY[chyby])

secret = "šlamastika"
chyby = 0
aktualni = len(secret) * "_"
while True:
    vytiskni_obrazek(chyby)
    print(aktualni,end="\n")
    print("Zadej písmenko frajere: ",end="")
    p = input()
    if p not in secret:
        chyby += 1
    else:
        aktualni = uprav_aktualni(secret,aktualni,p)
    if chyby >= len(STAVY):
        print("Ty jsi ale jelito! Na to, kolik jsi měl pokusů jsi moc velký divadlo nezahrál.")
        break
    if aktualni == secret:
        print("Jsi naprostá legenda!")
        break