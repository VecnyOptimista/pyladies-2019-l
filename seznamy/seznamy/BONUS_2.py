# Napis funkci, ktera dostane seznam a bude vracet novy seznam, ve kterem budou pouze dva nahodne vybrane prvky z puvodniho seznamu
import random


seznam = [1, 5, 4, 12, 3, 7, 11]

def zpracuj(seznam):
    vysledek = []
    for step in range(2):
        vysledek.append(seznam[random.randint(0, len(seznam) - 1)])
    return vysledek

print(zpracuj(seznam))
