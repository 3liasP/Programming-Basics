def tulosta_pyoreat(luku: float, viesti: str):
    maara = round(luku)
    laskuri = 1
    while laskuri <= maara:
        print(viesti)
        laskuri += 1

tulosta_pyoreat(4.49, "Heippa")