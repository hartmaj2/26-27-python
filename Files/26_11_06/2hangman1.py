
# ukol: dostaneme slovo a pismenko, nasim ukolem je vytvorit vysledek tvaru __x_x_x
# kde x je na pozicich, kde se nachazi pismenko

def zkus_pismenko(tajne : str, aktualni : str, pismenko : str) -> str:
    vysledek = ""
    for i in range(len(tajne)):
        if pismenko == tajne[i]:
            vysledek = vysledek + pismenko
        else:
            vysledek = vysledek + aktualni[i]
    return vysledek


secret = "šlamastika"
aktualni = len(secret) * "_"
while True:
    print("Zadej písmenko: ",end="")
    p = input()
    aktualni = zkus_pismenko(secret,aktualni,p)
    print(aktualni)