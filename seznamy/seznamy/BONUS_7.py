# Napis funkci, ktera pomoci cyklu vytvori vnoreny seznam podle nasledujiciho vzoru. Kazdy radek predstavuje jeden vnoreny seznam.

# [
#     [O, X, X, X, X],
#     [X, O, X, X, X],
#     [X, X, O, X, X],
#     [X, X, X, O, X],
#     [X, X, X, X, O],
# ]


def generuj_piskvorky(velikost):
    vysledek = []

    for radek in range(velikost):
        seznam_radku = []
        for bunka in range(velikost):
            if bunka == radek:
                seznam_radku.append("O")
            else:
                seznam_radku.append("X")
        vysledek.append(seznam_radku)
    return vysledek


for radek in generuj_piskvorky(5):
    print(radek)
