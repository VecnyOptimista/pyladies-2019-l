# Napis funkci ktera pro dany retezec vrati pocet vyskytu slova "ale"


text = "To jsem se ale zapotil pri psani tohoto ukolu. Ted uz to ale mam vsechno hotove."

def zpracuj(text):
    slova = text.split(" ")
    vysledek = slova.count("ale")
    return vysledek

print(zpracuj(text))
