#!/usr/bin/env python3

# Napis funkci ktera obdrzi na vstupu seznam celych cisel
# a vrati posledni dva z nich

# Priklad
# vrat_posledni_dva([9,8,12,3,7])  # vrati 3, 7
# vrat_posledni_dva([6,2,3,8,4])  # vrati 8, 4

def vrat_posledni_dva(seznam):
    return seznam[-2:]

print(vrat_posledni_dva([9,8,12,3,7]))
print(vrat_posledni_dva([6,2,3,8,4]))
