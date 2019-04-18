# Napis funkci, ktera dostane seznam celych cisel a vrati novy seznam, ktery obsahuje jen ta cisla, ktera jsou kladna

seznam = [1, -5, 4, -12, 3, -7, 0, 11]

def zpracuj(seznam):
    vysledek = []
    for cislo in seznam:
        if cislo >= 0:
            vysledek.append(cislo)
    return vysledek

print(zpracuj(seznam))
