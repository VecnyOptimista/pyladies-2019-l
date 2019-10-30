#!/usr/bin/env python3

# Napis funkci ktera obdrzi na vstupu seznam celych cisel
# a vrati to nejvetsi z nich

# Priklad
# vrat_nejvetsi([1,5,12,3,7])  # vrati 12
# vrat_nejvetsi([1,1,3,1,3])  # vrati 3

def vrat_nejvetsi(seznam):
    setrideny_seznam = sorted(seznam, reverse=True)
    return setrideny_seznam[0]

print(vrat_nejvetsi([1,5,12,3,7]))

def vrat_nejvetsi_2(seznam):
    return max(seznam)

print(vrat_nejvetsi_2([1,5,12,3,7]))

