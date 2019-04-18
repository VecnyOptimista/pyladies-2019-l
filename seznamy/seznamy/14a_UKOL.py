#!/usr/bin/env python3

# Napis funkci ktera dostane dva vstupni argumenty. Obsah a nasobitel. Obsah muze byt string, nebo cislo
# Tato funkce vytvori seznam, ve kterem se bude X krat opakovat "Obsah". Cislo X je nasobitel.


# Priklad:
# namnozit('X', 3)  # Vyjde ['X', 'X', 'X']
# namnozit(1, 5)  # Vyjde [1, 1, 1, 1, 1]


def namnozit(obsah, nasobitel):
    return [obsah] * nasobitel

print(namnozit('X', 3))
print(namnozit(1, 5))
