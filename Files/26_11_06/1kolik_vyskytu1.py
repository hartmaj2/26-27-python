import time

text = "Český rozhlas (ČRo) je veřejnoprávní instituce provozující celoplošné rozhlasové vysílání na území Česka. Zřízen byl v roce 1992 zákonem o Českém rozhlasu, který stanovuje rámec jeho fungování, včetně plnění úkolů veřejné služby v oblasti rozhlasového vysílání a způsobu financování. Jako médium veřejné služby má zajišťovat všem občanům přístup k informacím, kultuře, vzdělání a zábavě. Působí jako nástupce předchozího státního Československého rozhlasu. Vysílá na 12 celoplošných a 14 regionálních stanicích, včetně zahraničního vysílání na objednávku státu. Sídlí v Praze v budově ve Vinohradské třídě. Generálním ředitelem Českého rozhlasu je od roku 2016 René Zavoral."

pocet = 0

i = 0
while True:
    # print(text[i])
    if text[i] == "a":
        pocet += 1
    i = i + 1
    if i >= len(text):
        break
    # time.sleep(0.1)

print(pocet)