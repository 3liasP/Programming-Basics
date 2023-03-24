import random

def arvo_ryhma(koko: int) -> list:
    x = 0
    arvaus = ""
    ryhma = []
    lista = []
    with open("nimet.txt") as tiedosto:
        for nimi in tiedosto:
            nimi = nimi.replace("\n","")
            lista.append(nimi)

    while x < koko:
        arvaus = random.choice(lista)
        if arvaus in ryhma:
            pass
        else:
            ryhma.append(arvaus)
            x += 1
    return ryhma
print(arvo_ryhma(3))