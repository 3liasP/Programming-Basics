lista = []

with open("nimet.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()
        lista.append(rivi)

    aakkoslista = sorted(lista)
    for nimi in aakkoslista:
        print(nimi)
