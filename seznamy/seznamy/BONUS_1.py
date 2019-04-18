# Napis funkci, ktera dostane seznam, odstrani posledni dva prvky a zbytek vrati jako setrideny seznam

seznam = [1, 5, 4, 12, 3, 7, 11]

def zpracuj(seznam):
    vysledek = seznam[:-2]
    vysledek.sort()
    return vysledek

print(zpracuj(seznam))
