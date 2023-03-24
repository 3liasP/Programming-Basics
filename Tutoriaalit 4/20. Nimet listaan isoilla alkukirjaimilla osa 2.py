lista = []

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        print(f"Nimet: {lista}")
        break
    if "-" in nimi:
        nimilman = nimi.replace(nimi[0], "", 1)
        alku = nimi[0].upper()
        nimi = alku + nimilman

        viiva = nimi.find("-")
        tokaalku = nimi[viiva + 1].upper()
        tokanimi = nimi.replace(nimi[viiva + 1], tokaalku, 1)
        nimi = tokanimi

        lista.append(nimi)
        
    else:
        nimilman = nimi.replace(nimi[0], "", 1)
        alku = nimi[0].upper()
        nimi = alku + nimilman
        lista.append(nimi)