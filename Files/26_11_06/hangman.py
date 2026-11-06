tajne = "bananabread"
pismenko = "a"

def vytiskni_nove(tajne,pismenko):
    nove = ""
    for i in range(len(tajne)):
        if tajne[i] == pismenko:
            nove += pismenko
        else:
            nove += "_"
    return nove

v = vytiskni_nove(tajne,pismenko)
print(v)