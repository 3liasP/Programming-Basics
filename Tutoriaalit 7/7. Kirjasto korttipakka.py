import random

def anna_pakka() -> list:
    hertta = 0
    pata = 0
    ruutu = 0
    risti = 0

    pakka = []

    while hertta < 13:
        hertta += 1
        y = "hertta"
        x = hertta
        kortti = (y, x)
        pakka.append(kortti)

    while pata < 13:
        pata += 1
        y = "pata"
        x = pata
        kortti = (y, x)
        pakka.append(kortti)

    while ruutu < 13:
        ruutu += 1
        y = "ruutu"
        x = ruutu
        kortti = (y, x)
        pakka.append(kortti)

    while risti < 13:
        risti += 1
        y = "risti"
        x = risti
        kortti = (y, x)
        pakka.append(kortti)

    return pakka

def jaa(pakka: list, maara: int) -> list:
    kasi = []
    x = 0
    while x < maara:
        kasi.append(pakka[x])
        x += 1
    del pakka[:maara]
    return kasi


    
def sekoita(pakka: list):
    mix = random.shuffle(pakka)
    return mix

print(jaa(anna_pakka(),4))

