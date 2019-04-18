# Napis funkci, ktera dostane seznam a vrati True pokud obsahuje nejake duplicitni hodnoty, jinak vrati false

unikatni_seznam = [1, 5, 4, 12]
duplicitni_seznam = [1, 5, 4, 1]

def obsahuje_duplicity(seznam):
    seznam.sort()
    for prvek in seznam:
        if seznam.count(prvek) > 1:
            return True
    return False

print(obsahuje_duplicity(duplicitni_seznam))
print(obsahuje_duplicity(unikatni_seznam))


def obsahuje_duplicity_efektivne(seznam):
    return len(seznam) != len(set(seznam))

print(obsahuje_duplicity_efektivne(duplicitni_seznam))
print(obsahuje_duplicity_efektivne(unikatni_seznam))
