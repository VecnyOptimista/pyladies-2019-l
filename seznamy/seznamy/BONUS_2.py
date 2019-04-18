# Napis funkci, ktera dostane seznam a bude vracet novy seznam, ve kterem budou pouze dva nahodne vybrane prvky z puvodniho seznamu

seznam = [1, 5, 4, 12, 3, 7, 11]

def zpracuj(seznam):
    vysledek = seznam[:-2]
    vysledek.sort()
    return vysledek

print(zpracuj(seznam))
