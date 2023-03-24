def lue_hedelmat() -> dict:
    with open("hedelmat.csv") as tiedosto:
        hedelmat = {}
        for rivi in tiedosto:
            tiedot_rivilla = rivi.strip().split(";")
            hedelmat[tiedot_rivilla[0]] = float(tiedot_rivilla[1])
    return hedelmat

print(lue_hedelmat())